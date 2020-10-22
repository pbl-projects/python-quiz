import html
import json
import random
from urllib.request import Request, urlopen

class Question:
    def __init__(self):
        self.question = ''
        self.correct_answer = ''
        self.incorrect_answers = []
        self.type = ''
        self.difficulty = ''
        self.category = ''
        self.suffled_options = []

    def get_answer_string(self):
        options = [self.correct_answer] + self.incorrect_answers
        random.shuffle(options)
        self.suffled_options = options
        s = ''
        c = 1
        for option in options:
            s = s + str(c) + "." + option + '\n'
            c = c + 1
        return s

    def __str__(self):
        return 'Question: ' + self.question + '\n' + self.get_answer_string()

    def ask(self):
        print(self)
        answer = input("Your answer: ")
        i = int(answer)-1
        if self.suffled_options[i] == self.correct_answer:
            return True
        else:
            return False


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current = 0

    def load(self):
        req = Request('https://opentdb.com/api.php?amount=5', headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req).read()
        data = json.loads(response.decode())
        for element in data['results']:
            q = Question()
            q.category = element['category']
            q.type = element['type']
            q.difficulty = element['difficulty']
            q.question = html.unescape(element['question'])
            q.correct_answer = element['correct_answer']
            for ans in element['incorrect_answers']:
                q.incorrect_answers.append(html.unescape(ans))
            self.questions.append(q)

    def ask_current(self):
        result = self.questions[self.current].ask()
        self.current = self.current + 1
        if result:
            self.score = self.score + 1

    def has_more_questions(self):
        return self.current != len(self.questions)

    def print_score(self):
        print("SCORE: " + str(self.score))


# ask user for their name
quiz = Quiz()
quiz.load()
while quiz.has_more_questions():
    quiz.ask_current()
quiz.print_score()
# save user-name and score in file
print("Bye, Thanks for trying")