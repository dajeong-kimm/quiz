# quiz.py
import random
from quiz_data import QuizData

class Quiz:
    def __init__(self):
        self.quiz_data = QuizData()
        self.quiz_dict = self.quiz_data.get_quiz_dict()

    def start_quiz(self):
        count = 1
        while self.quiz_dict:
            len_dict = len(self.quiz_dict)
            r_num = random.randrange(len_dict)
            problem_list = list(self.quiz_dict.items())
            print(f"#{count}")
            question, answer = problem_list[r_num][0], problem_list[r_num][1]
            print(question)
            user_answer = input("정답입력: ")
            print(answer)
            if user_answer.lower() == answer.lower():
                print("정답!")
                problem_list.pop(r_num)
            else:
                print("오답!")
            print("------------------------------------")
            count += 1

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
