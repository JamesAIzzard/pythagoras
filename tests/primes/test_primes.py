from unittest import TestCase

import primes

class TestCheckIfPrime(TestCase):
    def test_returns_true_for_2(self):
        self.assertTrue(primes.check_if_prime(2))

    def test_returns_true_for_3(self):
        self.assertTrue(primes.check_if_prime(3))

    def test_returns_false_for_9(self):
        self.assertFalse(primes.check_if_prime(9))

    def test_returns_false_for_1(self):
        self.assertFalse(primes.check_if_prime(1))

    def test_returns_false_for_0(self):
        self.assertFalse(primes.check_if_prime(0))

    def test_returns_false_for_neg_1(self):
        self.assertFalse(primes.check_if_prime(-1))

class TestGetPrimesSmallerThan(TestCase):
    def test_lists_primes_before_23_correctly(self):
        self.assertEqual(
            primes.get_primes_smaller_than(23),
            [2, 3, 5, 7, 11, 13, 17, 19]
        )

class TestFindPrimeFactors(TestCase):
    def test_factorises_1_correctly(self):
        self.assertEqual(
            primes.find_prime_factors(1), {}
        )

    def test_factorises_2_correctly(self):
        self.assertEqual(
            primes.find_prime_factors(2),
            {2:1}
        )
    
    def test_factorises_10_correctly(self):
        self.assertEqual(
            primes.find_prime_factors(10),
            {
                2: 1,
                5: 1
            }
        )

    def test_factorises_15_correctly(self):
        self.assertEqual(
            primes.find_prime_factors(15),
            {
                3: 1,
                5: 1
            }
        )

    def test_factorises_24_correctly(self):
        self.assertEqual(
            primes.find_prime_factors(24),
            {
                2: 3,
                3: 1
            }
        )

    def test_factorises_360_correctly(self):
        self.assertEqual(
            primes.find_prime_factors(360),
            {
                2: 3,
                3: 2,
                5: 1
            }
        )