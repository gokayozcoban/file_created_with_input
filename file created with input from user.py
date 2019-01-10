
file_name = input("Enter the file name you want to create: ")
file = open("file_name.txt","w")
print("File is ready!")

name = input("What is your name: ")
age  = input("How old are you: ")
text = input("Write someting about you: ")

file.write("Name:  = {}\n".format(name))
file.write("Age: {}\n".format(age))
file.write("I AM: {}\n".format(text))

print("File write operation completed!")
file.close()
