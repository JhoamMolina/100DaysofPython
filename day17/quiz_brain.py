from typing import List
from question_model import Question


def parse_bool(input_str: str) -> bool:
    normalized_str = input_str.strip().lower()
    if normalized_str in ('true', 'yes', '1', "t"):
        return True
    elif normalized_str in ('false', 'no', '0', "f"):
        return False
    else:
        raise ValueError(f"Invalid boolean value: {input_str}")


class QuizBrain():
    def __init__(self, question_list: List[Question]):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):

        amount_of_questions = len(self.question_list)
        return amount_of_questions > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number }: {question.text} (True/False): ").lower()
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer: str, correct_answer: bool):
        parsed_answer = parse_bool(user_answer)
        parsed_correct_answer = parse_bool(correct_answer)

        if parsed_answer == parsed_correct_answer:
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
