import art as at
import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
pot = 200
print(at.logo)
print(at.houserules)
print(f"You will start with {pot} points")


def Blackjack():
    global pot
    while pot > 0:
        print(f"Your current pot is {pot} points")
        bet = int(input(f'''
        {at.bet}
        Place your bet='''))
        if bet> pot:
            print(f"Your current pot is {pot} points")
            bet = int(input("Bet cannot be more than the Pot: "))
            return
        if bet < 10:
            print(f"Your current pot is {pot} points")
            bet = int(input("Minimum bet must be 10, Put a higher bet: "))
            return
        user = []
        user = rd.sample(cards, 2)
        total = sum(user)
        print(f"You've been dealt with= {user} \n sum= {total}")
        dealer = []
        dealer = rd.sample(cards, 2)
        dealer_total = sum(dealer)
        print(f"the dealer has= {dealer[1]}")
        if total == 21:
            print(f"{at.logo} \nBlackjack! You win!")
            pot += bet
            continue
        elif dealer_total == 21:
            print(f"{at.lose} \nDealer has blackjack! You lose!")
            pot -= bet
            break
        while total < 21 and dealer_total < 21:
            choice = input("Do you want to Hit or Stand?= ").lower()
            
            if choice == "hit":
                user.append(rd.sample(cards, 1)[0])
                total = sum(user)
                print(f"You now have= {user} \n sum= {total}")

                if total > 21:
                    print(f"{at.bust} \nBust, Dealer wins!")
                    pot -= bet
                    break
                elif total == 21:
                    print(f"{at.logo} \nBlackjack! You win!")
                    pot += bet
                    break

            elif choice == "stand":
                print(f"Dealer's cards: {dealer} Sum={dealer_total}")
                
                
                while dealer_total < 17:
                    dealer.append(rd.sample(cards, 1)[0])
                    dealer_total = sum(dealer)
                    print(f"Dealer draws: {dealer} Sum={dealer_total}")
                
                if dealer_total > 21:
                    print(f"{at.win} \nDealer busts, you win!")
                    pot += bet
                elif dealer_total > total:
                    print(f"{at.lose} \nDealer wins!")
                    pot -= bet
                elif dealer_total < total:
                    print(f"{at.win} \nYou win!")
                    pot += bet
                else:
                    print(f"{at.draw} \nDraw!")
                
                break  
            
            else:
                print("Invalid choice. Please type 'hit' or 'stand'.")
        if pot <10:
            print("your pot is less than 10 points, you cannot play anymore")
            b= input("Do you want to play again? y/n: ")
            b=b.lower()
            if b== "y":
                pot = 200
                print(f"Pot restored to {pot} points")
                Blackjack()
            else:
                print("Thanks for playing!")
                break
    if pot == 0:
        print(at.gameover)
        a=input("Do you want to play again? y/n: ")
        a=a.lower()
        if a== "y":
            pot = 200
            print(f"Pot restored to {pot} points")
            Blackjack()
        else:
            print("Thanks for playing!")
Blackjack()
