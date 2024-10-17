with open("text.txt","w") as file:
    # file.write("This is a new file created!")
    file.writelines(["Hello Everyone\n","My name is Aryan\n","I work at MAQ Software\n","I am building a flask application\n"])
try:
    with open("text.txt","r") as file:
        print(file.read())
except FileNotFoundError as e:
    print("File not found",e)
except Exception as e:
    print("Error!",e)