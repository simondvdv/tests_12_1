import runner
import unittest


class TournamentTest(unittest.TestCase):
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

    def test_tour_1(self):
        self.tour = runner.Tournament(90, self.r1, self.r3)
        self.all_results = self.tour.start()
        self.assertTrue('Ник' == self.all_results[len(self.all_results)].name)
        TournamentTest.all_results[1] = self.all_results

    def test_tour_2(self):
        self.tour = runner.Tournament(90, self.r2, self.r3)
        self.all_results = self.tour.start()
        self.assertTrue('Ник' == self.all_results[len(self.all_results)].name)
        TournamentTest.all_results[2] = self.all_results

    def test_tour_3(self):
        self.tour = runner.Tournament(90, self.r1, self.r3, self.r2)
        self.all_results = self.tour.start()
        self.assertTrue('Ник' == self.all_results[len(self.all_results)].name)
        TournamentTest.all_results[3] = self.all_results
