print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')


print("Welcome to treasure Island!\nYour mission is to find the treasure.")

way = input("Which way traveller?: left or right?").lower()

if way == "left":
    swim = input("swim or wait?").lower()
    if swim=="wait":
        door = input("which door? -> Red, blue, or Yellow?").lower()
        if door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")
