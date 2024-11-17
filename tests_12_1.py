import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r1 = Runner('John')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        r1 = Runner('John')
        for _ in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    def test_challenge(self):
        r1 = Runner('John')
        r2 = Runner('Kael')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

if __name__ == '__main__':
    unittest.main()