import random

print("\nLet's play Rock, Paper, Scissors!\n")
your_bet = input("Rock(r), Paper(p) or Scissors(s)?: ")
score_you = 0
score_comp = 0


#for rock
def rock():
    hand = """
        _______
    ---'   ____)
          (_____)
ROCK      (_____)
          (____)
    ---.__(___)
    """
    return hand

def paper():
    hand = """
        ________
    ---'    ____)____
               ______)
PAPER         _______)
             _______)
    ---.__________)
    """
    return hand

def scissors():
    hand = """
        _______
    ---'   ____)____
              ______)
SCISSORS   _________) 
          (____)
    ---.__(___)
    """
    return hand

comp_choices = [rock(), paper(), scissors()]
comp_bet = random.choice(comp_choices)


def you_win(you, comp):
    score1 = 0
    print(f"\n\nYou chose: {you}")
    print(f"\nComputer chose: {comp}")
    print("                         Winner: YOU")
    score1 += 1
    return score1

def you_lose(you, comp):
    score1 = 0
    print(f"\nYou chose: {you}")
    print(f"\nComputer chose: {comp}")
    print("                         Winner: COMPUTER")
    score1 += 1
    return score1

def tie():
    if your_bet == "r":
        hand = rock()
        return hand
    elif your_bet == "p":
        hand = paper()
        return hand
    elif your_bet == "s":
        hand = scissors()
        return hand

def repeat():
    print(f"\n                         YOU: {score_you}  |  COMPUTER: {score_comp}")
    again1 = input("\nWould you try another round? Yes(y) or No(n): ")
    if again1 == "y":
        bet2 = input("\nRock(r), Paper(p) or Scissors(s)?: ")
        comp_bet2 = random.choice(comp_choices)
        return bet2, comp_bet2
    else:
        print(f"\n                         FINAL POINTS:")
        print(f"\n                         YOU: {score_you}  |  COMPUTER: {score_comp}")
        exit()

while True:
    if your_bet == "r":
        if comp_bet == paper():
            score = you_lose(rock(), paper())
            if score == 1:
                score_comp += 1

        elif comp_bet == scissors():
            score = you_win(rock(), scissors())
            if score == 1:
                score_you += 1
        else:
            your_bet2 = tie()
            print(f"You chose:"
                  f"{your_bet2}")
            print(f"\nComputer chose:"
                  f"{comp_bet}")
            print("                         It's a tie!")

        again = repeat()
        your_bet, comp_bet = again


    elif your_bet == "p":
        if comp_bet == scissors():
            score = you_lose(paper(), scissors())
            if score == 1:
                score_comp += 1

        elif comp_bet == rock():
            score = you_win(paper(), rock())
            if score == 1:
                score_you += 1
        else:
            your_bet2 = tie()
            print(f"You chose:"
                  f"{your_bet2}")
            print(f"\nComputer chose:"
                  f"{comp_bet}")
            print("                         It's a tie!")

        again = repeat()
        your_bet, comp_bet = again

    elif your_bet == "s":
        if comp_bet == rock():
            score = you_lose(scissors(), rock())
            if score == 1:
                score_comp += 1

        elif comp_bet == paper():
            score = you_win(scissors(), paper())
            if score == 1:
                score_you += 1

        else:
            your_bet2 = tie()
            print(f"You chose:"
                  f"{your_bet2}")
            print(f"\nComputer chose:"
                  f"{comp_bet}")
            print("                         It's a tie!")

        again = repeat()
        your_bet, comp_bet = again


    else:
        print("Invalid input. Try again")
        reenter = input("Rock(r), Paper(p) or Scissors(s)?: ")
        your_bet = reenter
