import random
print('''                                                                              
  _   _                       ___                                             
 | | | |                     / _ \             /\                             
 | |_| |_ _   _ ___  ___    | | | | ___       /  \   ___   __   __  ___  ___  
 |  _  | ( \ / ) __)/ _ \   | | | |/ _ \     / /\ \ / _ \ / / _ \ \/ __)/ _ \ 
 | | | | |\ v /> _)| |_) )  | |_| | |_) )   / /  \ ( (_) ) |_/ \_| > _)| |_) )
 |_| |_|\_)| | \___)  __/    \___/|  __/   /_/    \_\___/ \___^___/\___)  __/ 
           | |     | |            | |                                  | |    
           |_|     |_|            |_|                                  |_|          
''')
count = 0
def test():
    choice = input(' Which is Higer \n A or B \n ')
    print(f" you chose {choice.upper()}")
    global count
    a = random.randint(0, 100)
    b = random.randint(10, 100)
    if a > b and choice.upper() == "A":
        count += 1
        print(" Next ")
        return True
    elif b > a and choice.upper() == "B":
        count += 1
        print(" Next ")
        return True
    else:
        print(" End : Wrong Anser :( ")
        return False

while(True):
    if test() == False:
        break
    else:
        test()
