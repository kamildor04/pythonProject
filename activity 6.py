
print("How many bars should be charged?")
battery = int(input())
var = 0

while var < battery:
    var = var + 1
    print(f"Charging: {'█ ' * var}")

