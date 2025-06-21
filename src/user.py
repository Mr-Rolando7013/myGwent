class User:
    def __init__(self, name, gamesWon, deckCards, leaderCard=None):
        self.name = name
        self.gamesWon = gamesWon
        self.deckCards = deckCards
        self.leaderCard = leaderCard
    def __repr__(self):
        return f"Name: {self.name}, Games won: {self.gamesWon}"