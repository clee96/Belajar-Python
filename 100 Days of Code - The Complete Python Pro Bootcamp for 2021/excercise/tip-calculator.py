#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome Tip Calculator")
bill = int(input("Your Bill is $ ..."))
tip = float(input("How much you want to give us a tip? (%)..."))
split = int(input(
    '''Do you want to split your bill?
    Enter 1 for yes
    Enter 2 for no   '''))

def main(choice):
    if choice == 2:
        total = bill + bill*(tip/100)
        print("you should pay $ ", str(round(total, 2)))
    else:
        pic = int(input("Enter number of person.."))
        total = (bill + bill*(tip/100))/pic
        print("Each person should pay $ ", str(round(total, 2)))
main(split)
