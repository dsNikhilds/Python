# Secret Auction Program

print("Welcome to the secret auction program!")

repeat = True
auction ={}
while repeat:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    auction[name] = bid
    user = input("Are there more bidders? Yes or No \n").lower()
    if user == "no":
        repeat = False
    else:
        pass
maxx = []

for key in auction:
    maxx.append(auction[key])
max_value = max(maxx)  
print(f"Maximum bidder is {list(auction.keys())[list(auction.values()).index(max_value)]} with a bid of {max_value}")    