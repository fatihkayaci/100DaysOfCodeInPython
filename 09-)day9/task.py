from art import logo
print(logo)
bids = {}
continue_program = True
while continue_program:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    program = input("Are there any other bidders? Type 'yes' or 'no'. ")
    
    if program == "no":
        continue_program = False
    else:
        print("\n" * 100)

max_bid = 0
name = ""
for key in bids:
    if max_bid < bids[key]:
        name = key
        max_bid = bids[key]
print(f"The winner is {name} with a bid of ${max_bid}")
