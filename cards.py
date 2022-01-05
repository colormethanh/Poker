class Cards():
    
    def __init__(self):
        suits = ["hearts", "diamonds", "clover", "spades"]
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
        deck = [(suit, num) for suit in suits for num in nums] 
        
        print(f"the legnth of the deck is {len(deck)} cards long")
        print(deck[:10])
        
my_deck = Cards()
        
        
        