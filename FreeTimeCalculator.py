import json 

def load_data():
    with open('data.json') as UserData:
        data = json.load(UserData)
        return data
def UserData():
    User_data = {
            "Name": [],
            "LastName": 
            }

    User_data["Name"]= input("Please, type your name."))
    User_data["LastName"]=int(input("Please, type your last name."))
    User_data["Age"]=int(input("Please, insert your name."))
    User_data["Occupation"]=int(input("What is your occupation?"))
    User_data["FreeTime"]=int(input("What you think,do you have a lack of free time?"))
    return User_data
 
    
def Unavailable_Time:
    Unavailable_Time = {



            }
    Unavailable_Time["Amount_of_Sleep"]=float(input("How many hours a day do you sleep?"))
    Unavailable_Time["Time_Spent_on_Hobbies"]=float(input("How many hours a day do you usually spend on your hobbies?" /)
    Unavailable_Time["Time_Spent_on_Work"]=float(input("How many hours a day do you usually spend on your work?" /)hobbies))
    Unavailable_Time["Time_Spent_on_Homework"]=float(input("How many hours a day do you usually spend on your homework?" /)work))
    Unavailable_Time["Time_Spent_on_Meals"]=float(input("How many hours a day you usually spend on your meals?" /)homework))
    Unavailable_Time["Suggestions"]=int(input("Your suggestions on what you spend your time."))
    Unavailable_Time["Time_Spent_on_Suggestions"]=float(input("How many overall hours a day do you spend on your suggested activities?" /)meals))
    return Unavailable_Time

def save_to_json():
    x = open("data.json")
    to_json = json.dumps(x)

def Free_Time_Calc(Unavailable_Time):
    sleep = Unavailable_Time["Amount_of_Sleep"] #24 - Unavailable_Time["Amount_of_Sleep"]
    )hobby = remainder_sleep - Unavailable_Time["Time_Spent_on_Hobbies"]
    )work = remainder_hobbies - Unavailable_Time["Time_Spent_on_Work"]
    )homework = remainder_work - Unavailable_Time["Time_Spent_on_Homework"]
    )meals = remainder_homework - Unavailable_Time["Time_Spent_on_Meals"]
    your_free_time = )meals - Unavailable_Time["Time_Spent_on_Suggestions"]

