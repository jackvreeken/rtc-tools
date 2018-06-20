import collections

from pymoca.backends.casadi.alias_relation import AliasRelation  # noqa: F401


class OrderedSet(collections.MutableSet):
    """
    Adapted from https://code.activestate.com/recipes/576694/
    with some additional methods:
    __getstate__, __setstate__, __getitem__
    """

    def __init__(self, iterable=None):
        self.end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def __getstate__(self):
        """ Avoids max depth RecursionError when using pickle """
        return list(self)

    def __setstate__(self, state):
        """ Tells pickle how to restore instance """
        self.__init__(state)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, stride = index.indices(len(self))
            return [self.__getitem__(i) for i in range(start, stop, stride)]
        else:
            end = self.end
            curr = end[2]
            i = 0
            while curr is not end:
                if i == index:
                    return curr[0]
                curr = curr[2]
                i += 1
            raise IndexError('set index {} out of range with length {}'.format(index, len(self)))

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)
# End snippet


class AliasDict:
    def __init__(self, relation, other=None, signed_values=True):
        self.__relation = relation
        self.__d = {}
        self.__signed_values = signed_values
        if other:
            self.update(other)

    def __canonical_signed(self, key):
        var, sign = self.__relation.canonical_signed(key)
        if self.__signed_values:
            return var, sign
        else:
            return var, 1

    def __setitem__(self, key, val):
        var, sign = self.__canonical_signed(key)
        if isinstance(val, tuple):
            self.__d[var] = [-c if sign < 0 else c for c in val]
        else:
            self.__d[var] = -val if sign < 0 else val

    def __getitem__(self, key):
        var, sign = self.__canonical_signed(key)
        val = self.__d[var]
        if isinstance(val, tuple):
            return [-c if sign < 0 else c for c in val]
        else:
            return -val if sign < 0 else val

    def __delitem__(self, key):
        var, sign = self.__canonical_signed(key)
        del self.__d[var]

    def __contains__(self, key):
        var, sign = self.__canonical_signed(key)
        return var in self.__d

    def __len__(self):
        return len(self.__d)

    def __iter__(self):
        return iter(self.__d)

    def update(self, other):
        for key, value in other.items():
            self[key] = value

    def get(self, key, default=None):
        if key in self:
            return self[key]
        else:
            return default

    def setdefault(self, key, default):
        if key in self:
            return self[key]
        else:
            self[key] = default
            return default

    def keys(self):
        return self.__d.keys()

    def values(self):
        return self.__d.values()

    def items(self):
        return self.__d.items()
