import random

count = 0
game_count = 0
names = {1:"Камень", 2:"Бумага", 3:"Ножницы"}

while True:
    gg = random.randint(1, 3)
    you = input("выбери:1 (Камень) или 2 (Бумага) или 3 (Ножницы)")
    if you ==  "конец":
        break
    you =int(you)
    print("Компьюетер:", names[gg])
    if you == str(gg) :
        print("Ничья")
    elif (you == 1 and gg == 3) or (you == 2 and gg == 1) or (you == 3 and gg == 2):
        print("YOU WIN")
        count += 1
    else:
        print("YOU LOSE")
        game_count += 1


print("счетчик", count,"/",game_count )


