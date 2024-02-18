import requests
def get_questions():
    response=requests.get("https://opentdb.com/api.php?amount=3&type=multiple")
    if response.status_code == 200:
        data=response.json()
        return data['results']
    else:
        print("Failed to fetch questions")
        return []

def run_quiz(questions):
    score=0
    for index, question in enumerate(questions, 1):
        print(f"Question {index}: {question['question']}")
        print("Options:")
        options = question['incorrect_answers'] + [question['correct_answer']]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        answer = input("Your answer: ")
        if options[int(answer) - 1] == question['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print(f"You got {score} out of {len(questions)} questions correct.")
    return score


while True:
    questions = get_questions()
    if questions:
        score = run_quiz(questions)
        play_again = input("Do you want to try again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


