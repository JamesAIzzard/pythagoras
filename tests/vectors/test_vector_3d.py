from unittest import TestCase

from vectors import Vector3D

class TestX(TestCase):
    def test_x_returns_correct_value(self):
        v1 = Vector3D(2, 3, 4)
        self.assertEqual(v1.x, 2)

class TestY(TestCase):
    def test_y_returns_correct_value(self):
        v1 = Vector3D(2, 3, 4)
        self.assertEqual(v1.y, 3)

class TestZ(TestCase):
    def test_z_returns_correct_value(self):
        v1 = Vector3D(2, 3, 4)
        self.assertEqual(v1.z, 4)

class TestAddition(TestCase):
    def test_vectors_add_correctly(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(-3, -4, 5)
        v3 = v1 + v2
        self.assertEqual(
            v3.head.coords,
            (-2, -2, 8)
        )

class TestLength(TestCase):
    def test_length_returns_correct_value(self):
        v1 = Vector3D(1, 2, 3)
        self.assertAlmostEqual(
            v1.length,
            3.742,
            delta=0.001
        )