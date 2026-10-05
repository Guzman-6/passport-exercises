import unittest

from passport_example import total_memory_gib


class TotalMemoryTests(unittest.TestCase):
    def test_one_cpu(self) -> None:
        self.assertEqual(total_memory_gib(1, 3), 3)

    def test_multiple_cpus(self) -> None:
        self.assertEqual(total_memory_gib(4, 3), 12)


if __name__ == "__main__":
    unittest.main()
