# List of questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "How many planets are in the solar system? (Enter a number)",
        "answer": "9",
        "answer": "8"
    },
    {
        "question": "Who is one of the founders of Apple?",
        "answer": "Steve Jobs",
        "answer": "Steve Wozniak",
        "answer": "Ronald Wayne"
    }
]
def quiz_user(questions):
    score = 0
    for question in questions:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    return score

