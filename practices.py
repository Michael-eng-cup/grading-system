name = input("name")
score = int(input("Enter score"))
if score >= 70 and score <= 100:
    message = f"{name}, Your score is {score}, you get an A"
elif score >= 60 and score < 70 :
    message =f"{name},Your score is {score}, you get a B"  
elif score >=50 and score <60:
    message =f"{name},Your score is {score}, you get a C"
elif score >= 40 and score <50:
    message =f"{name},Your score is {score}, you get a D"
elif score >= 30 and score < 40:
    message =f"{name},Your score is {score}, you get an E"
elif score >=0 and score< 30:
    message=f"{name},Your score is {score}, you get an F"       
else:
    massage = f"{name},Your score is {score}, you get an invalid score"   

print(message)              



# user = input("name")
# if len(user) > 5:
#     if user.isalpha():
#         print("name is vaild")
#     else:
#         print("name invalid")
# else:
#     print("name is less than 5")    
    

# user = input("name")
# if len(user) > 5 and user.isalpha():
#     print("name is vaild")
# else:
# #     print("name is less than 5")  


# user =input("user name")
# if user.isalpha():
#     password = int(input("Enter your password"))
#     if len(password) > 4:
#         print("Welcome user")
#     else:
#         print("Password must be greater than 4")    
# else:
#     print("user name is not valid")    
    


# friends = ["michael", "jayne", "favour", "stephanie", "rapheal", "50"]# list
# followers = ("michael", "jayne", "favour", "stephanie", "rapheal")# tuple
# name = friends.index("jayne")
# print(name)

# converted_tuple = tuple(friends)
# converted_followers = list(followers)

# print(dir(followers))
# print(type(friends))
# print(type(followers))



# assignment 1

# age_grade = int(input(" Enter your age: "))
# if age_grade >= 18:
#     print("You are eligible to vote")
# else:
#     print("Your are not eligible vote")    

# # assignment 2

# values = ("bcc2025")
# user = input("Please enter your password: ")
# if values == user:
#     print("Access Granted")
# else:
#     print("Access Denied!")    

#  # assignment 3
# user = int(input("Enter number: "))
# if user % 2 == 0 :
#     message =(f" The number {user} is an even number ")
# else:
#     message=(f" The number {user} is an odd number ")   
# print(message)     



friends = ["michael", "jayne", "favour", "stephanie", "rapheal", "50"]
name = friends.insert("marry[0]")
print(name)