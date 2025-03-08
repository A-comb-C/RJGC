import unittest
import os
import tempfile
from main import main

class TestPlagiarismChecker(unittest.TestCase):
    def setUp(self):
        # 创建临时文件
        self.original_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
        self.plagiarized_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
        self.output_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')

    def tearDown(self):
        # 删除临时文件
        os.unlink(self.original_file.name)
        os.unlink(self.plagiarized_file.name)
        os.unlink(self.output_file.name)

    def test_identical_texts(self):
        """测试完全相同的文本"""
        self.original_file.write("今天是星期天，天气晴，今天晚上我要去看电影。")
        self.original_file.close()
        self.plagiarized_file.write("今天是星期天，天气晴，今天晚上我要去看电影。")
        self.plagiarized_file.close()

        # 运行主程序
        main()

        # 读取输出文件
        with open(self.output_file.name, 'r', encoding='utf-8') as file:
            similarity = float(file.read().strip())
        self.assertEqual(similarity, 1.00)

    def test_different_texts(self):
        """测试完全不同的文本"""
        self.original_file.write("今天是星期天，天气晴，今天晚上我要去看电影。")
        self.original_file.close()
        self.plagiarized_file.write("明天是星期一，天气阴，我明天要去上班。")
        self.plagiarized_file.close()

        # 运行主程序
        main()

        # 读取输出文件
        with open(self.output_file.name, 'r', encoding='utf-8') as file:
            similarity = float(file.read().strip())
        self.assertLess(similarity, 0.5)

    def test_partially_similar_texts(self):
        """测试部分相似的文本"""
        self.original_file.write("今天是星期天，天气晴，今天晚上我要去看电影。")
        self.original_file.close()
        self.plagiarized_file.write("今天是周天，天气晴朗，我晚上要去看电影。")
        self.plagiarized_file.close()

        # 运行主程序
        main()

        # 读取输出文件
        with open(self.output_file.name, 'r', encoding='utf-8') as file:
            similarity = float(file.read().strip())
        self.assertGreater(similarity, 0.7)
        self.assertLess(similarity, 1.0)