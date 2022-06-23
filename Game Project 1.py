from logging import raiseExceptions
from turtle import end_fill

name = input('Enter your name.')
print('Remember to type in LOWERCASE ONLY!!!')
money = 500
health = 10
if health <= 0:
    print("You died")
    exit()
attackpower = 1
print('Welcome ' + name + ' I am the questmaster and I will be the one helping you find your quest.')
print('You have $500, 10 health,and 1 attack power.')
buy = input("Enter armour if you want to buy armour for $200. This will give you +2 health. Enter sword, if you want to buy a sword for $300. This will give +1 more attack power. If you would like to buy nothing press enter.")
if buy == 'armour':
    money = (money - 200)
    health = (health + 2)
    print('You have succesfully bought the armour. Your money is now ' + str(money) + ' and your health is now ' + str(health) + '. Congratulations on making your first purchase!')
if buy == 'sword':
    money = (money - 300)
    attackpower = (attackpower + 1)
    print('You have succesfully bought the sword. Your money is now' + str(money) + ' and your attack power is now ' + str(attackpower) + '. Congratulations on making your first purchase.')
print('Ok! Now that you have your gear, let me explain to you what first quest is.')
print('You will be visitng either the old dungeon in austin, or you could go to the new, allegedly, haunted dungeon just outside Washington D.C. Then you will have to search for the secret jewel, that are rumoured to be hidden in both places.')
print('The one in Austin is bigger and will take more time, but it has less hostile creatures inside. The one in Washington D.C however is the exact opposite and will take less timne to explore but will require more stregnth. Food is easier to find in Washington D.C.')
location = input('Enter austin if you want to visit the dungeon in Austin. Enter washington if you want to choose the dungeon in washington DC.')
if location == 'washington':
    print('You have chosen the haunted dungeon in Washington D.C. You will have to search for the secret jewel in this dungeon.')
    print('The flight will cost you $50, you now have $' + str(money - 50) +'. You enter the dungeon and you see a door that is locked. You will have to find the key to unlock it.')
    key = input('Enter key if you want to find the key. Enter nothing if you do not want to find the key. It will cost you $20 if you want to search for the key.')
    if key == 'key':
        money = (money - 20)
        #randomize if they can find the key
        import random
        random_number = random.randint(1, 10)
        if random_number == 1:
            print('You found the key! You unlock the door and you enter the dungeon.')
            money = (money + 100)
            print('You open the door and you see a chest. You try the same key and it works. There are $100 in the chest. You now have $' + str(money + 100) + '.')
        else:
            print('You did not find the key.')
    print('You continue your search and find a note saying that the jewel is not here in this dungeon, the note says it is outside the dungeon.')
    leave = input('Do you want to listen to the note and search outside the dungeon? Enter yes if you want to search outside the dungeon. Enter no if you do not want to search outside the dungeon. Enter leave if you want to quit the quest altogether.')
    if leave == 'yes':
        print('You have been ambushed by a group of ghosts! You lose 10 health.')
        health = (health - 10)       
        print('You now have ' + str(health) + ' health.')
        #if their health is lower than 0, they lose
        if health <= 0:
            print('You have lost the game.')
            raise SystemExit
        print('After the attack you wake up and you find the secret jewel, congrats.')
        #won the game
        print('You have won the game!')
        print('You have $' + str(money) + ' and ' + str(health) + ' health.')
        print('Thank you for playing!')
    if leave == 'leave':
        #end game
        print('You have left the quest.')
        raise SystemExit
    if leave == 'no':
        print('You have chosen to not search outside the dungeon.')
        health = (health - 1)
        print('You get hungry and lose one health. You now have ' + str(health) + ' health.')
        doory = input('You find a door. Do you want to open it? Enter yes if you want to open it. Enter no if you do not want to open it.')
        if doory == 'yes':
            print('You open the door and you find the secret jewel, congrats.')
            #won the game
            print('You have won the game!')
            print('You have $' + str(money) + ' and ' + str(health) + ' health.')
            print('Thank you for playing!')
            #end game
            raise SystemExit
        if doory == 'no':
            print('You continue on for a while and then hear a voice. The voice gets closer and closer and you look forward. There is nothing there. ')
            print('You got a slight glance at your assasin when you looked back, but you fall down and die.')
            health = 0
            print('You have lost the game.')
#seperate location
if location == 'austin':
    money = (money - 50)
    print('Ok, you take a flight to Austin which costs you $50, you now have $ ' + str(money) + '. You enter the dungeon and find a lamp on the other side, do you want to go and pick that up?')
lamp = input('Enter yes if you want to pick up the lamp, or enter no if you do not want to pick up the lamp.')
if lamp == 'yes':
    print('You have succesfully picked up the lamp.')
if lamp == 'no':
    print('You have not picked up the lamp.')
    health = (health - 1)
    print('You have lost 1 health.')
print('You enter the dungeon and find a chest, do you want to open it? It has a weird lock on it. Do you want to search for the key, it will cost you $50.')
chest = input('Enter yes if you want to search for the key, or enter no if you do not want to search for the key.')
if chest == 'yes':
    import random
    random_number = random.randint(1, 2)
    if random_number == 1:
        print('You have found the key!')
        money = (money + 50) 
        print('You open the chest and find $50 inside! Congratulations!')
        print('You now have $' + str(money) + '.')
    if random_number == 2:
        print('You have not found the key.')
        money = (money - 50)
        print('You have lost $50')
        print('You now have $' + str(money) + '.')
if chest == 'no':
    print('You have chosen to not look for the key.')
print('You are feeling hungry, do you want to search for the food? It will cost you $50.')
food = input('Enter yes if you want to search for the food, or enter no if you do not want to search for the food.')
if food == 'yes':
    print('You have succesfully found the food.')
    money = (money - 50)
    health = (health + 1)
    print('You now have $' + str(money) + 'and your health is now ' + str(health) + '.')
if food == 'no':
    print('You have not eaten the food.')
print('You find a underground tunnel, do you want to go down there? It does not look like it is safe.')
tunnel = input('Enter yes if you want to go down the tunnel, or enter no if you do not want to go down the tunnel.')
if tunnel == 'yes':
    print('You go down the tunnel and find a secret room, do you want to enter it?')
    secret = input('Enter yes if you want to enter the secret room, or enter no if you do not want to enter the secret room.')
    if secret == 'yes':
        print('You have succesfully entered the secret room.')
        money = (money + 50)
        print('You now have $' + str(money) + '.')
        print('You decide to go back to the main dungeon.')
    if secret == 'no':
        print('You have not entered the secret room.')
        print('You decide to go back to the main dungeon.')
if tunnel == 'no': 
    print('You have chosen to not go down the tunnel.') 
    print('You continue on your journey.')
print('You have been searching for the secret jewel for a while, and then you see a green glow. You think it might be the secret jewel, do you want to go there?')
glow = input('Enter yes if you want to go there, or enter no if you do not want to go there.')
if glow == 'yes':
    print('You enter the secret room and find a big green worm that is trying to eat you. It has a health of 10 and an attack power of 1. You have to fight it if you want to live.')
    while health > 0 and health > 0:
        print('You have ' + str(health) + ' health and ' + str(money) + ' money.')
        print('The worm has ' + str(health) + ' health and ' + str(attackpower) + ' attack power.')
        print('What do you want to do?')
        print('1. Attack')
        print('2. Run')
        print('3. Heal')
        print('4. Quit')
        choice = input('Enter 1, 2, 3, or 4.')
        if choice == '1':
            health = (health - attackpower)
            print('You have attacked the worm and it has ' + str(health) + ' health.')
            if health <= 0:
                print('You have killed the worm.')
                money = (money + 100)
                print('You now have $' + str(money) + '.')
                print('The worm gets cut in half and you find the secret jewel.')
                print('You have won the game!')
                break
        if choice == '2':
            print('You have chosen to run.')
            print('You have lost 1 health.')
            health = (health - 1)
            if health <= 0:
                print('You have died.')
                print('You have lost the game.')
                break
        if choice == '3':
            print('You have chosen to heal.')
            health = (health + 1)
            print('You now have ' + str(health) + ' health.')
        if choice == '4':
            print('You have chosen to quit.')
            print('You have lost the game.')
            break
    if health <= 0:
        print('You have died.')
        print('You have lost the game.')
if glow == 'no':
    print('You have chosen to not go there.')
    print('You continue on your journey.')
    print('You continue for a while and you find an empty room, do you want to enter it?')
    empty = input('Enter yes if you want to enter the empty room, or enter no if you do not want to enter the empty room.')
    if empty == 'yes':
        print('You have succesfully entered the empty room.')
        print('You see the secret jewel lying right in front of you and you pick it up.')
        print('You are on your way back when you get hungry but decide to continue on your journey.')
        print('You clutch the secret jewel in your hands and keep on walking until you feel dizzy all of a sudden and fall down to your death.')
        print('It turns out that the jewel you were holding was a cursed jewel and it caused your death.')
        print('You have lost the game.')
        health = 0
        money = 0
        raiseExceptions ('Health is 0.')
    if empty == 'no':
        print('You have chosen not to enter the room and you start to get lost.')
        print('Eventually you run out of breath and you close your eyes and fall to your death.')
        health = 0
        print('You have lost the game.')
        raiseExceptions ('Health is 0.')
