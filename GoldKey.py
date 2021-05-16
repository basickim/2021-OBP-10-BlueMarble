import random

class GoldKey():
    """황금열쇠"""
    
    card = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    mycard = random.choice(card)
    
    def draw(self):
        """"황금열쇠 뽑기"""
        
        
        matching = {1 : "+5 골드",
                    2 : "+10 골드",
                    3 : "-5 골드",
                    4 : "-10 골드",
                    5 : "세계여행",
                    6 : "우대권",
                    7 : "출발점으로",
                    8 : "정중앙으로",
                    9 : "자리 바꾸기",
                    10 : "어딘가로 문",}
        
        return (matching[GoldKey.mycard])

    def freepass(self):
        """우대권 저장"""

        if(GoldKey.mycard == 6):
            print("keep or go?")
    


""""--------------------test--------------------------------------------"""    
key = GoldKey()

print(key.draw())
key.freepass()