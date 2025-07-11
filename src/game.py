from user import User

class Game:
    def __init__(self, user1, user2, pointsUser1, pointsUser2, isUser1Turn, isUser2Turn):
        self.user1 = user1
        self.user2 = user2
        self.pointsUser1 = pointsUser1
        self.pointsUser2 = pointsUser2
        self.isUser1Turn = isUser1Turn
        self.isUser2Turn = isUser2Turn
        

    def startGame(self, cardsUser1, cardsUser2):
        self.user1.assignDeck(cardsUser1)
        self.user2.assignDeck(cardsUser2)

    def __repr__(self):
        return f"User 1: {self.user1}, User 2: {self.user2}, points user 1: {self.pointsUser1}, points user 2: {self.pointsUser2}"
    
    