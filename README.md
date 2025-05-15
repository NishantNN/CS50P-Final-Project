# Quick Quiz
#### Video Demo: https://www.youtube.com/watch?v=pqrwyvaWv-Y
This is the final project of CS50's Introduction to programming with Python completed Nishanta Poudel.
This project is a quiz where the user can set different criteria for questions that is to be asked to them. The criteria that are flexible to the user are as follows:
- Number of questions(questions are the natural number multiple of 10 ranging from 10 to 50)
- Category(total 10 different categories)
- Difficulty level(three level of difficulty i.e. easy, medium and hard)

#### Description:
There are total 5 functions, 6 including main, in this project. Each of the functions are explained as follows:

1.get_amount():
- The function get_amount() does not have arguments but has a return type. Within the function, the user is prompted a set of options they can select for total number of questions. They can only select the options 10, 20, 30, 40 and 50. Any other number or any value other than the displayed options will raise a ValueError. This function is wrapped in an infinite While loop which breaks only when correct option is provided and returns the corresponding number as an integer. The ValueError is handled by prompting the user, "Invalid Input!" and continuing the while loop another time. The loop continues until a valid option is selected.

2. get_category():
- The function get_category() does not have arguments but has a return type. Within the function, the user is prompted to select a category from a list of category as follows:
    1. Arts & Literature
    2. Film & TV
    3. Food & Drink
    4. General Knowledge
    5. Geography
    6. History
    7. Music
    8. Science 
    9. Society & Culture
    10. Sports & Literature
Each of these options, starting with their corresponding numbers, are stored in dictionaries where the options displayed to the user are the keys. The values are the very specific words which the api accepts as one of the  parameters. So the function receives the input from user as a number and converts it into it's corresponding index and returns the value of dictionary as string. The function uses infinite while loop which breaks only when the correct option is selected. Any incorrect option rises a ValueError which is handled by prompting the user, "Invalid Input!" along with continuation of the infinite while loop.

3. get_difficulty():
- The function get_difficulty() does not have arguments but has a return type. It has an infinite While loop inside which the user is prompted to input any one option as follows:
    1. easy
    2. medium 
    3. hard
The user has to choose one of the options among the given ones. Incorrect option raises a ValueError which prompts the user, "Invalid Input!" along with the continuation of infinite while loop. Only the correct option will return the corresponding string for difficulty and break the loop.

4. randomize_answers():
- The function randomize_answers() has two arguments and a return type. Ut takes a correct option and three incorrect option which the api returns and stores all the options in a list called answers. The list is than randomly shuffled using the shuffle function of the random module. After that, it returns the list of randomly shuffled answers.

5. check_answer():
- The function check_answer() has three arguments and a return type. It takes the list of all answers, option number of the user selected answer and the correct answer as it's arguments. It then converts the user's selected option number to the index of that answer in the answers list. it then compares the answer with user given answer and returns True for the correct answer and False for the incorrect answer.

6. main():
- The main function firstly prompts the user "QUICK QUIZ". then it stores the amount of questions in the variable amt which is obtained by get_amount() function. After that it uses the print() option to print a new line. The print() function is used to ensure a proper gap between each of the tier of user's selection menu. After that, it stores the category in a variable called category which is obtained by get_category() function. Then another print() function is called. After that, the variable difficulty stores the difficulty from the get_difficulty() function.
- Next, the url of api is stored in a variable called url. The proper parameters as retrieved from the user is stored in the dictionary named params. Then the api is fetched using requests passing the url and parameters as params after which all the information returned by the api is stored in the variable requests.
- After that, a variable called score, initialized to zero, is declared to keep track of and update the score of user. Next, a for loop is declared with range up to the amount of question user chooses for.
- Initially inside the for loop, the question variable stores the first question provided by the api. It then stores the correct and incorrect options provided by api in variables correct_answer and incorrect_answers respectively. The correct answer is a string and incorrect_answers is a list of three other incorrect answers. Then the question is prompted to the user followed by the option numbers from 1 to 4 using randomize_answers() function which is stored in a variable named answers.
- Next, an infinite while loop is declared inside of which the user is prompted to choose an option from 1 to 4. Any option other than the given range of numbers raises a ValueError. The ValueError is handled by prompting the user as "Invalid Input!" along with the continuation of the infinite loop. When the valid input is given, the input is converted to an integer and stored in a variable named user_answer and the loop is exited. 
- Next, a variable named answer_check calls the check_answer() function and stores the corresponding Boolean value returned by the function. If answer _check is True, user is prompted "Correct!" and the score variable is updated by 1. In the else block, the user is prompted "Incorrect!".
- The for loop runs again for the multiple iterations until the total number of questions are asked completely. finally the user is prompted a thanks message along with their score out of total number of questions as total score.

7. Other than the functions is a dictionary called category_dict that stores all the key value pairs of categories used by the get_category() function.





