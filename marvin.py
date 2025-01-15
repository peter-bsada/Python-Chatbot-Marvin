"""
All def Functions
"""
def menu():
    """
    Prints menu
    """
    print("1) Present yourself to Marv Albert.")
    print("2) Celsius to fahrenheit.?")
    print("3) Multiply a word")
    print("4) Sum and average")
    print("5) Higher or Lower")
    print("6) Word dasher")
    print("7) isogram")
    print("8) Random word")
    print("9) Anagram")
    print("10) Akronym")
    print("11) Disquise")
    print("12) Date and time")
    print("q) Quit.")

def greeter():
    """
    Prints greeting
    """
    name = input("What is your name? ")
    print("\nAlbert says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do for you?!")

def converts_celcius_to_fahrrenheit():
    """
    Converts celcius to fahrenhet
    """
    celcius = input("What is your temperatur in celcius?: ")
    resultcel = int(celcius)* 9 / 5 + 32
    print("\nAlbert says:\n")
    print("your temperatur is %s Farenheit" % resultcel)
    print("What can I do you for?!")

def multiplier():
    """
    Multiply a word with a number
    """
    word = input("Write any word: ")
    number = input("Write any number: ")
    print("\nAlbert says:\n")
    i = 0
    while i < int(number):
        print(word)
        i += 1
        print("")
    print("What can I do for you?!")

def average():
    """
    Sums up the numbers and finds the average.
    """
    counter = 1
    total = 0
    num = input("Write any number: ")
    if num == "d":
        print("not a number.")

    else:
        try:
            total = int(num)
        except ValueError:
            print("not a number.")

    while num != "d":
        num = input("d) for done or add more number: ")
        if num == "d":
            print("\nAlbert says:\n")
            resultf = str(int(total) / int(counter))
            print("Summan: " + str(total))
            print("Medelvärdet " + str(resultf))
            print("\nWhat can I do for you?\n")
            continue
        else:
            try:
                total = total + int(num)
                counter = counter + 1
            except ValueError:
                print("not a number.")
                continue

def higher_lower():
    """
    Checks if the previous number
    is higher or lower than current
    """
    current = input("Write a number: ")
    previous = input("write another number: ")
    while True:
        if current == "d":
            print("\nWhat can I do for you?!\n")
            print("bye!")
            break
        if int(current) > int(previous):
            print("\nAlebert says: ")
            print("\nCurrent number " + current+ " is larger\n")
        elif int(current) == int(previous):
            print("\nAlebert says: ")
            print("\nCurrent equal to previous\n")
        else:
            print("\nAlebert says: ")
            print("Previous number " + previous + " is larger")

        previous = current
        print("Old current, now previous: " + previous)
        current = input("Write a number (current) or (d) for done: ")

def seperator():
    """
    Seperates word with -
    """
    result = ""
    i = 1
    word_one = input("Write any word: ")
    for letter in word_one:
        result = result + letter * i + "-"
        i += 1
    print(result.rstrip("-"))

def isogram_():
    """
    Looks if the word is an isogram
    """
    word_input = input("Write the word you want to check: ")
    isogram = True

    for letter in word_input:
        count = 0

        for check_letter in word_input:
            if letter == check_letter:
                count += 1
                if count > 1:
                    isogram = False
                    break
        if not isogram:
            break

    if isogram:
        print("\nAlebert says: \n")
        print("Match")
        print("\nWhat can I do for you?!\n")
    else:
        print("\nAlebert says: \n")
        print("no match")
        print("\nWhat can I do for you?!\n")

def random_letter():
    """
    Throws around the letters in a word
    """
    import random
    word = input("Write a word ")
    shuffled = list(word)
    random.shuffle(shuffled)
    shuffled = ''.join(shuffled)
    print(shuffled)

def anagram():
    """
    checks if the two words is an anagram or not
    """
    wordone = input("write an word: ")
    wordtwo = input("write another word: ")
    if sorted(wordone.lower()) == sorted(wordtwo.lower()):
        print("\nAlebert says: \n")
        print("Match")
        print("\nWhat can I do for you?!\n")
    else:
        print("\nAlebert says: \n")
        print("no Match")
        print("\nWhat can I do for you?!\n")

def akronym():
    """
    New word with big letters
    """
    word = input("write an word: ")
    fullword = ""
    for letter in word:
        if letter.isupper():
            fullword += letter
    print(fullword)

def disquise_numbers():
    """
    disquise numbers execpt the last four numbers
    """
    fullnumber = ""
    firstnumber = input("Write an number: ")
    numberlenght = len(firstnumber)
    for index, letter in enumerate(firstnumber):
        if index >= numberlenght -4:
            fullnumber += letter
        else:
            fullnumber += "#"
    print("\nAlebert says: \n")
    print(fullnumber)
    print("\nWhat can I do for you?!\n")
