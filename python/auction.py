import os

def findwinner(bidder_details):
    highest_bid=0
    winner=""
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
            
    print(f"the winner is {winner} with a bid_price of {highest_bid}")
    
        
    

bidder_data={}
flag=False
while not flag:
    name=input("what is your name:")
    price=int(input("what is your bid?"))
    bidder_data[name]=price
    more_bidders=input("are there more biddders tyoe yes or no:").lower()
    if more_bidders=='no':
        flag=True
        findwinner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')
    
    
    

    
