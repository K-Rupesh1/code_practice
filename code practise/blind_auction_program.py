def highest_bidding(bidding_finder):
    highest_bidding=0
    winner=""
    for bid in bidding_finder:
        bid_amount=bidding_finder[bid]
        if bid_amount > highest_bidding:
            highest_bidding=bid_amount
            winner=bid
            print(f"highest bidding person is {winner} with price &{highest_bidding}")


bid={}
continue_bidding=True
while continue_bidding:
    name=input("enter your name")
    price=int(input("enter bid amount:$"))
    bid[name]=price
    should_continue=input("any one are going to bet yes/no:").lower()
    if should_continue=="no":
        continue_bidding=False
        highest_bidding(bid)
    elif should_continue=="yes":
        print("\n"*20)