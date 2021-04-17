import unittest
from 函数 import get_formatted_name_1


# 可通过的测试


class NameTestCase(unittest.TestCase):
    '''测试函数.py文件里的函数'''

    def test_first_last_name(self):
        username = get_formatted_name_1('lucky', 'baby')
        self.assertEqual(username, 'Lucky Baby')


# unittest.main()

# 不可通过的测试


def get_formatted_name(first, middle, last):
    username = first + ' ' + middle + ' ' + last
    return username.title()


class NameTestCase_2(unittest.TestCase):
    '''测试函数.py文件里的函数'''


"""     def test_first_last_name(self):
        username = get_formatted_name('lucky', 'baby')
        self.assertEqual(username, 'Lucky Baby') """


# unittest.main()

# 修改不可通过的测试的代码


def get_formatted_name_3(first, last, middle=''):
    if middle:
        username = first + ' ' + middle + ' ' + last
    else:
        username = first + ' ' + last
    return username.title()


class NameTestCase_3(unittest.TestCase):
    '''测试函数.py文件里的函数'''

    def test_first_last_name(self):
        username = get_formatted_name_3('lucky', 'baby')
        self.assertEqual(username, 'Lucky Baby')

    def test_first_middle_last_name(self):
        username = get_formatted_name_3('lucky', 'baby', 'luu')
        self.assertEqual(username, 'Lucky Luu Baby')


# unittest.main()

# 测试类


class AnonymousSurvey():
    '''匿名类调查问卷'''

    def __init__(self, question):
        '''存储一个问题'''
        self.question = question
        self.response = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.response.append(new_response)

    def show_response(self):
        print("Survey results:")
        for res in self.response:
            print("-", res)


question = 'What language did you first learn it?'

my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("enter 'q' to quit.")
while True:
    res = input("Language:")
    if res == 'q':
        break
    my_survey.store_response(res)
my_survey.show_response()

# 测试AnonymousSurvey类


class TestAnonymousSurvey(unittest.TestCase):
    '''测试AnonymousSurvey类'''

    def test_store_single_response(self):
        '''测试存储回复功能'''
        question = 'What language did you first learn it?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('PHP')
        self.assertIn('PHP', my_survey.response)


unittest.main()
