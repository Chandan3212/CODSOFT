import requests
from bs4 import BeautifulSoup
import random

def get_trivia_questions():
    url = 'https://opentdb.com/api.php?amount=5&type=multiple'  # Adjust the amount as needed
    response = requests.get(url)
    data = response.json()
    return data['results']

def display_question(question):
    print(question['question'])
    options = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(options)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    user_answer = input("Your answer: ")
    return str(user_answer)

def check_answer(question, user_answer):
    if user_answer == question['correct_answer']:
        print("Correct!")
        return 1
    else:
        print(f"Wrong! The correct answer is {question['correct_answer']}.")
        return 0
questions = get_trivia_questions()
score = 0
for question in questions:
    user_answer = display_question(question)
    score += check_answer(question, user_answer)

print(f"Quiz completed! Your final score is {score}/{len(questions)}.")
