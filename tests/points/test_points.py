from unittest import TestCase

import points

class TestGetDistBetweenPoints(TestCase):
    def test_correct_distance_is_returned(self):
        p1 = points.Point3D(1, 2, 3)
        p2 = points.Point3D(-1, -2, -3)
        self.assertAlmostEqual(
            points.get_dist_between_points(p1, p2),
            7.483,
            delta=0.001
        )