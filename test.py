import unittest
import GHAnalysis

class MyClassTest(unittest.TestCase):
    def test_queryu(self):
        self.my_data = GHAnalysis.Data('.')
        self.my_data = GHAnalysis.Data()
        self.assertEqual(self.my_data.get_cnt_user('rspt', 'PushEvent'), 1)

    def test_queryr(self):
        self.my_data = GHAnalysis.Data('.')
        self.my_data = GHAnalysis.Data()
        self.assertEqual(self.my_data.get_cnt_repo('rspt/rspt-theme', 'PushEvent'), 1)


    def test_queryru(self):
        self.my_data = GHAnalysis.Data('.')
        self.my_data = GHAnalysis.Data()
        self.assertEqual(self.my_data.get_cnt_user_and_repo('rspt', 'rspt/rspt-theme', 'PushEvent'), 1)


if __name__ == '__main__':
    unittest.main()
