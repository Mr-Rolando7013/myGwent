from user import User

class Game:
    def __init__(self, user1, user2, pointsUser1, pointsUser2):
        self.user1 = user1
        self.user2 = user2
        self.pointsUser1 = pointsUser1
        self.pointsUser2 = pointsUser2

    def __repr__(self):
        return f"User 1: {self.user1}, User 2: {self.user2}, points user 1: {self.pointsUser1}, points user 2: {self.pointsUser2}"
    
    