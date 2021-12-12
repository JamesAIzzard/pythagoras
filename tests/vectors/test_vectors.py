from unittest import TestCase

import vectors, axes, math

class TestMakeVectorFromAngleOnPlane(TestCase):
    def test_makes_pos_45_deg_vector_from_x_on_z_plane_correctly(self):
        v = vectors.make_vector_from_angle_on_plane(
            on_plane=axes.Axes.Z,
            angle_from=axes.Axes.X,
            angle=math.radians(45),
            length=5
        )
        self.assertEqual(v.length, 5)
        self.assertAlmostEqual(v.x, 3.536, delta=0.01)
        self.assertAlmostEqual(v.y, 3.536, delta=0.01)
        self.assertAlmostEqual(v.z, 0, delta=0.01)

    def test_makes_neg_45_deg_vector_from_x_on_z_plane_correctly(self):
        v = vectors.make_vector_from_angle_on_plane(
            on_plane=axes.Axes.Z,
            angle_from=axes.Axes.X,
            angle=math.radians(-45),
            length=5
        )
        self.assertEqual(v.length, 5)
        self.assertAlmostEqual(v.x, 3.536, delta=0.01)
        self.assertAlmostEqual(v.y, -3.536, delta=0.01)
        self.assertAlmostEqual(v.z, 0, delta=0.01)      

    def test_makes_pos_30_deg_vector_from_y_on_z_plane_correctly(self):
        v = vectors.make_vector_from_angle_on_plane(
            on_plane=axes.Axes.Z,
            angle_from=axes.Axes.Y,
            angle=math.radians(30),
            length=5
        )
        self.assertEqual(v.length, 5)
        self.assertAlmostEqual(v.x, -2.5, delta=0.01)
        self.assertAlmostEqual(v.y, 4.33, delta=0.01)
        self.assertAlmostEqual(v.z, 0, delta=0.01)          

    def test_makes_neg_30_deg_vector_from_y_on_z_plane_correctly(self):
        v = vectors.make_vector_from_angle_on_plane(
            on_plane=axes.Axes.Z,
            angle_from=axes.Axes.Y,
            angle=math.radians(-30),
            length=5
        )
        self.assertEqual(v.length, 5)
        self.assertAlmostEqual(v.x, 2.5, delta=0.01)
        self.assertAlmostEqual(v.y, 4.33, delta=0.01)
        self.assertAlmostEqual(v.z, 0, delta=0.01)  