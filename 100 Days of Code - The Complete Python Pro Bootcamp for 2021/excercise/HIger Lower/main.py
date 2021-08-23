from game_data import *
from art import *
import random

length_data = len(data) - 1 # sum of total data can use
count = 0 #user scor
print(logo)
def main(compare1, compare2, data):
    global vs
    global count
    print(data[compare1]['name'])
    print(vs)
    print(data[compare2]['name'])
    choice = input("enter your answer \n")
    if data[compare1]['follower_count'] > data[compare2]['follower_count'] and choice.lower() == data[compare1]['name'].lower():
        count += 1
        print("Next")
        return True
    elif data[compare2]['follower_count'] > data[compare1]['follower_count'] and choice.lower() == data[compare2]['name'].lower():
        count += 1
        print("Next")
        return True
    else:
        return False
    

while(True):
    a = random.randint(0, length_data)  # get random data to compare
    b = random.randint(0, length_data)
    if a == b:
        a == random.randint(0, length_data)
    test = main(a, b, data)
    if test == False:
        print('Game O')
        print("Your Score Is", count)
        break
    else:
        test

