# Activity 1
print("What type of cover does the book have?")
cover = input()

if cover == "soft":

    print("Is the book perfect-bound?")
    bound = input()

    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    if bound != "yes":
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")
