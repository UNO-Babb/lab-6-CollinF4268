#WordCount.py
#Name:Collin Frederick
#Date:3/2/25
#Assignment: word count

def main():
    file_name = input("Enter the name of the file to analyze: ")
    try:
        with open(file_name, 'r') as textFile:
            lines = textFile.readlines()  
            
            num_lines = len(lines)  # Count lines
            num_words = sum(len(line.split()) for line in lines)  # Count words
            num_chars = sum(len(line) for line in lines)  
            print("\nFile Analysis:")
            print("----------------------------")
            print(f"Total Lines    : {num_lines}")
            print(f"Total Words    : {num_words}")
            print(f"Total Characters: {num_chars}")

    except FileNotFoundError:
        print("Error: File not found. Please enter a valid file name.")

if __name__ == '__main__':
    main()
