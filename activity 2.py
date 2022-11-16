# Activity 2
print("Where should I look?")
place = input()

if place == "in the bedroom":

    print("Where in the bedroom should I look?")
    bound = input()

    if bound == "under the bed":
        print("Found some shoes but no battery")
    if bound != "under the bed":
        print("Found some mess but no battery")

if place == "in the bathroom":

    print("Where in the bathroom should I look?")
    bound = input()

    if bound == "in the bathtub":
        print("Found a rubber duck but no battery")
    if bound != "in the bathtub":
        print("Found a wet surface but no battery.")

if place == "in the lab":

    print("Where in the lab should I look?")
    bound = input()

    if bound == "on the table":
        print("Yes! I found my battery")
    if bound != "on the table":
        print("Found some tools but no battery")

