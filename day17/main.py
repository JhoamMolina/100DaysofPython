from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def create_question_bank():
    """ Creates a  bank of objects of quetions """
    question_bank = []
    for question in question_data:
        new_question = Question(
            question["question"], question["correct_answer"])
        question_bank.append(new_question)
    return question_bank


def main():

    quiz = QuizBrain(create_question_bank())
    while quiz.still_has_question():
        quiz.next_question()

    print("You have completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


main()
