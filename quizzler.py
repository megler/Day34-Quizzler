# quizzler.py
#
# Python Bootcamp Day 37 - Quizzler
# Usage:
#      A redo of Day 17 Quiz Game. This utilized tkinter to create a gui layout
# and queries the Open Trivia DB API for dynamic question generation.
#
# Marceia Egler December 6, 2021

from ui import QuizInterface
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
