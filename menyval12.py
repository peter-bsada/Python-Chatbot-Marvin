"""
menu for option 12
"""
import random
import datetime
def menuval_12():
    """
    Print date and time
    """
    fhand = open("format.txt")
    line = fhand.readline()

    moods = ["happy", "sad", "depressed", "angry", "annoyed", "bored", "confused", "excited", "lonely"]
    mood = random.choice(moods)
    smilies = [":)", ":(", ":D", ":/", ":|", ":'(", ":O", ":@", ":P", ":3"]
    smiley = random.choice(smilies)

    talet = random.randint(0, 11)
    decimal = random.uniform(0, 11)
    print(line.format(mood=mood, smiley=smiley, talen=talet, deci=round(decimal, 3)))

    s = datetime.datetime.now().second
    m = datetime.datetime.now().minute
    h = datetime.datetime.now().hour
    days = datetime.datetime.now().day
    mon = datetime.datetime.now().month
    yr = datetime.datetime.now().year
    total_time = str(yr) + "-" + str(mon) + "-" + str(days) + " " + str(h) + ":" + str(m) + ":" + str(s)

    print("Dagens datum är:" + str(total_time))
