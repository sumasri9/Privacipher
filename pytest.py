import redactor
import unittest
import glob
path = glob.glob('1.txt')
class Test(unittest.TestCase):
    def test1(self):
        for file in path:
            with open(file, 'r',encoding="utf-8") as file:
                text = file.read()
            result = redactor.phone_number(text)
        self.assertIsNotNone(result,"didn't return any value")
    def test2(self):
        for file in path:
            with open(file, 'r',encoding="utf-8") as file:
                text = file.read()
            result = redactor.gender(text)
        self.assertIsNotNone(result,"didn't return any value")
    def test3(self):
        for file in path:
            with open(file, 'r',encoding="utf-8") as file:
                text = file.read()
            result = redactor.date(text)
        self.assertIsNotNone(result,"didn't return any value")
    def test4(self):
        for file in path:
            with open(file, 'r',encoding="utf-8") as file:
                text = file.read()
            result = redactor.names(text)
        self.assertIsNotNone(result,"didn't return any value")
    def test5(self):
        for file in path:
            with open(file, 'r',encoding="utf-8") as file:
                text = file.read()
            result = redactor.address(text)
        self.assertIsNotNone(result,"didn't return any value")
if __name__ == '__main__':
    unittest.main()
