from unittest import TestCase

import multiples

class TestGetLowestCommonMultiple(TestCase):
    def test_gets_lcm_for_24_10_15_correctly(self):
        self.assertEqual(
            multiples.get_lcm([24, 10, 15]), 120
        )

    def test_gets_lcm_for_543_21_43(self):
        self.assertEqual(
            multiples.get_lcm([543, 21, 43]), 163443
        )