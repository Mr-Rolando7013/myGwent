from card import Card, getCard

class User:
    def __init__(self, name, gamesWon, deckCards=[], leaderCard=None):
        self.name = name
        self.gamesWon = gamesWon
        self.deckCards = deckCards
        self.leaderCard = leaderCard
    
    def assignDeck(self, cards):
        # cards is a list of paths to the cards.
        for x, _ in enumerate(cards):
            card = getCard(cards[x])
            self.deckCards.append(card)
        
        return self.deckCards
    
    def assignLeaderCard(self, card):
        self.leaderCard = getCard(card)
        return self.leaderCards

    def __repr__(self):
        return f"Name: {self.name}, Deck: {self.deckCards}, Games won: {self.gamesWon}"
    
