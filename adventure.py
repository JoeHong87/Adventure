
#Village of Hommlet

inventory = ["Backpack"]
items = []
gold = 100

class Item:
    def __init__(self,name,location,cost):
        self.name = name
        self.location = location
        self.cost = cost

def print_word_with_a(name):
    if name[0] == 'a' or name[0] == 'e' or name[0] == 'i' or name[0]=='o' or name[0] == 'u':
        return "an "+name
    else:
        return "a "+name


def print_items(desc_str,location):
    global items
    items_in_location = []
    number_of_items = 0
    print_str = ""
    for item in items:
        if ( item.location == location ):
            items_in_location.append(item)
            number_of_items = number_of_items + 1
    if number_of_items == 1:
        item = items_in_location[0]
        print_str = desc_str + " is " + print_word_with_a(item.name)
    elif number_of_items == 2:
        item0 = items_in_location[0]
        item1 = items_in_location[1]
        print_str = desc_str + " are " + print_word_with_a(item0.name) + " and " + print_word_with_a(item1.name)
    elif number_of_items > 2:
        print_str =  "Lots of items"
        build_str = ""
        for i in range(number_of_items-1):
            build_str = build_str + print_word_with_a(items_in_location[i].name) + ", " 
        build_str = build_str + " and " + print_word_with_a(items_in_location[number_of_items-1].name)
        print_str = desc_str + " are " + build_str
    print print_str

def print_desc(location_desc,ground_desc,location):
    print location_desc
    print_items(ground_desc,location)    

def print_inventory():
    print "Inventory:"
    print "Gold: %d" % gold
    for item in items:
        if ( item.location == -1 ):
            print item.name
    print

def in_inventory(name):
    for item in items:
        if ( item.location == -1 ) and ( name == item.name ):
            return True
    return False


def get_input(location):
    tmp_string = raw_input("> ")
    if "inventory" in tmp_string or "Inventory" in tmp_string:
        print_inventory()
    if "quit" in tmp_string or "Quit" in tmp_string:
        print "Goodbye!"
        exit()
    if "get" in tmp_string or "Get" in tmp_string or "take" in tmp_string or "Take" in tmp_string:
        split_str = tmp_string.split(' ')
        print "Inside get"
        for item in items:
            if split_str[1] == item.name and item.location != -2:
                item.location = -1
                print "You got "+ print_word_with_a(item.name)
#            elif :
#                print "You need to buy "+print_word_with_a(item.name)
    if "drop" in tmp_string or "Drop" in tmp_string:
        split_str = tmp_string.split(' ')
        for item in items:
            if split_str[1] == item.name:
                item.location = location
                print "You dropped " +  print_word_with_a(item.name)

    return tmp_string

#1
def start():
    while True:
        print_desc( "You are on a road.  Ahead is a small village.  On the right is a farm.  Do you go down the road or go to the farm on the right?"
            ,"On the ground ",1)
        next = get_input(1)
        if "right" in next or "farm" in next:
            return 9
        elif next == "ahead":
            return 2

#2
def road1():
    while True:
        print_desc( "You are in a village.  On left is an inn.  On the right is a church.  Further ahead is more road.  Back is more road.",
            "On the ground",2)
        next = get_input(2)
        if "ahead" in next:
            return 3
        if "right" in next or "church" in next:
            return 8
        if "left" in next or "inn" in next:
            return 7
        if "back" in next:
            return 1

#3
def road2():
    while True:
        print_desc( "You are on a road.  Further ahead is more road.  Back is the village.  On the right is a general store.",
            "On the ground ",3)
        next = get_input(3)
        if "ahead" in next:
            return 4
        if "Back" in next or "back" in next or "village" in next:
            return 2
        if "right" in next or "Right" in next or "store" in next:
            return 10

#4
def road3():
    while True:
        print_desc( "You are still on a road.  Further ahead is more road.  Back is more road. ",
            "On the ground ",4)
        next = get_input(4)
        if "ahead" in next:
            return 5
        if "Back" in next or "back" in next:
            return 3

#5
def road4():
    while True:
        print_desc( "You are on a road.  Further ahead is more road.  Back is more road.  Up ahead you see something on the left side of the road.",
            "On the ground", 5)
        next = get_input(5)
        if "ahead" in next:
            return 6
        if "Back" in next or "back" in next:
            return 4

#6
def road5():
    while True:
        print_desc( "You are on a road.  On the left is a hill with an entrance.  Back is more road",
            "On the ground",6)
        next = get_input(6)
        if "left" in next or "hill" in next or "entrance" in next:
            return 11
        if "Back" in next or "back" in next:
            return 5

#7
def inn():
    while True:
        print_str =  """You are inside an inn.  The innkeeper comes up and asks what would you like to drink some ale.
Also inside the inn are some farmers and some mercenaries."""
        print_desc(print_str,"On the ground",7)
        next = get_input(7)
        if "Leave" in next or "leave" in next or "exit" in next:
            return 2

#8
def church():
    while True:
        print_str =  """You are inside a small church.
There is an altar at which you can pray.
There is an exit behind you from which you can leave"""
        print_desc(print_str,"On the floor",8)
        next = get_input(8)
        if "Leave" in next or "leave" in next or "exit" in next:
            return 2

#9
def farm():
    while True:
        print_str = """You are at the farm.  There are children playing in the field nearby.
Inside the farm house, comes the smell of cooking. 
Do you enter the farm house or exit back to the road?"""
        print_desc(print_str, "On the ground",9)
        next = get_input(9)
        if "Leave" in next or "leave" in next or "exit" in next or "back" in next:
            return 1
        if "inside" in next or "Inside" in next or "enter" in next or "Enter" in next:
            return 16

#10
def store():
    global gold
    while True:
        print "You are inside the store.  Items for sale include:"
        for item in items:
            if ( item.location == -2 ):
                print item.name + " ("+ str(item.cost) +" gold)"
        print_items("On the ground ",10)
        next = get_input(10)
        if "Leave" in next or "leave" in next or "exit" in next or "back" in next:
            return 3
        if ("Buy" in next or "buy" in next):
            buy_flag = False
            for item in items:
                if (item.name in next) and (item.location==-2) and (gold >= item.cost):
                    print "You buy " + print_word_with_a(item.name)
                    gold -= item.cost
                    item.location = -1
                    buy_flag = True
            if buy_flag == False:
                print "You don't have enough money"
        if ("Sell" in next or "sell" in next):
            for item in items:
                if (item.name in next) and (item.location==-1):
                    print "You sell " + print_word_with_a(item.name)
                    gold += item.cost
                    item.location = -2



#11
def entrance():
    while True:
        if in_inventory("lantern"):
            print_str = """You are inside the entrance to a dungeon.  You see a door to the right, a door to the left, and a door ahead.
You can also exit back out of the dungeon"""
            print_desc(print_str,"On the ground",11)
        else:
            print "You are inside a dank and dark dungeon."
        next = get_input(11)
        if "Leave" in next or "leave" in next or "exit" in next:
            return 6
        if "right" in next or "Right" in next:
            return 12
        if "left" in next or "Left" in next:
            return 13
        if "ahead" in next or "Ahead" in next:
            return 14

#12
def room1():
    while True:
        if in_inventory("lantern"):
            print_desc("You are in a crystalline room.  The walls reflect the light from your lantern","On the ground ",12)
        else:
            print "You are in a dark room"
        next = get_input(12)
        if "back" in next:
            return 11
#13
def room2():
    while True:
        if in_inventory("lantern"):
            print_desc("You are in a massive cavern.  The bats above you are disturbed by your light","On the ground ",13)
        else:
            print "You are in a dark room"
        next = get_input(13)
        if "back" in next:
            return 11

#14
def room3():
    while True:
        print_desc("You are in a passageway.  Up ahead you see some sort of fire and light, and you hear heavy breathing.  Behind you is an exit","On the ground ",14)
        next = get_input(14)
        if "back" in next or "exit" in next or "behind" in next:
            return 11
        if "ahead" in next:
            return 15

#15
def lastroom():
    while True:
        print_str = "You enter a treasure room.  On top of a heap of gold, gems, jewelry, and other treasure sits a dragon."
        if in_inventory("sword") and in_inventory("armor") and in_inventory("shield"):
            print "The dragon breathes fire upon you which you deflect with the shield."
            print "It then tries to rake you with its claws, but your armor deflects the claws."
            print "You swing at the dragon with your sword and you kill it!"
            print "Congratulations!  You have won the game."
            exit()
        elif in_inventory("sword") and not in_inventory("shield") and not in_inventory("armor"):
            print "You try swinging your sword at the dragon.  Although you manage to wound it.  It breathes fire upon you."
            print "You die.  Perhaps if you had some protection you might have survived"
            exit()
        elif in_inventory("shield") and in_inventory("armor") and not in_inventory("sword"):
            print "You stand in front of the dragon.  It breathes fire upon you which you shield deflects."
            print "It then claws at you which your armor protects you from momentarily."
            print "Unfortunately you have no weapon to kill the dragon."
            print "The dragon takes its mightly body and drops it on top of you."
            print "You are dead.  Perhaps if you had a weapon you would be alive."
            exit()
        else:
            print "The dragon kills you.  Perhaps if you had a weapon and better protection you would be alive."
            exit()



#16
def insidefarm():
    while True:
        print_desc("You are inside a farmhouse.  The farmer's wife is cooking","On the ground ",16)
        next = get_input(16)
        if "back" in next or "exit" in next or "behind" in next:
            return 9





current_location = 1
chicken = Item("chicken",9,10)
items.append(chicken)
pig = Item("pig",9,20)
items.append(pig)
items.append(Item("cow",9,28))
holy_symbol = Item("holy symbol",8,200)
items.append(holy_symbol)
dog = Item("dog",8,30)
items.append(dog)

sword = Item("sword",-2,80)
items.append(sword)
lantern = Item("lantern",-2,25)
items.append(lantern)
waterbag = Item("waterbag",-2,10)
items.append(waterbag)
items.append(Item("armor",-2,110))
items.append(Item("shield",-2,30))

items.append(Item("gem",12,200))


#print items
#for item in items:
#    print item.name

while True:
    if current_location == 1:
        current_location = start()
    elif current_location == 2:
        current_location = road1()
    elif current_location == 3:
        current_location = road2()
    elif current_location == 4:
        current_location = road3()
    elif current_location == 5:
        current_location = road4()
    elif current_location == 6:
        current_location = road5()
    elif current_location == 7:
        current_location = inn()
    elif current_location == 8:
        current_location = church()
    elif current_location == 9:
        current_location = farm()
    elif current_location == 10:
        current_location = store()
    elif current_location == 11:
        current_location = entrance()
    elif current_location == 12:
        current_location = room1()
    elif current_location == 13:
        current_location = room2()
    elif current_location == 14:
        current_location = room3()
    elif current_location == 15:
        current_location = lastroom()
    elif current_location == 16:
        current_location = insidefarm()



