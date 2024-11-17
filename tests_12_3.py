import unittest
from tests_12_1 import Runner
from tests_12_2 import TournamentTest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r1 = Runner('John')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r1 = Runner('John')
        for _ in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner('John')
        r2 = Runner('Kael')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = runner.Runner('Усэйн', 10)
        self.r2 = runner.Runner('Андрей', 9)
        self.r3 = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            print_string = '{'
            for key, value in i.items():
                print_string += f'{key}: {value}'
                if key == len(i):
                    print_string += '}'
                    break
                print_string += ', '
            print(print_string)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_1(self):
        self.tour = runner.Tournament(90, self.r1, self.r3)
        self.all_results = self.tour.start()
        self.assertTrue('Ник' == self.all_results[len(self.all_results)].name)
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        self.tour = runner.Tournament(90, self.r2, self.r3)
        self.all_results = self.tour.start()
        self.assertTrue('Ник' == self.all_results[len(self.all_results)].name)
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_3(self):
        self.tour = runner.Tournament(90, self.r1, self.r3, self.r2)
        self.all_results = self.tour.start()
        self.assertTrue('Ник' == self.all_results[len(self.all_results)].name)
        TournamentTest.all_results[3] = self.all_results


if __name__ == "__main__":
    unittest.main()