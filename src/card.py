import hashlib
import json
import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self, name, image, damage, isLegend=False, specialAbility=None, weatherType=None):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)
        self.damage = damage
        self.isLegend = isLegend
        self.specialAbility = specialAbility
        self.weatherType = weatherType

    def __repr__(self):
        return f"Name: {self.name}, Damage: {self.damage}, Is Legend: {self.isLegend}"

class HouseCard(Card):
    def __init__(self, house, name, image, damage, field, isLegend, specialAbility=None, isLeader=False):
        self.house = house
        self.field = field
        self.isLeader = isLeader
        super().__init__(name, image, damage, isLegend, specialAbility, weatherType=None)
    
    def __repr__(self):
        base_rpr = super().__repr__()
        return f"{base_rpr} House: {self.house}, is leader: {self.isLeader}"
    
def sha256sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

#Maybe in the future I can check which is the best search algorithm for this situation.
def linearSearch(lHashes, hash):
    for i in lHashes:
        if i["hash"] == hash:
            return i

def getCard(url):
    # this is supposed to be the azure blob url, however right now will be a path
    hash = sha256sum(url)
    # Read json with all the info of the cards
    file = open("C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\cardsInfo\\cardsInfo.json", "r")
    # This returns a list
    lines = file.readlines()
    # Convert it to string, so json library can load it
    objects = ''.join(lines)
    x = json.loads(objects)
    isLegend = False
    weatherType = None

    cardInfo = linearSearch(x, hash)

    # Json crashes and show an error if object is not in the file. We gotta catch the error.
    try:
        if cardInfo["isLegend"]:
            isLegend = True
    except KeyError:
        isLegend = False

    try:
        if cardInfo["weatherType"]:
            weatherType = cardInfo["weatherType"]
    except KeyError:
        weatherType = None

    try:
        if cardInfo["isLeader"]:
            isLeader = True
    except KeyError:
        isLeader = False

    #if weatherType... Manage weather

    card = HouseCard (
        cardInfo["house"],
        cardInfo["name"],
        "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Schirru.png",
        cardInfo["damage"],
        cardInfo["field"],
        isLegend,
        cardInfo["ability"],
        isLeader)
    return card
