from unittest import TestCase

import points

class TestCoords(TestCase):
    def test_correct_coords_are_returned(self):
        p1 = points.Point3D(2, 3, 4)
        self.assertEqual(
            p1.coords,
            (2, 3, 4)
        )