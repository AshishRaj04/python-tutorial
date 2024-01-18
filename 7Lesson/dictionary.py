# Dictionaries

band = {
    "name": "The Black Keys",
    "origin": "Louisville, Kentucky",
    "members": ["Dan Auerbach", "Patrick Carney"],
    "genres": ["rock", "blues"]
}

band2 = dict(
    name="Arcade Fire",
    origin="Edinburgh and Dublin, Scotland",
    members=["William Brittin", "Wincent Joye",
             "Tim Neill", "Col lin Donnelly", "Richard Reid"],

    genres=["indie rock", "art pop"]
)

print(band)
print(band2)
print(len(band))
print(type(band))

# Access items

print(band["origin"])
print(band.get("members"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list all keys/value pairs as tuple
print(band.items())

# Verify a key exists
print("guitar" in band)
print("genres" in band)

# Change values
band["name"] = "Black Keys"
band["members"].append("Mark Ronson")
band.update(
    {"website": "http://www.blackkeysmusic.com"},
)
print(band)

# Remove items
print(band.pop("website"))  # return popped item
print(band)

band["website"] = "http://www.blackkeysmusic.com"
print(band)

print(band.popitem())  # return popped item in tuple
print(band)

# Delete and clear

band["website"] = "http://www.blackkeysmusic.com"
print(band)
del band["website"]
print(band)

band2.clear()  # empty the band2
print(band2)

# Copy dictionaries

# band2 = band # Creates a refrence
# Don't use this method to copy dictionaries . Here both the variables refer to the same memory location . Changing something in one variable lets say poppin something from band will all pop out the same thing from band2
# print("Bad copy")
# print(band)
# print(band2)

# band["website"] =  "http://www.blackkeysmusic.com"
# print(band2)

band2 = band.copy()
band["website"] = "http://www.blackkeysmusic.com"
print("Good copy")
print(band)
print(band2)

band3 = dict(band)
print("Good copy")
print(band3)

# Nested dictionaries

member1 = {
    "name": "Elliottkeyword",
    "instrument": "guitar"
}

member2 = {
    "name": "Dexterkeyword",
    "instrument": "bass"
}

group = {
    "member1": member1,
    "member2": member2
}

print(group)
print(group["member2"]["instrument"])

