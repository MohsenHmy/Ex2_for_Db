users = {}
count = int(input("Please enter the number of users: "))

while count>= 1:
    user_name = input("Enter users's name: ")
    user_age = input("Enter users's age: ")
    users.update({user_name : user_age})

    count-=1

nameToSearch = input("Enter the name you are looking for: ")
checker = 0

for k,v in users.items():
    if k == nameToSearch:
        print (v)
        checker+=1
    

if checker == 0:
    print('There is no user with given name!')



    