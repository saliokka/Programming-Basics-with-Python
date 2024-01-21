username = input()
password = input()
login_info = input()

while login_info != password:
    login_info = input()
print("Welcome", username + "!")
