import random
from random import choice, randint, shuffle
import statistics

coin = random.choice(["heads", "tails"])
fav_city = choice(["Istanbul", "Kandahar"])
print(coin)
print(fav_city)
randNumber = randint(1, 10)
print(randNumber)
cards = ["Ace", "King", "Queen", "Jack"]
shuffle(cards)

for card in cards:
    print(card)


math_avg = statistics.mean([90, 80])
print(math_avg)
