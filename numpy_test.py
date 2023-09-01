import unittest
import numpy


class NumpyTestCase(unittest.TestCase):
    """A basic check that sufficient numpy dependency is loaded to do basic work.

    Numpy in past has cross-platform, cross-version, and wheel issues:
    1. python setup assumes that the build platform is the run platform; this shows up when a
        dependency tries to load some compiled/optimized component such as
        `numpy.core._multiarray_umath`:
    1.1. bulding on Mac, but running on linux, the loader looks for a
        `site-packages/numpy/core/_multiarray_umath.cpython-39-linux.so` for there's only a
        `site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so`
    1.2. building on ARM HW but running on x86_64 linux, as was most of available AWS EC2, if
        `_multiarray_umath.cpython-39-linux.so` was found, the ARM .so didn't provide what the
        x86-64 `ldd` needed
    1.3. building on python-3.11, but running on python-3.9 or vice-versa, the loader searching for
        `_multiarray_umath.cpython-39-linux.so` would not see the `_multiarray_umath.cpython-311-linux.so`
        provided during build
    2. module authors don't often have the awareness for cross-platform, or the hardware to check
    3. Python setup is a great place to hide idiosyncrasies of your setup; this hidden logic is
        hard to make work in cross-platform, cross-arch, or cross-version, and it doesn't fail
        consistently ("works on my system, dunno your problem")

    ... so we load some part of numpy to see whether it'll do what needs to be done.  It's possible
    that this simple test doesn't do neough to trigger the loading of custom optimized code, but we
    can extend this unittest when we discover a shortfall.
    """

    def test_shape(self):
        """Simple test hoping to have enough coverage to trigger any additional module load"""

        a = numpy.arange(6)
        a2 = a[numpy.newaxis, :]

        self.assertIsNotNone(a2)

        self.assertEqual(a2.shape, (1, 6))


if __name__ == "__main__":
    unittest.main()
