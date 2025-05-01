# Task 1: Read a File and handle errors.

try:
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")
            #print("Line " + str(line_number) + ": " + line.strip())  
except FileNotFoundError:
    print("Error: The file sample.txt was not found.")