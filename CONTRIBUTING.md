# Contributing to RTC-Tools 2

## Version Numbering and Release Cycle

For version numbers we use the guidelines described in <https://semver.org>:

> Given a version number MAJOR.MINOR.PATCH, increment the:
> 
> 1. MAJOR version when you make incompatible API changes
> 2. MINOR version when you add functionality in a backward compatible manner
> 3. PATCH version when you make backward compatible bug fixes
> 
> Additional labels for pre-release and build metadata are available
> as extensions to the MAJOR.MINOR.PATCH format.

The development of a new MINOR version in RTC-Tools consists of four stages:

1. Alpha (a): Version that is not yet feature complete and may contain bugs.
    Each alpha release can either fix bugs or add new features.
2. Beta (b): Version that is feature complete but is likely to contain bugs.
    After a beta version has been created, no new features can be added anymore.
    A beta version is tested more thoroughly.
3. Release candidate (rc): Version that has been tested through the beta versions releases
    and can now be tested as if it were the stable release.
    If bugs still pop up, new RC versions can be created to fix them.
    Additions are allowed but should be code-unrelated,
    such as changes to the documentation required for the release.
4. Stable release: Final version that has passed all tests.

There can be multiple alpha-, beta-, and rc-versions,
but we should not go back to a previous stage.

An example of a release sequence is:

- 2.6.0a1 Add a feature.
- 2.6.0a2 Add another feature and fix a bug.
- 2.6.0b1 First beta release.
- 2.6.0b2 Fixed a bug.
- 2.6.0b3 Fixed another bug.
- 2.6.0rc1 First release candidate after having tested thoroughly.
- 2.6.0rc2 Fixed a bug that did not show up in the standard tests.
- 2.6.0 **Stable release**.
    No changes were made after last release candidate.
- 2.6.1 Fixed a bug.
- 2.6.2 Fixed another bug.

If we start with a new release cycle for X.Y+1,
and still want to fix a bug for the previous version X.Y,
we create a separate branch `maintenance/X.Y` where we add patches for X.Y.

## Release Notes

Before creating a release, make sure that the release notes are updated in
[RELEASE_NOTES.md](RELEASE_NOTES.md).


## Commits and Commit Messages

Each commit ideally satisfies the following:

- Each commit has a clear and single purpose.
- After each commit, all unit tests should still pass.

Commit messages should have the following structure:

```text
<scope>: <short description>

<complete description>
```

- scope: explains which part of the code is affected, e.g.:
    - optimization (only affects the optimization part)
    - homotopy_mixin (only affects the homotopy_mixin module)
    - tests (only affects the tests)
    - doc (only affects the documentation)
- short description: describes what is changed in the commit with a single sentence.
- complete description: explain in detail what is done in the commit and why.
    This can take up multiple paragraphs.
