#functions for mile stone project
from classes_project import card
from classes_project import deck
from classes_project import player

def draw_card(player_name,player_cards, player_sum, new_deck):
    new_card = new_deck.all_cards.pop(0)
    player_cards.append(new_card)
    
    if new_card.rank == "Ace":
        if player_name == "player1":
            print(f"You have {new_card.suit} of Ace")
            print(f"Right now, your sum is {player_sum}")
            while True:
                try:
                    value = int(input("Which value you want Ace to have between 1 and 11?"))
                except ValueError:
                    print("Enter an integer number")
                else:
                    if value == 1 or value == 11:
                        break
                    else:
                        print("Enter a number 1 or 11")
        else: #player_name == "dealer"
            if player_sum + 11 <= 21:
                value = 11
            else:
                value = 1
            
        new_card.value = value
    
    player_sum += new_card.value
    
    return player_sum

def compete(player_sum,dealer_sum):

    if dealer_sum > 21:
        return "player1"
    
    if player_sum > dealer_sum:
        return "player1"
    elif player_sum == dealer_sum:
        return "tie"
    else:
        return "dealer"

def BlackJack(player1):
    
    new_deck = deck()
    new_deck.shuffle()

    player_cards = []
    dealer_cards = []
    
    player_sum = 0
    dealer_sum = 0

    game_on = True
    at_war = True   

    print("\n")
    print(f"Hello {player1.name}!")
    print("Welcome to BlackJack")
    print(f"the current amount of your money is {player1.money}\n")
    if player1.money == 0:
        print("Look like you are broke!! Play next time!")
        game_on = False
    
    while game_on:

        #enter the bet
        print("How much do you wanna bet? :)")
        while True:  
            try:
                bet = float(input("Please enter the bet: "))
            except ValueError:
                print("Enter a number")
            else:
                if bet > player1.money:
                    print(f"The bet is too large. You only have {player1.money} dollars")
                else:
                    break

        # initiate the sums
        for i in range(2):
            player_sum = draw_card("player1",player_cards,player_sum,new_deck)
            dealer_sum = draw_card("dealer",dealer_cards,dealer_sum,new_deck)

        #game logic

        if player_sum < 21:

            #player turn
            print(f"The total sum of your cards is {player_sum}")
            print(f"The value of dealer's first card is {dealer_cards[0].value} \n")
            print("Do you want to hit or stay. Press 1: Stay, 2: Hit")
            while True:
                try:
                    decision = int(input())
                except ValueError:
                    print("Enter an integer number")
                else:
                    if decision == 1 or decision == 2:
                        break
                    else:
                        print("Enter 1 or 2")

            if decision == 2: #player hits
                player_sum = draw_card("player",player_cards,player_sum,new_deck)
                if player_sum > 21:
                    winner = "dealer"
                    at_war = False

            #compete
            if at_war:
                dealer_sum = draw_card("dealer",dealer_cards,dealer_sum,new_deck)
                winner = compete(player_sum,dealer_sum)

        else:
            winner = "dealer"

        #display the result
        display_dealer_cards = [(str(card),card.value) for card in dealer_cards]
        display_player_cards = [(str(card),card.value) for card in player_cards]

        print('\n')
        if winner == "player1":
            print('the winner is you! \n')
        elif winner == "tie":
            print("This is a tie!")
        else: 
            print('the winner is a dealer! \n')
        print('Dealer cards:') 
        for i in range(len(display_dealer_cards)):
              print(display_dealer_cards[i])
        print(f"\n total score: {dealer_sum} \n")

        print('Player cards:')
        for i in range(len(display_player_cards)):
              print(display_player_cards[i])
        print(f"\n total score: {player_sum} \n")

        print("***********************************************\n")
        
        #display player1's money
        if winner == "player1":
            player1.collect_money(bet)
        elif winner == "dealer":
            player1.lose_money(bet)
        print(f" the current amount of your money is {player1.money}\n")
        
        print("***********************************************\n")
        
        #Replay?
        print("Do you want to play again? ")
        
        while True:
            try:
                again = int(input(("Press 1: Yes, Press 2: No")))
            except ValueError:
                print("Enter a number")
            else:
                if again == 1 or again == 2:
                    break
                else:
                    print("Enter 1 or 2")
                    
        if again == 1:
            BlackJack(player1)
        else:
            print("Thank you for playing with us!")
        
        game_on = False

