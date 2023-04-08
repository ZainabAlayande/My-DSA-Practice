from unittest import TestCase
from DSA.lcmAlgorithm import lowest_common_multiple


class Test_Lowest_Multiple(TestCase):

    def test_get_lcm_of_1(self):
        actual = lowest_common_multiple.get_lcm(1)
        expected = [1]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_2(self):
        actual = lowest_common_multiple.get_lcm(2)
        expected = [2, 1]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_4(self):
        actual = lowest_common_multiple.get_lcm(4)
        expected = [2, 2]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_6(self):
        actual = lowest_common_multiple.get_lcm(6)
        expected = [2, 3]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_8(self):
        actual = lowest_common_multiple.get_lcm(8)
        expected = [2, 2, 2]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_15(self):
        actual = lowest_common_multiple.get_lcm(15)
        expected = [3, 5]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_20(self):
        actual = lowest_common_multiple.get_lcm(20)
        expected = [2, 2, 5]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_50(self):
        actual = lowest_common_multiple.get_lcm(50)
        expected = [2, 5, 5]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_100(self):
        actual = lowest_common_multiple.get_lcm(100)
        expected = [2, 2, 5, 5]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_1000(self):
        actual = lowest_common_multiple.get_lcm(1000)
        expected = [2, 2, 2, 5, 5, 5]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_20000(self):
        actual = lowest_common_multiple.get_lcm(20000)
        expected = [2, 2, 2, 2, 2, 5, 5, 5, 5]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_500000(self):
        actual = lowest_common_multiple.get_lcm(500000)
        expected = [2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5]
        self.assertEqual(expected, actual)

    def test_get_lcm_of_1000000(self):
        actual = lowest_common_multiple.get_lcm(1000000)
        expected = [2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5]
        self.assertEqual(expected, actual)

