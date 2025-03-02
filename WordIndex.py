#WordIndex.py
#Name:Collin Frederick
#Date:3/2/25
#Assignment:word index

def main():
    file_name = input("Enter the name of the file to analyze: ")
    try:
        with open(file_name, "r") as textFile:
            words = {}  
            for line_num, line in enumerate(textFile, start=1):
                word_list = line.split()
                for word in word_list:
                    word = word.strip(",.!?;:\"()[]").lower() 
                    
                    if word in words:
                        words[word].add(line_num)  
                    else:
                        words[word] = {line_num}  

            print("\nWord Index Analysis:")
            print("---------------------------------------------------")
            for word, line_numbers in sorted(words.items()):  
                line_str = ", ".join(map(str, sorted(line_numbers)))  
                print(f"{word}: Appears in lines {line_str}")

    except FileNotFoundError:
        print("Error: File not found. Please enter a valid file name.")

if __name__ == '__main__':
    main()