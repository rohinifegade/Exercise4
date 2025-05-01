user_input=input("Enter text to write to the file:")
with open('output.txt','w') as file:
    file.write(user_input)
    print("data successfully written to output.txt") 

user_append=input("Enter additional text to append:")
with open('output.txt','a') as file:
    file.write('\n' +user_append)
    print("data successfully appended")

with open('output.txt','r') as file:
    print("Final content of output.txt:")
    for line in file:
        print(line.strip())


    