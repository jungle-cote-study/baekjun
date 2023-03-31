# 5568 : 카드 놓기
import copy
def addNumber(cards, n, resultNumber, resultNumbers):
  # 만약 남은 카드 갯수가 있으면 결과 뒤에 합치고 다음 카드 고르기
  # 남은 카드들은 이전에 사용한적 없는 카드여야 한다. 
  # 즉 이전에 사용한 카드들은 제거해서 넘겨주자
  if(n > 0) :
    for card in cards:
      list2 = cards[:]
      list2.remove(card)
      addNumber(list2, n-1, resultNumber + card, resultNumbers)
  else : 
    resultNumbers.add(resultNumber)
  
# 데이터 받기
cardsNum = int(input())
cards = []
n = int(input())
  
for _ in range(cardsNum):
  cards.append(input())

## 결과를 담을 SET
resultNumbers = set([])

addNumber(cards, n, "", resultNumbers)

print(len(resultNumbers))
