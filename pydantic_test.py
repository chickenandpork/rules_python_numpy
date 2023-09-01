from datetime import datetime
from pydantic import BaseModel
from typing import Tuple

import unittest


class Delivery(BaseModel):
    """A Delivery is a basic struct to trigger some schema behavior in Pydantic"""

    timestamp: datetime
    dimensions: Tuple[int, int]


class DoesItEvenLoadPydanticTestCase(unittest.TestCase):
    """A basic check that sufficient pydantic dependency is loaded to do basic work.

    In past, Pydantic-Core has shown cross-platform, cross-version, and wheel issues, appearing as error messages such as:

        No module named 'pydantic_core._pydantic_core'

    This pops up even though the dependency is clearly present.  The key is looking at the resource
    name: I only see "_<thing>" naming -- prefixed with an underscore("_") -- as cpython
    compiled/optimized, typically backed by a shared object ("DLL", .dlsym,  or .so)

    1. python setup assumes that the build platform is the run platform; this shows up when a
        dependency tries to load some compiled/optimized component such as
        `site-packages/pydantic_core/_pydantic_core.cpython-39-linux.so`
    1.1. bulding on Mac, but running on linux, the loader looks for a
        `site-packages/numpy/pydantic_core/_pydantic_core.cpython-39-linux.so` for there's only a
        `site-packages/numpy/pydantic_core/_pydantic_core.cpython-39-darwin.so`
    1.2. building on ARM HW but running on x86_64 linux, as was most of available AWS EC2, if
        `_pydantic_core.cpython-39-linux.so` was found, the ARM .so didn't provide what the
        x86-64 `ldd` needed
    1.3. building on python-3.11, but running on python-3.9 or vice-versa, the loader searching for
        `_pydantic_core.cpython-39-linux.so` would not see the `_pydantic_core.cpython-311-linux.so`
        provided during build
    2. module authors don't often have the awareness for cross-platform, or the hardware to check
    3. Python setup is a great place to hide idiosyncrasies of your setup; this hidden logic is
        hard to make work in cross-platform, cross-arch, or cross-version, and it doesn't fail
        consistently ("works on my system, dunno your problem")

    ... so we load some part of numpy to see whether it'll do what needs to be done.  It's possible
    that this simple test doesn't do neough to trigger the loading of custom optimized code, but we
    can extend this unittest when we discover a shortfall.
    """

    def test_inference(self):
        """Simple test hoping to have enough coverage to trigger any additional module load"""

        m = Delivery(timestamp="2020-01-02T03:04:05Z", dimensions=["10", "20"])

        self.assertIsNotNone(m)
        self.assertIsNotNone(m.dimensions)

        self.assertEqual(m.dimensions, (10, 20))


if __name__ == "__main__":
    unittest.main()
