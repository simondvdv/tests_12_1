import unittest
import tests_12_3 as t

all_tests = unittest.TestSuite()
all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(t.RunnerTest))
all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(t.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(all_tests)

