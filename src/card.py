import hashlib
import json

class Card:
    def __init__(self, name, image, damage, isLegend=False, specialAbility=None, weatherType=None):
        self.name = name
        self.image = image
        self.damage = damage
        self.isLegend = isLegend
        self.specialAbility = specialAbility
        self.weatherType = weatherType

    def __repr__(self):
        return f"Name: {self.name}, Damage: {self.image}, Is Legend: {self.isLegend}"

class HouseCard(Card):
    def __init__(self, house, name, image, damage, isLegend, specialAbility=None, weatherType=None, isLeader=False):
        self.house = house
        self.isLeader = isLeader
        super().__init__(name, image, damage, isLegend, specialAbility, weatherType)
    
    def __repr__(self):
        base_rpr = super().__repr__()
        return f"{base_rpr} House: {self.house}, is leader: {self.isLeader}"
    
def sha256sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()
    
def merge(left, right, hash):
    result = []
    if left[0] <= right[0]:
        result.append(left[0])
        left.remove(0)

    
def mergeSort(lHashes, hash):
    iSize = len(lHashes)
    if iSize <= 1:
        return lHashes
    
    iMedium = iSize / 2, iStart = 0, iFinal = iSize - 1
    left = merge(lHashes[:iMedium - 1])
    right = merge(lHashes[iMedium:iFinal])
    return merge(left, right, hash)

def getCard():
    # this is supposed to be the azure blob url, however right now will be a path
    #hash = sha256sum(url)
    file = open("C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\cardsInfo\\cardsInfo.json", "r")
    lines = file.readlines()
    objects = ''.join(lines)
    x = json.loads(objects)
    print("SIZE:", len(x))

    return x[0]["hash"]

print(getCard())