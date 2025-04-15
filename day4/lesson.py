import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#first way
print(random.choice(friends))

#second way
#random_friends_select = random.randint(0, len(friends)-1)
#print((friends[random_friends_select]))

#random_heads_or_tails = random.randint(0, 1)
#print(f"random number = {random_heads_or_tails}")
#if random_heads_or_tails == 0:
#    print("Heads")
#else:
#    print("Tails")