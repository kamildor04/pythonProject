print("What type of adventure should I have?")
adventure = input()

if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest!")
elif (adventure == "safe") or (adventure == "long"):
    print("Taking the safe route")

print("What did I hear?")
sound = input()
print("What did I see?")
sight = input()

if (sound == "grrr") and (sight == "two red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")

