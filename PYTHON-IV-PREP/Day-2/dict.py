ipl = ["CSK", "MI"]
for team in ipl:
    print(team)

ipl = {
    "CSK": "Chennai Super Kings",
    "MI": "Mumbai Indians"
}

for team in ipl:
    print(team)
    print(ipl[team])

ipl = ("CSK", "MI")
team1 = ipl[0]
team2 = ipl[1]

team1, team2 = ("CSK", "MI")

ipl = {
    "CSK": "Chennai Super Kings",
    "MI": "Mumbai Indians"
}

print(ipl.keys())
print(ipl.values())
# print(ipl.items())

for team, name in ipl.items():
    print(team)
    print(name)

ipl = ["CSK", "MI", "KKR"]
for team in ipl:
    print(team)
    if team == 'MI':
        break

ipl = ["CSK", "MI", "KKR"]
for team in ipl:
    if team == 'MI':
        continue
    print(team)

# List comprehension
ipl = ["CSK", "MI", "KKR"]
ipl_len = []
for team in ipl:
    ipl_len.append(len(team))

print(ipl_len)

ipl = ["CSK", "MI", "KKR"]
ipl_len = []
for team in ipl:
    if len(team) > 2:
        ipl_len.append(len(team))

print(ipl_len)

ipl = ["CSK", "MI", "KKR"]
ipl_len_com = [len(team) for team in ipl]
print(ipl_len_com)

ipl = ["CSK", "MI", "KKR"]
ipl_len_com = [len(team) for team in ipl if len(team) > 2]
print(ipl_len_com)
