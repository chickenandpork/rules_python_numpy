import unittest
import numpy

class NumpyTestCase(unittest.TestCase):

    def test_shape(self):
        a = numpy.arange(6)
        a2 = a[numpy.newaxis, :]

        self.assertIsNotNone(a2)

        self.assertEqual(a2.shape, (1,6))

if __name__ == "__main__":
    unittest.main()
