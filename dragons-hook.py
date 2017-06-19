from sys import exit
from sys import argv
from os.path import exists

# This enables me to use the `name` variable throughout the script
# inv = open("ex36_game_txt.txt", 'w')

name = raw_input("What is your name, brave adventurer? > ")

print "Welcome to Dragon's Hook, %s." % name

def portal():
    print "The large, stone circle bursts to life and, through the ripples in the centre of the circle, you see your home. It is a doorway, will you step through it?"

    portal_choice = raw_input("Yes or no? > ")

    if portal_choice == "yes":
        print "You step through the rippling gate and find yourself back home. The sun is shining and the air is cool."
        print "You have come to the end of your journey. Congratulations %s." % name
    elif portal_choice == "no":
        print "The portal fades and closes after a few minutes and you find yourself in darkness. You step out the room into the passage outside and the door swings closed behind you."
        return end()

def exit():
    print "You step through the door and into the early morning light. The next chapter of your adventure lies ahead of you."

def died():
    print "Your short quest has come to an end, along with your life, %s. Perhaps you will have more success in the next life." % name

def end():
    print "You have reached the end of the passage and you are faced with three options: A door to your 'left', another to your 'right' and the 'exit' behind you."
    print "Make your choice. Do you want to take the 'left' door, the 'right' door or 'exit' the dungeon?"

    end_choice = raw_input("> ")

    if end_choice == "left":
        return room5()
    elif end_choice == "right":
        return room6()
    elif end_choice == "exit":
        return run_away()
    else:
        print "Surely you have learned to make a decision by now, %s?" % name
        return end()

def room6():
    print "You step into the room. There is a window with bars on the opposite wall."
    print "On the wall to your left, you see a heavy, reinforced door. The sunlight shines underneath it."
    print "There is nothing else in the room. What do you want to do now?"

    room6_choice = raw_input("Will you 'open' the door or 'exit' the room? > ")

    if room6_choice == "open":
        return exit()
    elif room6_choice == "exit":
        return end()
    else:
        print "You're not good at making decisions, are you %s? Why don't you just leave the room and hope that your ability to make decisions returns next time?" % name
        return room6()

def room5():
    print "As you step into this room, you notice that the door seems different. Unlike the other doors that are worn down, breaking, this door is like new."
    print "As you step into the room, you see an iron lever in the ground. When you step up to it, you see that you can move the lever one position."
    print "On the wall to your right, there is a large stone circle the height of a large human."

    lever_choice = raw_input("What do you want to do? 'Move' the lever or 'leave' the room?")

    if lever_choice == "move":
        return portal()
    elif lever_choice == "leave":
        print "Perhaps wisely, you ignore the temptation and step out of the room."
        return end()

def room3():
    print "You step into the room. The door slams shut behind you and locks. You look around the room and, as you do, a strange creature steps out of the shadows."
    print "The creature looks at you, its eyes glow and you hear a voice in your head: 'Answer my riddle, %s, and you may go free. If you fail, your pitiful mind will be mine forever ...'" % name
    print "You are enthralled by the strange creature. Once again, it speaks ... 'If there are 4 apples before you and and you take away 3, how many apples do you have?'"

    room3_choice = raw_input("What is your answer? > ")

    if room3_choice == "3":
        print "The creature withdraws back into the shadows ... 'You may leave ... never return!'"
        print "You step out of the room and the door slams shut and locks."
        return middle()
    else:
        print "Incorrect answer! If you take away 3 apples, you have 3 apples!"
        print "The creature's eyes burn into your soul and a terrible voice says, 'You have failed. Your fragile mind is mine forever ...'"
        return died()


def room4():
    print "As you open the door to this room, you see a small fire in the centre of the room. There are two goblins sitting around it with their backs to you."
    print "You also notice a short sword against the wall next to the door."
    print "Just as you look up, you notice that one of the goblins has seen you and is drawing his sword to attack."
    print "You have three choices: 1. You can `rush` them and try beat them in the confusion. 2. You can grab the `sword` and attack them, losing the element of surprise. 3. You can close the door and `leave`."

    room4_choice = raw_input("What do you do? > ")

    if room4_choice == "rush":
        print "It probably seemed like a good idea but you're no match for two armed goblins. They cut you down and have adventurer kebabs for dinner."
    elif room4_choice == "sword":
        print "You lift the short sword and attack. They get a few slices in but you defeat them, killing both goblins."
        print "Alas, it was all for naught, there is no more treasure here. You do have a sword though."
    elif room4_choice == "leave":
        print "Today is your lucky day. You close the door and they don't chase you."
        return middle()
    else:
        print "Once again, your indecision fails you. They cut you down and have adventurer kebabs for dinner."
        return died()

def middle():
    print "You find yourself back in the dark corridor."
    print "Once again, you have a door to your left and a door to your right."
    print "You can also move ahead or exit the dungeon and call it a day."
    print "What do you want to do? Will you take the 'left' door, the 'right' door, move 'ahead' or 'exit' the dungeon?"

    middle_choice = raw_input("> ")

    if middle_choice == "left":
        room3()
    elif middle_choice == "right":
        room4()
    elif middle_choice == "ahead":
        end()
    elif middle_choice == "exit":
        run_away()
    else:
        room1_indecision()

def room2():
    print "As you push this door open, it falls from its rotten hinges and crashes to the ground."
    print "Fortunately, there are no terrible creatures waiting to eat you here. There is only a small wooden chest in the middle of the room."
    print "What would you like to do? 'Open' the chest or 'leave' the room?"

    room2_choice = raw_input("> ")

    if room2_choice == "open":
        print "The lid of the chest creaks open and reveals half a dozen rubies. You stuff them into your pouch and leave the room."
        # inv = open("ex36_game_txt.txt", 'w')
        # line1 = raw_input("12 rubies")
        # inv.write(line1)
        # inv.write("\n")
        # inv.close()
        # Add rubies to inventory
        return middle()
    elif room2_choice == "leave":
        middle()
    else:
        print "You're not good at making decisions, are you %s? Why don't you just leave the room and hope that your ability to make decisions returns next time?" % name
        return middle()

def room1_run():
    print "Throwing caution to the wind, you burst into the room and sprint to the treasure chest at the far end of the room."
    print "You hear a roar as you run and see a ferocious feral bear with claws extended hurtling after you in the dim light of the room."
    print "Just as you reach the treasure chest, the bear attacks you. What do you do?"
    print "You don't have any weapons. Do you fight or grab some treasure and run away?"

    bear_attack = raw_input("Choose either to 'fight' or 'run'. > ")

    if bear_attack == "fight":
        print "You put up a valiant struggle against the feral bear ... for about 10 seconds before it mauls you to death. Someone is probably proud of you and the bear has something to eat for dinner."
        return died()
    elif bear_attack == "run":
        print "You manage to grab a few handfuls of gold coins before the bear stabs its claws into you and sprint for the exit."
        # inv = open("ex36_game_txt.txt", 'w')
        # line2 = raw_input("10 gold coins")
        # inv.write(line2)
        # inv.write("\n")
        # inv.close()
        # I also want to add "gold coins" to a text file inventory that the script will add to.
        print "You manage to slam the door closed just as the bear reaches it. It howls in frustration and hunger."
        return middle()
    else:
        room1_indecision()

def room1_creep():
    print "You slowly enter the room, and look around. In the opposite corner of the room, you see a ferocious looking bear. It doesn't seem to have seen you yet."
    print "You make your way to the chest at the end of the room, checking to see whether the bear has seen you yet. So far, so good."
    print "Just as you reach the treasure chest, you hear a roar from the bear that seems to have seen you. What do you do? Rush 'back' to the door or go for the 'treasure'?"

    creep_choice = raw_input("You have two choices: 'back' or 'treasure'. > ")

    if creep_choice == "back":
        print "You make a run for it. You feel the bear's hot breath on the back of your neck but you reach the door before it catches you."
        print "You slam the door closed behind you and you find yourself back in the passage."
        return entrance()
    elif creep_choice == "treasure":
        print "You manage to grab a few handfuls of gold coins before the bear stabs its claws into you and sprint for the exit."
        # inv = open("ex36_game_txt.txt", 'w')
        # line3 = raw_input("10 gold coins")
        # inv.write(line3)
        # inv.write("\n")
        # inv.close()
        # I also want to add "gold coins" to a text file inventory that the script will add to.
        print "You manage to slam the door closed just as the bear reaches it. It howls in frustration and hunger."
        return middle()
    else:
        room1_indecision()

def room1_indecision():
    print "Once again, you are immobilised by fear, %s. This time it doesn't serve you and a terrible, feral bear pounces on you and mauls you savagely. Perhaps you will fare better in your next life." % name
    return died()

def room1():
    print "You push open a heavy wooden door and peer into a dimly lit room. You hear a shuffling sound somewhere in the room but you can't make out what's causing it."
    print "You notice a wooden chest at the far end of the room. You can just make out the glint of gold on the stone floor around the chest. Treasure!"
    print "What do you want to do? Burst into the room and run to the treasure or creep in more cautiously?"

    room1_choice = raw_input("Choose 'back', 'run' to the treasure or 'creep' in. > ")

    if room1_choice == "back":
        entrance()
    elif room1_choice == "run":
        room1_run()
    elif room1_choice == "creep":
        room1_creep()
    else:
        room1_indecision()

def entrance():
    print "You find yourself before the entrance to an ancient dungeon. It is dark inside and there is a terrible smell of death wafting out from its depths."
    print "You check your equipment (or rather the lack of any real equipment) and step inside ..."
    print "After a few steps into the gloomy dungeon, you see a door to your left and another to your right."
    print "You can also continue ahead or exit the dungeon."

    entrance_choice = raw_input("What is your choice? Left, right, ahead or exit? > ")

    if entrance_choice == "left":
        room1()
    elif entrance_choice == "right":
        room2()
    elif entrance_choice == "ahead":
        middle()
    elif entrance_choice == "exit":
        run_away()
    else:
        print "Still can't make a decision, %s? You can stand here and wait for something to eat you or you can choose to go left, right, ahead or the exit." % name
        print "Let's try that again, ok?"
        return entrance()

def run_away():
    print "You turn and return to safer lands. We won't think less of you. Braver adventurers than you have tried and failed. Try again, another day ..."

def start():
    print "Well, %s, this is a trecherous land. Only the brave venture here. Are you such a person? Are you willing to risk your life for glory and riches?" % name

    challenge1 = raw_input("What do you say? Are you up for the challenge? Answer 'yes' or 'no': > ")

    if challenge1 == "yes":
        print "Very well, you may proceed ..."
        entrance()
    elif challenge1 == "no":
        run_away()
    else:
        print "You have not made a choice. Frozen by terror?"
        print "Let's try that again. Take your time ..."
        return start()

start()
