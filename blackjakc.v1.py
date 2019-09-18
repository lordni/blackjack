import random
# BlackJack eller 21 game

# Planlægningsfasen
    # Dealer kortene array
    # Spiller kortene array

# Deal
    # Dealer
        # Giv kort til Dealer
#while len(dealer_cards) < 3:
#    dealer_cards.append(random.randint(1, 11))
        
    # Giv kort til spilleren
#while len(player_cards) < 3:
#    player_cards.append(random.randint(1, 11))        

# Udregn og gem summen af spillerens kort

# Print dealer og spillers kort

#print("Dealer has x & ", dealer_cards[1])
#print("You have ", player_cards, " sum is " , sum(player_cards))

# Udregn dealerens kort sum

# Sammelign og fortsæt spillet
    # Dealer skal finde ud af om sum af kortene er li med 21 eller over 21

    #print("Dealer has ", d_sum, " and wins!")

    #print("Dealer busted")

# Spilleren
# Fortsæt loop så lang tid spilleren har en kortsum på under 21
    # få input om spilleren vil ha et nyt kort eller stå
        # Hvis "hit" bliver valgt så giv spilleren et kort mere,
        # udregn summen af kort og udskriv spillerens kort og sum
    # Ellers
while p_sum < 21:
    aktion_taken = str(input("Do you want to stay or hit? "))
    if aktion_taken == "hit" or aktion_taken == "h":
        player_cards.append(random.randint(1, 11))
        p_sum = sum(player_cards)
        print("You now have a total of " + str(p_sum) + " from these cards ", player_cards)
    else:
        # Dealer hit until > 15
        while d_sum < 16:
            dealer_cards.append(random.randint(1, 11))
            d_sum = sum(dealer_cards)
        
        print("Dealer has ", d_sum, " with ", dealer_cards)
        print("You now have a total of " + str(p_sum) + " from these cards ", player_cards)
        if d_sum > p_sum and d_sum < 22:
            print("Dealer wins!")
            break
        else:
            print("You Win!")
            break

if p_sum > 21:
    print("You are BUSTED! Dealers wins.")
elif p_sum == 21:
    print("You got BLACKJACK! You Win!! 21")
    
    # Compare sums of the cards between player and dealer
        # If player card sum is greater than 21 = BUST
        # If player card sum is less than 21 = option Hit or Stay
        # If player option Stay compare sum of Dealer vs Player
        # If player card sum < 21 && > Dleaer card sum then Player wins!
        # If player card sum < Dealer card sum then Player loses


# The dealer should go on getting cards until he hits 16 or above


# Next time
# Money and stuff could be nice to