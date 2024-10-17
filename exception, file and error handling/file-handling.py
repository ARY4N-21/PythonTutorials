# file = open("file.txt", "r")
# content = file.read()  # Reads the whole file
# print(content)
# file.close()  # Always close the file after use

# # Read file line by line
# file = open("file.txt", "r")
# for line in file:
#     print(line.strip())  # Print each line
# file.close()

# Writing in a file (overwrite)
# file = open("file.txt", "w")  # Open file in write mode
# file.write("Hello, World!\n")  # Writing text to the file
# file.write("Writing another line.\n")
# file.close()  # Close the file

# file = open("file.txt", "a")  # Open file in append mode
# file.write("This is an appended line.\n")
# file.close()  # Close the file


# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)
# # No need to manually close the file


# file = open("file.txt","r")
# print(file.read())
# file.close()