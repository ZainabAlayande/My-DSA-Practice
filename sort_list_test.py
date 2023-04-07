from unittest import TestCase
from DSA.sort_list_algorithm import sort_list


class TestSort_List(TestCase):

    def test_one_for_unsorted_list(self):
        the_list = [34, 12, 98, 3, 1, 9, 100, 500, 25, 2, 1, 0, 15, 33]
        expected = [0, 1, 1, 2, 3, 9, 12, 15, 25, 33, 34, 98, 100, 500]
        actual = sort_list.sort(the_list)
        self.assertListEqual(expected, actual)

    def test_two_for_unsorted_list(self):
        the_list = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
        expected = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        actual = sort_list.sort(the_list)
        self.assertListEqual(expected, actual)

    def test_three_for_unsorted_list(self):
        the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = sort_list.sort(the_list)
        self.assertListEqual(expected, actual)
