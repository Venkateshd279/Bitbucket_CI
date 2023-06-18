import unittest
import app
import numpy as np

class TestApp(unittest.TestCase):

    def test_numeric_add_one(self):
        array = np.array([1, 2, 3])
        answer = np.array([2, 3, 4])
        np.testing.assert_array_equal(app.add_one(array), answer)

    def test_nan_add_one(self):
        array = np.array([np.nan, 2, 3])
        answer = np.array([np.nan, 3, 4])
        np.testing.assert_array_equal(app.add_one(array), answer)

if __name__ == '__main__':
    unittest.main()
