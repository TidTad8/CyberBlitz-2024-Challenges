import os
import random
import string
import nltk
from nltk.corpus import words

# Set the base directory for the challenge
base_directory = "TaiscéalaíochtCheilte_Updated"

# Set the number of levels, folders, and files you want in the challenge
num_levels = 5  # Increased to 5 levels
num_folders_per_level = 3
num_files_per_folder = 5

# Initialize the nltk words corpus
nltk.download('words')
word_list = words.words()

# Function to generate a random word
def generate_random_word():
    return random.choice(word_list)

# Function to generate a random string of given length
def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to create directories recursively based on the number of levels
def create_directories(path, levels, folders_per_level, files_per_folder):
    if levels == 0:
        return
    
    for folder_num in range(1, folders_per_level + 1):
        folder_name = generate_random_string(10)  # Generate a random folder name
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path)
        
        for file_num in range(1, files_per_folder + 1):
            file_name = f"{generate_random_word()}.txt"  # Generate a random word as file name
            file_content = generate_random_string(50)
            file_path = os.path.join(folder_path, file_name)
            
            with open(file_path, "w") as file:
                file.write(file_content)
        
        create_directories(folder_path, levels - 1, folders_per_level, files_per_folder)

# Create the base directory if it doesn't exist
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# Generate directories recursively
create_directories(base_directory, num_levels, num_folders_per_level, num_files_per_folder)

# Randomly place the flag file in one of the innermost levels
innermost_levels = []
for root, dirs, files in os.walk(base_directory):
    if len(dirs) == 0:  # Check if it's an innermost level
        innermost_levels.append(root)

if innermost_levels:
    random_innermost_level = random.choice(innermost_levels)
    with open(os.path.join(random_innermost_level, "bratach.txt"), "w") as flag_file:
        flag_file.write("CyberBlitz{Myster10usM00nWalks!_Suiii}")
        print(f"Flag placed at: {os.path.join(random_innermost_level, 'bratach.txt')}")
else:
    print("No innermost levels found. Flag not placed.")
