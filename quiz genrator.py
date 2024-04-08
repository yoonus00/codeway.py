import random


funny_quiz_questions = {
    "Why don't scientists trust atoms?": "Because they make up everything!",
    "Why did the scarecrow win an award?": "Because he was outstanding in his field!",
    "What do you call fake spaghetti?": "An impasta!",
    "Why did the tomato turn red?": "Because it saw the salad dressing!",
    "What do you call cheese that isn't yours?": "Nacho cheese!"
}

def display_welcome_message():
    print("Welcome to the Funny Joking Quiz Game!")
    print("Get ready to laugh while you answer some hilarious questions.")
    print("Let's see how many jokes you can crack!")

def present_quiz_questions():
    questions = list(funny_quiz_questions.keys())
    random.shuffle(questions)  # Shuffle questions for randomness

    score = 0
    total_questions = len(questions)

    for question in questions:
        print("\n" + question)
        user_answer = input("Your answer: ").strip().capitalize()

        correct_answer = funny_quiz_questions[question].capitalize()
        if user_answer == correct_answer:
            print("Haha! That's right!")
            score += 1
        else:
            print("Oops! That's not quite it. The correct answer is:", correct_answer)

    return score, total_questions

def display_final_results(score, total_questions):
    print("\nJoking Quiz Complete!")
    print("You got", score, "out of", total_questions, "jokes right.")
    print("Your joke-cracking score is:", score, "/", total_questions)

def play_again():
    choice = input("\nDo you want to crack some more jokes? (yes/no): ").strip().lower()
    return choice == "yes"

def main():
    display_welcome_message()
    while True:
        score, total_questions = present_quiz_questions()
        display_final_results(score, total_questions)
        if not play_again():
            print("Thank you for cracking jokes with us!")
            break

if __name__ == "__main__":
    main()
