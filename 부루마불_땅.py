#땅 정보 필요한거 : 땅 이름, 가격, 땅 소유자 , 땅 좌표(진행하면서 추가)
#맵 중앙 0,0 우상이 양수
#절대값이 같으면 대각선 라인


class Territory_A1:
    name = "서울"                                      #땅 이름 - 클래스 변수
    price = 15                                         #땅 가격 - 클래스 변수
    
    def __init__(self, owner):
            #self.name = "서울"                  
            #self.price = int(1500)              
            self.owner = owner                        #땅 주인 - 인스턴스 변수

    def ChangePrice(self, price):                     #땅 가격 변경
            if self.price <= price :
                    self.price = price
            else:
                print("비용 낮음")                     #낮으면 땅 값 안오름
            
    def ChangeOwner(self,owner):                      #땅 주인 변경
            self.owner = owner

    def ShowTerritoryInformation(self):               #땅 정보 보기
            print(self.name, self.price, self.owner)
            
        
            
temp=Territory_A1("플레이어 1")

temp.ShowTerritoryInformation()      

temp.ChangeOwner("플레이어 2")

temp.ChangePrice(10)

temp.ShowTerritoryInformation()

temp.ChangePrice(20)

temp.ShowTerritoryInformation()