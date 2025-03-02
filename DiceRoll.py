#DiceRoll.py
#Name:Collin Frederick
#Date:3/2/25
#Assignment:Dice roll

import random

def main():
    rolls = [0] * 13  
    total_rolls = 10000  

    for _ in range(total_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        rolls[roll_sum] += 1  

    print("Sum of Dice | Frequency | Percentage")
    print("--------------------------------------")
    for i in range(2, 13):
        percentage = (rolls[i] / total_rolls) * 100  
        print(f"{i:^12} | {rolls[i]:^9} | {percentage:.2f}%")

if __name__ == '__main__':
    main()