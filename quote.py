"""
modules
"""

import random
filename = "quotes.txt"
with open(filename) as filehandle:
    content = filehandle.read()
def quot():
    """
    import random quote
    """

    lines = content.split("\n")
    random.shuffle(lines)
    print(lines[0])

def lunch():
    """
    Print out random lunch
    """
    lunchStan = ['Olles krovbar',
                 'Lila thai stället',
                 'donken',
                 'tex mex stället vid subway',
                 'Subway',
                 'Nya peking',
                 'kebab house',
                 'Royal thai',
                 'thai stället vid hemmakväll',
                 'Gelato',
                 'Indian garden',
                 'Sumo sushi',
                 'Pasterian i stan',
                 'Biobaren',
                 'Michelangelo']
    random.shuffle(lunchStan)
    print("Albert says good choice!" + "\n")
    print(lunchStan[0])

def hellow():
    """
    print out a greeting
    """
    hello = ['Hej själv', 'trevligt att du bryr dig om mig', 'Det var länge sedan någon var trevligt om mig.',
             'Hello, det ser ut att bli mulet idag',
            ]
    random.shuffle(hello)
    print("Alfons says" + "\n")
    print(hello[0])
