import unittest
import main


class Testmain(unittest.TestCase):
    def test1(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test2(self):
        test_param = "Mohammad"
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))


unittest.main()
