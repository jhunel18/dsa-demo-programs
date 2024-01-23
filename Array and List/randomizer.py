import random
leadersList = ["Aquino","Banal", "Chavenia", "Crujido", "Latchica", "Logmao","Macalam", "Macapagal", "Manalo", "Oflaria", "Ramos", "Verastigue"]

matchList = []
chosenOne = random.choice(leadersList)

while True:
    if chosenOne not in matchList:
        matchList.append(chosenOne)
        continue
    else:
        break
print(matchList)