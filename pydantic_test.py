import unittest
from datetime import datetime
from typing import Tuple

from pydantic import BaseModel

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]



class DoesItEvenLoadPydanticTestCase(unittest.TestCase):

    def test_inference(self):
        m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])

        self.assertIsNotNone(m)
        self.assertIsNotNone(m.dimensions)

        self.assertEqual(m.dimensions, (10,20))

if __name__ == "__main__":
    unittest.main()
