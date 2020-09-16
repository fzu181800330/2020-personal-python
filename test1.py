import unittest
import GHAnalysis

class MyClassTest(unittest.TestCase):
    def test_queryu(self):#测试查询个人的 4 种事件的数量
        self.my_data = GHAnalysis.Data('.')
        self.my_data = GHAnalysis.Data()
        self.assertEqual(self.my_data.get_cnt_user('rspt', 'PushEvent'), 1)

    def test_queryr(self):#测试每一个项目的 4 种事件的数量
        self.my_data = GHAnalysis.Data('.')
        self.my_data = GHAnalysis.Data()
        self.assertEqual(self.my_data.get_cnt_repo('rspt/rspt-theme', 'PushEvent'), 1)


    def test_queryru(self):#测试每一个人在每一个项目的 4 种事件的数量
        self.my_data = GHAnalysis.Data('.')
        self.my_data = GHAnalysis.Data()
        self.assertEqual(self.my_data.get_cnt_user_and_repo('rspt', 'rspt/rspt-theme', 'PushEvent'), 1)


if __name__ == '__main__':
    unittest.main()
