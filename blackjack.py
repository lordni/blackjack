import random
# BlackJack or 21 game
# Planing phase
    # Dealer cards
dealer_cards = []
    # Player cards
player_cards = []
# Deal and display Cards
    # Dealer
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has x & ", dealer_cards[1])
    # Player
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have ", player_cards[1])

d_sum = sum(dealer_cards)
p_sum = sum(player_cards)
    # Sum cards
        #Dealer 
        #Player
# Compare
    # Dealer
if d_sum == 21:
    print("Dealer has ", d_sum, " and wins!")
elif d_sum > 21:
    print("Dealer busted")

    # Player
while p_sum < 21:
    aktion_taken = str(input("Do you want to stay or hit? "))
    if aktion_taken == "hit" or aktion_taken == "h":
        player_cards.append(random.randint(1, 11))
        p_sum = sum(player_cards)
        print("You now have a total of " + str(p_sum) + " from these cards ", player_cards)
    else:
        print("Dealer has ", d_sum, " with ", dealer_cards)
        print("You now have a total of " + str(p_sum) + " from these cards ", player_cards)
    
    
    # Compare sums of the cards between player and dealer
        # If player card sum is greater than 21 = BUST