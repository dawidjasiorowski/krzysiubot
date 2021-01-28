import random

with open("./adjectives.txt", "r") as f:
    s = str(f)
    adj = s.split(" ")
with open("./names.txt", "r") as f:
    s = str(f)
    names = s.split(" ")
#adjectives = ["Czekoladowy", "Lemoniadowy", "Marcepanowy", "Kisielowy", "Malinowy", "Truskawkowy", "Jablkowy", "Pomaranczowy", "Galaretkowy", "Chalwowy", "Batonikowy", "Gruszkowy", "Cytrynowy", "Owocowy", "Melonowy", "Arbuzowy", "Wodny", "Choco", "Floppa", "Giga", "Ultra"]
#names = ["John", "Lui", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth", "Joshua", "Kevin", "Brian", "George"]


def getName():
    a = random.randrange(0, len(adj))
    b = random.randrange(0, len(names))
    return adj[a] + " " + names[b]

print(getName())
