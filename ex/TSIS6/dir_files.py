#1
'''import os

def list_directories_and_files(path):
    directories = []
    files = []
    all_directories_and_files = []

    items = os.listdir(path)

    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
        elif os.path.isfile(item_path):
            files.append(item)
        all_directories_and_files.append(item)

    print("Directories:")
    print(directories)
    print("\nFiles:")
    print(files)
    print("\nAll directories and files:")
    print(all_directories_and_files)

path = input("Enter the path: ")
#path = 'C:/Users/User/Desktop/КБТУ/Master/python/ex/tsis6'
list_directories_and_files(path)'''

#2
'''import os
path = input("Enter the path to check: ")
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))

#path = 'C:/Users/User/Desktop/КБТУ/Master/python/ex/tsis6'
'''
#3
'''import os

def analyze_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")

        filename = os.path.basename(path)
        print(f"Filename: {filename}")

        directory = os.path.dirname(path)
        print(f"Directory: {directory}")

    else:
        print(f"The path '{path}' does not exist.")
path = input("Enter the path to analyze: ")
#path = 'C:/Users/User/Desktop/КБТУ/Master/python/ex/tsis6
analyze_path(path)'''

#4
'''def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"Number of lines in '{filename}': {num_lines}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the file name: (dont forget to add '.txt') ")
#new.txt
count_lines(filename)'''

#5
'''def write(filename, list_data):
    try:
        # Open the file in write mode
        with open(filename, 'w') as file:
            # Write each item in the list to the file
            for item in list_data:
                file.write(str(item) + '\n')
        print(f"List has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = input("Enter the file name: ")
list_data = input("Enter the list items separated by spaces: ").split()

write(filename, list_data)'''
#6
'''import string
def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + '.txt'
        with open(filename, 'w') as file:
            pass  
generate_files()'''
#7 
'''first = input("Enter the path of the first file: ")
second = input("Enter the path of the second file: ")
#first = 'C:/Users/User/Desktop/КБТУ/Master/python/ex/tsis6/new.txt'
#second = 'C:/Users/User/Desktop/КБТУ/Master/python/ex/tsis6/second.txt'
with open(first,'r') as firstfile, open(second,'a') as secondfile: 
    for line in firstfile: 
             secondfile.write(line)'''
#8
'''import os

def delete_file(path):
    try:
        if os.path.exists(path):
            print(f"The path '{path}' exists.")
            if os.access(path, os.W_OK):
                os.remove(path)
                print(f"File '{path}' has been deleted successfully.")
            else:
                print(f"Error: You do not have write access to '{path}'.")
        else:
            print(f"Error: The path '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
path = input("Enter the file path to delete: ")
delete_file(path)'''
