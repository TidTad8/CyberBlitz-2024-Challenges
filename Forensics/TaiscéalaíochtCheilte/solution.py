import os
import base64

# Set the base directory relative to the current working directory
base_directory = "Bridget The Seeker"

# Function to search for bratach.txt file and read its content
def find_bandera(directory):
    flag_count = 0  # Initialize the flag count
    for root, dirs, files in os.walk(directory):
        if "bratach.txt" in files:
            flag_count += 1
            file_path = os.path.join(root, "bratach.txt")
            with open(file_path, "r") as file:
                encoded_flag = file.read().strip()
                # Decode the Base64 flag
                try:
                    flag = base64.b64decode(encoded_flag).decode()
                    print(f"Flag found at: {file_path}")
                    print("Flag Content:")
                    print(flag)
                except Exception as e:
                    print(f"Error decoding flag at {file_path}: {e}")
                print("-" * 30)
    return flag_count

# Main function to find and print the flag count
def main():
    flag_count = find_bandera(base_directory)
    if flag_count > 0:
        print(f"Total number of 'bratach.txt' files found: {flag_count}")
    else:
        print("Oops! No 'bratach.txt' files found")

if __name__ == "__main__":
    main()
