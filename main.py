#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import marvin
import inventory
import menyval12
import quote
marvin_image = r"""
         _____
     _-~~     ~~-_//
   /~             ~\
  |              _  |_
 |         _--~~~ )~~ )___
\|        /   ___   _-~   ~-_
\          _-~   ~-_         \
|         /         \         |
|        |           |     (O  |
 |      |             |        |
 |      |   O)        |       |
 /|      |           |       /
 / \ _--_ \         /-_   _-~)
   /~    \ ~-_   _-~   ~~~__/
  |   |\  ~-_ ~~~ _-~~---~  \
  |   | |    ~--~~  / \      ~-_
   |   \ |                      ~-_
    \   ~-|                        ~~--__ _-~~-,
     ~-_   |                             /     |
        ~~--|                                 /
          |  |                               /
          |   |              _            _-~
          |  /~~--_   __---~~          _-~
          |  \                   __--~~
          |  |~~--__     ___---~~
          |  |      ~~~~~
          |  |
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hello my name is Albert. I know about everything in the world. What can I do for you ?")

    marvin.menu()

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        marvin.greeter()

    elif choice == "2":
        marvin.converts_celcius_to_fahrrenheit()

    elif choice == "3":
        marvin.multiplier()

    elif choice == "4":
        marvin.average()

    elif choice == "5":
        marvin.higher_lower()

    elif choice == "6":
        marvin.seperator()

    elif choice == "7":
        marvin.isogram_()

    elif choice == "8":
        marvin.random_letter()

    elif choice == "9":
        marvin.anagram()

    elif choice == "10":
        marvin.akronym()

    elif choice == "11":
        marvin.disquise_numbers()

    elif choice == "12":
        menyval12.menuval_12()

    elif choice == "inv":
        inventory.readfile()

    elif "citat" in choice or "Citat" in choice:
        quote.quot()

    elif "lunch" in choice or "annan lunch" in choice:
        quote.lunch()

    elif "hej" in choice:
        quote.hellow()

    elif "inv" and "pick" in choice:
        inventory.write_to_file(choice[9:], "a")

    elif "inv" and "drop" in choice:
        inventory.remove_item(choice[9:])

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
