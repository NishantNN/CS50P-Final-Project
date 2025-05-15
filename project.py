import requests
import random
def main():
    print("QUICK QUIZ.")
    amt=get_amount()
    print()
    category=get_category()
    print()
    difficulty=get_difficulty()
    print()
    # fetching url and extracting questions
    url="https://the-trivia-api.com/api/questions"
    params = {
    "limit": amt,                         
    "difficulty": difficulty,             
    "categories": category    
}
    response=requests.get(url, params=params)
    score =0
    for i in range(amt):
        question = response.json()[i]['question']
        correct_answer=response.json()[i]['correctAnswer']
        incorrect_answers=response.json()[i]['incorrectAnswers']
        print(question)
        answers = randomize_answers(correct_answer,incorrect_answers)
        print(f"1.{answers[0]} \n 2.{answers[1]} \n 3.{answers[2]} \n 4.{answers[3]}")
        while True:
            try:
                user_answer = int(input("Choose an option: "))
                if 1>user_answer<4:
                    raise ValueError
                else:
                    break
            except (ValueError):
                print("Invalid Input!")
                continue
        ans_check=check_answer(answers,user_answer,correct_answer)
        if ans_check:
            print("Correct!")
            score+=1
        else:
            print("Incorrect!")
    print("Thanks for playing! your score is",score,"out of",amt)


category_dict = {
    "1 Arts & Literature": "arts_and_literature",
    "2 Film & TV": "film_and_tv",
    "3 Food & Drink": "food_and_drink",
    "4 General Knowledge": "general_knowledge",
    "5 Geography": "geography",
    "6 History": "history",
    "7 Music": "music",
    "8 Science": "science",
    "9 Society & Culture": "society_and_culture",
    "10 Sport & Leisure": "sport_and_leisure"
}


# Function to get amount
def get_amount():
    print("1. Choose the number of questions:")
    print("10")
    print("20")
    print("30")
    print("40")
    print("50")
    while True:
        try:
            amt=int(input("Total-questions:"))
            if amt==10:
                return 10
            elif amt==20:
                return 20
            elif amt==30:
                return 30
            elif amt==40:
                return 40
            elif amt==50:
                return 50
            else:
                raise ValueError
        except (ValueError):
            print("Invalid Input!")
            continue


# Function to get category
def get_category():
    print("2. Choose a Category Number:")
    for category in category_dict:
        print(category)
    while True:
        try:
            category_num=int(input("Category-Number: "))
            if 1<=category_num<=10:
                key_list=list(category_dict.keys())
                return category_dict[key_list[category_num-1]]
            else:
                raise ValueError
        except (ValueError):
            print("Invalid Input!")
            continue


# Function to get difficulty
def get_difficulty():
    print("3. Choose a Difficulty Number:")
    print("1 for easy")
    print("2 for medium")
    print("3 for hard")
    
    while True:
        try:
            categ_num=int(input("Difficulty: "))
            if categ_num ==1:
                return f"easy"
            elif categ_num ==2:
                return f"medium"
            elif categ_num ==3:
                return f"hard"
            else:
                raise ValueError
        except (ValueError):
            print("Invalid Input!")
            continue


# function to randomize options
def randomize_answers(c,inc):
    answers=[]
    for opt in inc:
        answers.append(opt)
    answers.append(c)
    random.shuffle(answers)
    return answers


# function to compare and check for correct answer
def check_answer(ans,usr,c):
    if ans[usr-1]==c:
        return True
    else:
        return False
if __name__=="__main__":
    main()