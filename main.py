print("Greetings! It's auction program")
bidders = {}

def list_of_bidders(name, bid):
    bidders[name] = bid
    print(bidders)


def winner(bidders):
    max = 0
    winner = ''
    for key in bidders:
        if bidders[key] > max:
            max = bidders[key]
            winner = key
    print(winner, max)


go_on = True
while go_on:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    list_of_bidders(name, bid)
    add_new = input("Any other bidders? Y/N: ").lower()
    if add_new == "n":
        winner(bidders)
        go_on = False

