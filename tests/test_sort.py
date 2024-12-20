import operator
import unittest

from utils.utils import merge_sort


class UtilsTestCase(unittest.TestCase):

    def test_merge_sort(self):
        a = [3, 1, 6, 2, 5, 4]
        result = merge_sort(a)

        self.assertEqual(a, [3, 1, 6, 2, 5, 4])
        self.assertEqual(result, sorted(a))


        result = merge_sort(a, operator.gt)

        self.assertEqual(a, [3, 1, 6, 2, 5, 4])
        self.assertEqual(result, sorted(a, reverse=True))

        b = ["abc", "a", "bc", "bcde", "ccccc"]

        result = merge_sort(b, lambda x, y: len(x) < len(y))

        self.assertEqual(b, ["abc", "a", "bc", "bcde", "ccccc"])
        self.assertEqual(result, ["a", "bc", "abc", "bcde", "ccccc"])



