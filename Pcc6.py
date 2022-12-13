# ====== Dictionaries ======
alien_0 = {"color": "green", "points": 5}
print(alien_0 ["color"])
print(alien_0 ["points"])
alien_0["size"] = "large"

print(alien_0)


# It's convinient start a dictionary empty and add pairs as it goes.
Rmg = {}
Rmg["Ranged"] = 76
Rmg["Magic"] = 69
print(Rmg)

# Modifying a key-value in a Dictorionary.
Rmg["Magic"] = 70
print(f"Your magic level is now {Rmg['Magic']}")

#let's determine how fast magic is leveling up (exp per hour)
Rmg["Eph"] = "fast"
print(Rmg)
#give a exp per hour rate (slow, medium or fast)
if Rmg["Eph"] == "slow":
    lvl_increase = 1 #level
elif Rmg["Eph"] == "medium":
    lvl_increase = 2 #levels
elif Rmg["Eph"] == "fast":
    lvl_increase = 3 #levels

#The new level is the old level plus the increment
Rmg["Magic"] = Rmg["Magic"] + lvl_increase
print(f"New level after training 1 hour: {Rmg['Magic']}")

# Remove a key-value from a Dictorionary
del Rmg["Ranged"]
print (Rmg)

#new dictionary indented
fav_color = {
    "Itzel": "Pink",
    "Miley" :"Blue",
    "Alejandro": "Red",
    "Emma": "Orange"
}
print(f"Baby Emma's favorite color is {fav_color['Emma']}")
#the get() function
tere_fav_color = fav_color.get("Teresa","There is no Teresa assigned.")

#practice makes perfect
#looping on a dictionary write key & value in the for loop.// items() at the end of the dictionary


lucky_number = {
    "alejandro": 34,
    "jose": 15,
    "armando": 19,
    "katherine": 23,
    "lucia": 21,
}
for name,numbers in lucky_number.items():
    print(f"{numbers} is the lucky number for {name.title()}")