from card import Card, getCard

class User:
    def __init__(self, name, gamesWon, deckCards=[], leaderCard=None):
        self.name = name
        self.gamesWon = gamesWon
        self.deckCards = deckCards
        self.leaderCard = leaderCard
    
    def assignDeck(self, cards):
        for x, _ in enumerate(cards):
            card = getCard(cards[x])
            self.deckCards.append(card)
        
        #print("DECK CARDSSS:", self.deckCards)
        return self.deckCards
    
    def assignLeaderCard(self, card):
        self.leaderCard = getCard(card)
        return self.leaderCards

    def __repr__(self):
        return f"Name: {self.name}, Deck: {self.deckCards}, Games won: {self.gamesWon}"
    
