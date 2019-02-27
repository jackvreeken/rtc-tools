import unittest

import casadi as ca

import numpy as np

from rtctools.optimization.timeseries import Timeseries


class TestTimeseries(unittest.TestCase):

    def test_dm(self):
        ts = Timeseries([1, 2, 3], ca.DM([1, 2, 3]))
        self.assertTrue(np.array_equal(ts.values, np.array([1, 2, 3])))
        self.assertEqual(ts.values.dtype, np.float64)

    def test_broadcast_scalar(self):
        ts = Timeseries([1, 2, 3], 4)
        self.assertTrue(np.array_equal(ts.values, np.array([4, 4, 4])))
        self.assertEqual(ts.values.dtype, np.float64)

    def test_broadcast_single_element(self):
        ts = Timeseries([1, 2, 3], [4])
        self.assertTrue(np.array_equal(ts.values, np.array([4, 4, 4])))
        self.assertEqual(ts.values.dtype, np.float64)

    def test_numpy_array(self):
        vals = np.array([1, 2, 3], dtype=np.float64)
        ts = Timeseries([1, 2, 3], vals)
        self.assertTrue(np.array_equal(ts.values, vals))
        self.assertEqual(ts.values.dtype, np.float64)
        self.assertFalse(vals is ts.values)  # Make sure a copy was made

    def test_list(self):
        vals = [1, 2, 3]
        ts = Timeseries([1, 2, 3], vals)
        self.assertTrue(np.array_equal(ts.values, np.array(vals, dtype=np.float64)))
        self.assertEqual(ts.values.dtype, np.float64)
