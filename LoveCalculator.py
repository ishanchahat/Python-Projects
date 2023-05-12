while True:
    print("Welcome to my Love Calculator")
    name1 = input("Enter your name: ")
    name2 = input("Enter his/her name: ")

    combined_string = name1+name2
    lower_case_string = combined_string.lower()

    t = lower_case_string.count("t")
    r = lower_case_string.count("r")
    u = lower_case_string.count("u")
    e = lower_case_string.count("e")
    
    true = t+r+u+e

    l = lower_case_string.count("l")
    o = lower_case_string.count("o")
    v = lower_case_string.count("v")
    e = lower_case_string.count("e")

    love = l+o+v

    love_score = int(str(true) + str(love))

    if(love_score < 10):    
        print(f"your love score is {love_score}, Nothing good happens after 2A.M.")
    elif(love_score > 90):  
        print(f"your love score is {love_score}, You are meant for destiny")
    elif(love_score > 40 and love_score <= 50): 
        print(f"your love score is {love_score}, You are alright together")
    else:
        print(f"your love score is {love_score}")
        
    choice = input("Do you want to continue: y/n ")
    if choice.lower == 'n':
        break