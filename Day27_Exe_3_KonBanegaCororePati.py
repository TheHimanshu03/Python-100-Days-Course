#Q1. Create a program that capable for displays question to the user like crorepati .?
'''
1. Use List Data type to store the question and correct answers.
2. Display the final amount that a person is taking home after playing the game.
'''

questions = [
    ["which language was used to create Facebook ? ", "java" , "python" , "javascript" , "php" , "none" , 4],
    ["which language was used to create Instagram ? ", "java" , "python" , "javascript" , "php" , "none" , 4],
    ["which language was used to create Twitter ? ", "java" , "python" , "javascript" , "php" , "none" , 4],
    ["which language was used to create Trading ? ", "java" , "python" , "javascript" , "php" , "none" , 4],
    ["which language was used to create Dhan ? ", "java" , "python" , "javascript" , "php" , "none" , 4],
    ["which language was used to create Zerodha ? ", "java" , "python" , "javascript" , "php" , "none" , 4],
    ["which language was used to create CoinDCX ? ", "java" , "python" , "javascript" , "php" , "none" , 4],
    ["which language was used to create TradingView ? ", "java" , "python" , "javascript" , "php" , "none" , 4],
    ["which language was used to create FB ? ", "java" , "python" , "javascript" , "php" , "none" , 4],
    ["which language was used to create FB ? ", "java" , "python" , "javascript" , "php" , "none" , 4]
    
    ]

levels = [1000 , 2000 , 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 480000 ]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs: {levels[i]} ")
    #print(questions[i][0])
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")

    reply = int(input("Please enter your answer in between (1-4) or enter (0) to quit the game"))

    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):

        print(f"Congratulations! You have won Rs: {levels[i]} ")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("\nOPPS! wrong Answer")
        break    

print(f" \n\nCongratulations ! You have taken amount of Rs. {money} at home")