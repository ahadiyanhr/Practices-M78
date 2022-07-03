# Get the Username and Password from user
Username = input("Enter the Username:> ")
Password = input("Enter the Password:> ")

if Username == "admin":
    if Password == "admin":
        print("Welcome on Admin")
    else:
        print("Wrong")   
else:
    print("Hello", Username)
    
        
        