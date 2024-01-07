import unittest
from s3sync.utils import chunks


class TestChunksFunction(unittest.TestCase):
    def test_empty_list(self):
        lst = []
        result = list(chunks(lst, 2))
        self.assertEqual(result, [])

    def test_even_chunks(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = list(chunks(lst, 3))
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_odd_chunks(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = list(chunks(lst, 2))
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6], [7, 8], [9]])

    def test_fewer_elements_than_n(self):
        lst = [1, 2, 3]
        result = list(chunks(lst, 5))
        self.assertEqual(result, [[1, 2, 3]])

    def test_single_element(self):
        lst = [42]
        result = list(chunks(lst, 1))
        self.assertEqual(result, [[42]])


if __name__ == "__main__":
    unittest.main()
