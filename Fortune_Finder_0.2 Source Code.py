import random
import time
import os
import csv
import numpy as np
import sys
import threading
import pandas as pd

#added the net profit loss but decieded not to use it. 
#will prob remove later if no use

RESET = "\033[0m"
BLACK = '\033[30m'
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BROWN = "\033[38;5;94m"

# for crash game

max_value = 100
exponent = 3

# function used to ask user if they want to play again
def replay_prompt():
    global game_selection
    global game_functions
    while True:
        try:
            user_input = input("Would you like to play again? (y/n): ")
            if user_input not in ["y","n"]:
                print("Invalid input please select (y/n): ")
            elif user_input == "y":
                return game_functions[game_selection]()
            else:
                home()
        except ValueError:
            print("Invalid input. Please enter a number.")

# counter for loans
loan_counter_mult = 0
def loan_counter():
    global loan_counter_mult
    loan_counter_mult += 1
    return loan_counter_mult
loan_counter()

    

# loan multiplier
# all source code of games

def detect_color_tower(num):
    if num == 0:
        return RESET
    elif num == 1:
        return RED
    elif num == 2:
        return GREEN
# clear check and checks if diff os system

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def make_loan_multi():
    # This variable will hold the current value
    value = 0
    
    def incrementer(amount):
        nonlocal value
        # Add 5% to the current value
        value += value * 0.05
        # Add the amount to the updated value
        value += amount
        return value
    
    return incrementer

# 33%
def black_jack_rig_user():
    global user_score
    temp_val_1 = random.randint(1,2)
    temp_val_2 = 1
    if temp_val_1 == temp_val_2:
        if 13 <= user_score <= 15:
            return random.randint(9,10)
    else:
        return None

# 25%
def black_jack_rig_dealer():
    temp_val_1 = random.randint(1,2)
    temp_val_2 = random.randint(1,2)
    if temp_val_1 == temp_val_2:
        return random.randint(2,5)
    else:
        return None

# Create an instance of the incrementer function
loan_multi = make_loan_multi()
loaned = False
def save_variables(name):
    global loaned
    global total_credit
    global names_and_credits
    total_credit = round(total_credit)
    banked_credits = 0
    if name in names_and_credits:
        banked_credits = names_and_credits[name]['credits']
    else:
        names_and_credits[name] = {'credits': 0, 'net_profit_loss': 0}
    
    if not loaned:
        loan_amount = total_credit * 2
    
    
    # Prompt user for input
    print("")
    while True:
        user_input_var = input("Would you like to deposit, withdraw, or take out a loan(d/w/l): ")
        if user_input_var not in ["d","w","l"]:
            print("Enter a valid input")
        else:
            break
    print("")
        # deposit
    if user_input_var == "d" or user_input_var == "deposit":
        while True:
            time.sleep(0.5)
            print(f"You currently have {GREEN}{total_credit}{RESET} total credits.")
            print("") 
            time.sleep(0.5)
            print(f"You currently have {YELLOW}{banked_credits}{RESET} in the bank") 
            print("")
            banked_amount = int(input("How much would you like to deposit: "))
           
            if banked_amount > total_credit:
                print("Insufficient credits.")
            else:
                total_credit -= banked_amount
                banked_credits += banked_amount
                names_and_credits[name]['credits'] = banked_credits
                update_bank("bank.csv", names_and_credits)
                print(f"You have deposited {YELLOW}{banked_amount}{RESET}")
                time.sleep(1) 
                home() # returns
                # withdraw
    elif user_input_var.lower() == "w" or user_input_var == "withdraw":
        while True:
            time.sleep(0.5)
            print(f"You currently have {GREEN}{total_credit}{RESET} total credits.")
            print("")
            time.sleep(0.5)
            print(f"You currently have {YELLOW}{banked_credits}{RESET} in the bank")
            print("")
            withdraw_var = int(input("How much would you like to withdraw: "))

            # checks if user has enough to withdraw

            if withdraw_var > banked_credits:
                print("Insufficient credits.")
            else:
                banked_credits -= withdraw_var
                total_credit += withdraw_var
                names_and_credits[name]['credits'] = banked_credits
                update_bank("bank.csv", names_and_credits)
                print("")
                print(f"You have withdrew {YELLOW}{withdraw_var}{RESET}")
                time.sleep(1)
                home() #returns
    # needs checker
    # if not in ["l","loan"]:
    #     print("")
    elif user_input_var.lower() == "l" or user_input_var == "loan":
        if not loaned:
            clear_screen()
            while True:
                time.sleep(0.5)
                print(total_credit)
                print(f"You qualify to take out a loan of {YELLOW}{loan_amount}{RESET}.")
                time.sleep(0.5)
                print(f"The interest rate is {RED}5%{RESET} each bet.")
                loan_var = int(input("How much you like to acquire: "))
                print()
                if loan_var > loan_amount:
                    print("Insufficient credits.")
                else:
                    loaned = True
                    total_credit += loan_var
                    time.sleep(0.5)
                    print(f"You have taken out a loan of {YELLOW}{loan_var}{RESET}")
                    time.sleep(0.5)
                    print(f"You will have to pay back the loan within {RED}10 bets{RESET}")
                    time.sleep(0.5)
                    print(f"The interest rate each bet is {RED}5%{RESET}")
                    time.sleep(1.5)
                    print("Good luck.")
                    time.sleep(1.5)
                    home()
        
            
                    
        elif loaned:
            clear_screen()
            shown_loan_counter_mult = 10
            shown_loan_counter_mult -= loan_counter_mult
            print(f"You have {RED}{shown_loan_counter_mult}{RESET} days left to pay your due's")
            time.sleep(5)
            home()
            # print(f"You currently owe {}")
        



        
    #int_var3 = int(input("Enter one more integer value for variable3: "))

    # Store variables in a dictionary
    update_bank("bank.csv", names_and_credits, names_and_profit_loss, )

# Example usage
#save_variables()

def update_bank(file_path, data):
    # Assume 'data' is a dictionary where each value is another dictionary including 'credits' and 'net_profit_loss'
    new_data = [{'name': name, 'credits': info['credits'], 'net profit/loss': info['net_profit_loss']} for name, info in data.items()]

    # Write the data to the CSV file
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['name', 'credits', 'net profit/loss']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()
        
        # Write the data
        writer.writerows(new_data)


def extract_name_and_credits(csv_file_path, name_to_check):
    name_details_dict = {}
    name_found = False

    # Open and read the CSV file
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV
        for row in reader:
            name = row['name'].strip()  # Strip whitespace from name
            credits = int(row['credits'].strip())
            net_profit_loss = int(row['net profit/loss'].strip())

            # Add the name, credits, and net profit/loss to the dictionary
            name_details_dict[name] = {'credits': credits, 'net_profit_loss': net_profit_loss}

            # Check if the current row's name matches the name_to_check
            if name == name_to_check.strip():  # Strip whitespace from name_to_check
                name_found = True
    
    # Return True if the name was found, otherwise return the dictionary
    if name_found:
        return True
    else:
        return name_details_dict

def skewed_random(max_value, exponent):
    # Generate a random number between 0 and 1
    rand_value = random.random()
    
    # Apply the exponent to skew the distribution
    skewed_value = rand_value ** exponent
    
    # Scale to the desired maximum value
    result = skewed_value * max_value
    if result > 90:
        result = random.uniform(19,99)
    elif result > 75:
        result =  random.uniform(9,18.99)
    elif result > 47:
        result = random.uniform(3.5,8.99)
    elif result > 28:
        result = random.uniform(1.9,3.4)
    else:
        result = random.uniform(1,1.9)
        insta_crash_check1 = random.randint(1,3)
        insta_crash_check2 = random.randint(1,3)
        if insta_crash_check1 == insta_crash_check2:
            result = 1
    
    if isinstance(result, (int, float)):
        result = round(result, 2)
    return result
    

explode_value = skewed_random(max_value, exponent)
#test thing

#thingy = skewed_random(max_value, exponent)
#print(thingy)
#thingy = skewed_random(max_value, exponent)
#print(thingy)
#for i in range(100):
    #print(skewed_random(max_value, exponent))

banked_value = 0
crash_checker = False
crash_win = False
def exponential_rise(max_value, num_points):
    log_space = np.logspace(0, np.log10(max_value), num=num_points)
    scaled_values = np.interp(log_space, (log_space.min(), log_space.max()), (1, max_value))
    return scaled_values

def display_exponential_change(max_value, stop_flag):
    global value
    global banked_value
    global crash_checker
    global crash_win
    explode_value = skewed_random(max_value, exponent)
    
    num_points = 115
    sequence = exponential_rise(max_value, num_points)
    for value in sequence:
        if stop_flag.is_set():
            if crash_checker == False:
                banked_value = value
                print(f"{GREEN}Cashed{RESET}")
                crash_checker = True
                crash_win = True
        
        sys.stdout.write("\r" + f"RISING... {GREEN}{value:.2f}" + f"x{RESET}")
        sys.stdout.flush()
        time.sleep(0.6)  # Sleep for 0.6 seconds to simulate time passing
        if value >= explode_value:
            print("")
            print(f"{RED}BOOM{RESET}")
            if crash_win == False:
                print("(Press Enter to contine)")
            return True
    return False

def user_input_thread(stop_flag):
    input("Press Enter to stop the rocketship...\n")
    stop_flag.set()


def bank():
    global total_credit
    global user_name
    clear_screen()
    print()
    print(f"{YELLOW}Welcome to the bank!{RESET}")
    print()
    save_variables(user_name)

    

def dice_game():
    clear_screen()
    global total_credit
    global user_name
    
    
    # Display welcome message and instructions
    print("")
    print(f"{GREEN}Welcome to the dice game!{RESET}")
    print("")
    print("In this game all you do is try to guess the number the dice will roll on.")
    print("")
    print(f"There are two versions, one the {BLUE}dice will have 3 sides{RESET} and the other, the {MAGENTA}dice will have 6.{RESET}")
    print("")
    
    
    
    # Prompt user to select the dice game version
    time.sleep(1)
    while True:
        
        try:
            sub_game_dice = input(f"Type {BLUE}0{RESET} for the first game; Type {MAGENTA}1{RESET} for the second game; Type {RED}2{RESET} to go back: ")
            
        except ValueError:
            print("Invalid input")
        
        if sub_game_dice not in ["0", "1", "2"]:
            print("Please select a valid input (0/1/2)")
        else:
            break
    if sub_game_dice == "2":
        home()
        
    # Game loop for the dice with 3 sides
    if sub_game_dice == "0":
        while True:
            total_credit = round(total_credit)
            # Roll the dice and display credits
            dice_side_3 = random.randint(1, 3)
            print()
            print(f"You currently have {GREEN}{total_credit}{RESET} credits")
            print()
            time.sleep(0.5)

            # Get and validate the bet amount
            while True:
                    try:
                        bet_amount_dice_3 = float(input("How much would you like to bet: "))
                        if bet_amount_dice_3 <= 0 or bet_amount_dice_3 > total_credit:
                            print("Invalid input. Please enter a valid bet amount.")
                        else:
                            break
                    except ValueError:
                        print("Enter a valid input")
                    
            
            
            time.sleep(0.5)
            print("")
            print(f"You have selected {GREEN}{bet_amount_dice_3}{RESET} to bet")
            total_credit -= bet_amount_dice_3
            print("")
            time.sleep(0.5)

            # Get and validate the user's guess
            while True:
                guess_dice_3 = int(input(f"Guess which side the dice rolled {GREEN}(1-3){RESET}: "))
                if guess_dice_3 not in [1, 2, 3]:
                    print("Please select a valid input (1-3)")
                else:
                    break
            time.sleep(0.5)
            print("Rolling....")
            time.sleep(0.5)
            print("Rolling....")
            time.sleep(0.5)
            print("Rolling....")
            time.sleep(1)

            # Check if the user guessed correctly
            if guess_dice_3 == dice_side_3:
                print("")
                print(f"The dice rolled a {GREEN}{dice_side_3}{RESET}")
                print(f"{GREEN}You have guessed correctly{RESET}")
                bet_amount_dice_3 *= 2
                total_credit += bet_amount_dice_3
                total_credit = round(total_credit)
                print(f"You now have {GREEN}{total_credit}{RESET} total credits!")
            else:
                # User guessed incorrectly
                print(f"The dice rolled a {RED}{dice_side_3}{RESET}")
                print(f"{RED}You have guessed incorrectly.{RESET}")
                print(f"You now have {RED}{total_credit}{RESET} total credit.")

            replay_prompt()

    # Game loop for the dice with 6 sides
    if sub_game_dice == "1":
        while True:
            # Roll the dice and display credits
            total_credit = round(total_credit)
            dice_side_6 = random.randint(1, 6)
            print("")
            print(f"You currently have {GREEN}{total_credit}{RESET} credits")
            print("")
            time.sleep(0.5)

            # Get and validate the bet amount
            while True:
                try:
                    bet_amount_dice_6 = float((input("How much would you like to bet: ")))
                    if bet_amount_dice_6 <= 0 or bet_amount_dice_6 > total_credit:
                        print("Invalid input. Please enter a valid bet amount.")
                    else:
                        break
                except ValueError:
                        print("Enter a valid input")
            time.sleep(0.5)
            print("")
            print(f"You have selected {GREEN}{bet_amount_dice_6}{RESET} to bet")
            total_credit -= bet_amount_dice_6
            print("")
            time.sleep(0.5)

            # Get and validate the user's guess
            while True:
                guess_dice_6 = int(input(f"Guess which side the dice rolled {GREEN}(1-6){RESET}: "))
                if guess_dice_6 not in [1, 2, 3, 4, 5, 6]:
                    print("Please select a valid input (1-6)")
                else:
                    break
            time.sleep(0.5)
            print("Rolling....")
            time.sleep(0.5)
            print("Rolling....")
            time.sleep(0.5)
            print("Rolling....")
            time.sleep(1)

            # Check if the user guessed correctly
            if guess_dice_6 == dice_side_6:
                print("")
                print(f"The dice rolled a {GREEN}{dice_side_6}{RESET}")
                print(f"{GREEN}You have guessed correctly{RESET}")
                bet_amount_dice_6 *= 4
                total_credit += bet_amount_dice_6
                total_credit = round(total_credit)
                print(f"You now have {GREEN}{total_credit}{RESET} total credits!")
            else:
                # User guessed incorrectly
                print(f"The dice rolled a {RED}{dice_side_6}{RESET}")
                print(f"{RED}You have guessed incorrectly.{RESET}")
                print(f"You now have {RED}{total_credit}{RESET} total credit.")

            replay_prompt()

# add rigger
def black_jack():
    clear_screen()
    global total_credit
    global restart_blackjack
    global user_name
    global card_dealt_dealer
    global user_score
    
    
    # Display welcome message for the Black Jack game
    print("")
    print(f"{GREEN}Welcome to Black Jack!{RESET}")
    print("")
    
    while True:
        win = 21  # Define the winning score for Black Jack
        # Deal initial cards to the user and dealer
        card_dealt_user = random.randint(2, 11)
        card_dealt_dealer = random.randint(2, 11)
        total_credit = round(total_credit)
        # Show the current credit of the user
        print("")
        print(f"You currently have {GREEN}{total_credit}{RESET} credits")
        print("")
        time.sleep(0.5)
        
        # Get and validate the bet amount from the user
        while True:
            if total_credit == 0.0:
                print("You thought you could play again?")
                print(f"You have {RED}lost everything,{RESET} sad man sad. ")
                return
            # NEEDS CHECKER
            try:
                bet_amount_blackjack = float((input("How much would you like to bet: ")))
                if bet_amount_blackjack <= 0:
                    print("Invalid input. Please enter a valid bet amount.")
                elif bet_amount_blackjack > total_credit:
                    print("Invalid input. Please enter a valid bet amount.")
                else:
                    break
            except ValueError:
                        print("Enter a valid input")
        time.sleep(0.5)
        print("")
        print(f"You have selected {GREEN}{bet_amount_blackjack}{RESET} to bet")
        total_credit -= bet_amount_blackjack
        print("")
        time.sleep(0.5)

        # Show the initial cards and scores
        user_score = card_dealt_user
        dealer_score = card_dealt_dealer
        print(f"You have been dealt a {CYAN}{user_score}{RESET}.")
        print("")
        time.sleep(0.5)
        print(f"The dealer has been dealt a {RED}{dealer_score}{RESET}")
        
        # Deal additional cards to the user and dealer
        card_dealt_user = random.randint(2, 11)
        card_dealt_dealer = random.randint(2, 11)
        user_score += card_dealt_user
        print("")
        time.sleep(0.5)
        print(f"You have been dealt a {CYAN}{card_dealt_user}{RESET}")
        print("")
        
        # Check if the user has hit blackjack
        if user_score == win:
            print(f"{GREEN}You have hit blackjack, you win!{RESET}")
            bet_amount_blackjack *= 2
            total_credit += bet_amount_blackjack
            total_credit = round(total_credit)
            replay_prompt()
        
        # User's turn to hit or stand
        while True:
            
            if user_score == win:
                print(f"You have dealt a {CYAN}{card_dealt_user}{RESET}")
                print(f"{GREEN}You have won!{RESET}")
                
                bet_amount_blackjack *= 2
                total_credit += bet_amount_blackjack
                print(f"You won {GREEN}{bet_amount_blackjack}{RESET}")
                total_credit = round(total_credit)
                replay_prompt()
            #needs checker
            while True:
                user_input = input(f"You currently have {CYAN}{user_score}{RESET}. Would you like to hit or stand? (h/s): ")
                if user_input not in ["h","s"]:
                    print("Invalid input. Please enter a valid input (h/s)")
                else:
                    break
            if user_input == "h":
                card_dealt_user = random.randint(2, 11)
                new_card_1 = black_jack_rig_user()
                if new_card_1 is not None:
                    card_dealt_user = new_card_1
                user_score += card_dealt_user
                # check if user bust
                if user_score > win:
                    print(f"You have been dealt a {RED}{card_dealt_user}{RESET}")
                    print(f"{RED}You have busted.{RESET}")
                    replay_prompt()
                elif user_score < win:
                    print("")
                    time.sleep(0.5)
                    print(f"You have been dealt a {CYAN}{card_dealt_user}{RESET}")
                    print("")
                    continue
            if user_input == "s":
                while True:
                    # NOT DONE
                    if dealer_score >= 17:
                        print(f"The dealer stands on {RED}{dealer_score}{RESET}")
                        if dealer_score > user_score:
                            print("")
                            print(f"{RED}Dealer wins{RESET}")
                            print("")
                            replay_prompt()
                        elif dealer_score < user_score:
                            bet_amount_blackjack *= 2
                            total_credit += bet_amount_blackjack
                            print(f"You won {GREEN}{bet_amount_blackjack}{RESET}")
                            total_credit = round(total_credit)
                            replay_prompt()
                    elif dealer_score <= 16:
                        card_dealt_dealer = random.randint(2,11)
                        # checking for rig
                        new_card = black_jack_rig_dealer()
                        # if rig sucessful
                        if new_card is not None:
                            card_dealt_dealer = new_card
                        dealer_score += card_dealt_dealer
                        print("")
                        time.sleep(1)
                        print(f"The dealer dealt a {RED}{card_dealt_dealer}{RESET}")
                        print("")
                        time.sleep(1)
                        print(f"The dealer currently has {RED}{dealer_score}{RESET}")
                        print("")
                        # check if dealer score  = 21
                        if dealer_score == win:
                            print("")
                            print(f"{RED}The dealer has reached 21{RESET}")
                            replay_prompt()
                        # check if dealer bust
                        elif dealer_score > win:
                            bet_amount_blackjack *= 2
                            total_credit += bet_amount_blackjack
                            total_credit = round(total_credit)

                            print(f"The dealer has {RED}busted{RESET}")
                            print(f"{GREEN}You have won{RESET}")
                            print(f"You won {GREEN}{bet_amount_blackjack}{RESET}")
                            replay_prompt()
                        # push
                        elif dealer_score ==  user_score:
                            total_credit += bet_amount_blackjack
                            print("You and the dealer have the same score.")
                            print(f"{YELLOW}PUSH{RESET}.")
                            replay_prompt()
# guessing game
# 
#
# add checker for the listed numbers
# add a back out
def  keno():
    clear_screen()
    global total_credit
    print()
    print(f"Welcome to {GREEN}Keno{RESET}")
    print()
    # ask user 

    print(f"To play this game you have to correctly guess {GREEN}7{RESET} numbers out of the range 1-40.")
    print()
    print(f"{YELLOW}Multipliers:{RESET}")
    print(f"{YELLOW}------------{RESET}")
    print(f"{YELLOW}|1: {RESET} {GREEN}2.5x{RESET}{YELLOW}  |{RESET}")
    print(f"{YELLOW}|2: {RESET} {GREEN}5.9x{RESET}{YELLOW}  |{RESET}")
    print(f"{YELLOW}|3: {RESET} {GREEN}8.5x{RESET}{YELLOW}  |{RESET}")
    print(f"{YELLOW}|4: {RESET} {GREEN}20.5x{RESET}{YELLOW} |{RESET}")
    print(f"{YELLOW}|5: {RESET} {GREEN}45x{RESET}{YELLOW}   |{RESET}")
    print(f"{YELLOW}|6: {RESET} {GREEN}95x{RESET}{YELLOW}   |{RESET}")
    print(f"{YELLOW}|7: {RESET} {GREEN}145x{RESET}{YELLOW}  |{RESET}")
    print(f"{YELLOW}------------{RESET}")
    print()
    print(f"You currently have {GREEN}{total_credit}{RESET} credits")
    print("")
    time.sleep(0.5)
    while True:
        try:

            bet_amount_keno = float(input("How much would you like to bet: "))
            print()
            if bet_amount_keno <= 0 or bet_amount_keno > total_credit:
                print("Invalid bet amount.")
            else:
                break
        except ValueError:
                        print("Enter a valid input")

    total_credit -= bet_amount_keno

    winning_numbers = []
    
    
    # used for correctly numbering the number of inputs

    counter = 1
    keno_multiplier = {
        1: {1:2.5},
        2: {1:5.9},
        3: {1:8.5},
        4: {1:20.5},
        5: {1:45},
        6: {1:95},
        7: {1:145},
    }
    
    # prompts user and adds to the list
    # also adds to the winner list
    
    for _ in range(7):
        clear_screen()
        win_num_1 = random.randint(1,40)
        while True:
            if win_num_1 in winning_numbers:
                win_num_1 = random.randint(1,40)
            else:
                break
        winning_numbers.append(win_num_1)
    
    while True:
        checker = False
        user_input = []
        user_input = input(f"Enter {YELLOW}7{RESET} numbers seperated by a space(1/40): ")
        user_input = user_input.split()

        # convert to int
        user_input = [int(x) for x in user_input]
        

        # check if more than 7 nums for less  
        if len(user_input) != 7:
            print("Please enter 7 numbers")
            time.sleep(0.5)
            continue
        
        # supposed to check if numbers above or below 1-40
        # this is wrong use a differnt checker
        if any(x < 1 or x > 40 for x in user_input):
            checker = True
        if checker:
            print("You entered an invalid number please select") 
        else:
            break
        
       
       
    # converts inputs to int
    try:
        user_input = list(map(int, user_input))
    except ValueError:
        print("Please enter valid integers.")

    # sorts both for readability
    winning_numbers.sort()
    user_input.sort()
    
    # compares
    compare = set(winning_numbers) & set(user_input)
    # used for multiplication
    results = len(compare)
   
    # rigger
    if results >= 1:
        compare.pop()
        results = len(compare)
    
    #print(winning_numbers)
    if results >= 1:
        total_multiplier = keno_multiplier[results][1]
        temp_shown_value = total_multiplier * bet_amount_keno
        total_credit += temp_shown_value
        #print(winning_numbers)
        #print(user_numbers)
        time.sleep(0.5)

        print(f"You have correctly guessed {GREEN}{results}{RESET} numbers")
        print()
        print(f"You guessed the numbers {GREEN}{compare}{RESET} correctly.")
        print()
        print(f"You have won {GREEN}{temp_shown_value}{RESET}")
        print()
        replay_prompt()

    elif results == 0:
        winning_numbers = []
        # rigger
        for _ in range(7):
            win_num_1 = random.randint(1,40)
            while True:
                # checks if the same number is already in winning number
                if win_num_1 in winning_numbers:
                    win_num_1 = random.randint(1,40)
                    continue
                # checks if winning number is in user picked numbers
                elif win_num_1 in user_input:
                    win_num_1 = random.randint(1,40)
                    continue
                else:
                    break
            winning_numbers.append(win_num_1)
        time.sleep(0.8)
        print(f"{RED}You did not correctly guess any numbers.{RESET} ")
        #print(winning_numbers)
        #print(user_numbers)
        #time.sleep(3)
        
        
        print(f"The correct numbers were {RED}{winning_numbers}{RESET}")
        replay_prompt()

# make the spin one at a time
def slots():
    clear_screen()
    global total_credit
    total_credit = round(total_credit,2)
    symbols = ["⭐", "🌀", "⚫", "🍏", "🍋", "🍋","✖️"]
    multipliers = {
        '⭐': {1: None, 2: None, 3: 100}, 
        '🌀': {1: None, 2: 5, 3: 10},
        '⚫': {1: None, 2: 3, 3: 7},
        '🍏': {1: None, 2: 2.3, 3: 4},
        '🍋': {1: 0.1, 2: 1.1, 3: 3},
        '✖️': {1: None, 2: None, 3: None}
    }
    def spin_reels():
        #Simulate spinning the slot machine reels
        return [random.choice(symbols) for _ in range(3)]

    def display_reels(reels):
        #Display the reels in a formatted way.
        print(f"| {reels[0]} | {reels[1]} | {reels[2]} |")
    
    def animate_reels():
        start_time = time.time()
        duration = 1.38  # Duration of the animation in seconds
        while time.time() - start_time < duration:
            reels = spin_reels()
            print("\033c", end="")  
            print("=== SLOT MACHINE ===")
            display_reels(reels)
            print("====================")
            time.sleep(0.1)  # Short delay between updates
    

    print("")
    print(f"{GREEN}Welcome to the Slots{RESET}")
    print("")
    print("To play this game enter a bet, then press enter to spin")
    print("")
    print("SYMBOLS || 1 Slot || 2 Slots || 3 Slots ||")
    print("--------||--------||---------||---------||")
    print("✖️ ✖️ ✖️   || ❌ ❌ ❌  || ❌ ❌ ❌   || ❌ ❌ ❌   ||")
    print("⭐ ⭐ ⭐   || ❌ ❌ ❌  || ❌ ❌ ❌   ||   100x  ||")
    print("🌀 🌀 🌀   || ❌ ❌ ❌  ||   5x    ||   10x   ||")
    print("⚫ ⚫ ⚫   || ❌ ❌ ❌  ||   3x    ||   7x    ||")
    print("🍏 🍏 🍏   || ❌ ❌ ❌  ||   2.3x  ||   4x    ||")
    print("🍋 🍋 🍋   ||   .1x  ||   1.1x  ||   3x    ||")
    print("-----------------------------------------")
    print("")

    time.sleep(0.5)
    print(f"You currently have {GREEN}{total_credit}{RESET} credits\n")
    
    while True:
        try:
            bet_amount_slots = float(input("How much would you like to bet: "))
            print()
            if bet_amount_slots <= 0 or bet_amount_slots > total_credit:
                print("Invalid bet amount.")
            else:
                break
        except ValueError:
                        print("Enter a valid input")

    while True:
        user_input = input(f"Press {GREEN}enter{RESET} to spin, {GREEN}b{RESET} to select a new bet, {GREEN}n{RESET} to play a new game (enter/b/n): ")
        if bet_amount_slots > total_credit:
            print("")
            print("Invalid bet amount")
            time.sleep(0.5)
            slots()
            return
        if user_input == "":
            # Animate the spinning effect
            animate_reels()

            # Final result after animation
            final_reels = spin_reels()
            print("\033c", end="")  
            print("=== SLOT MACHINE ===")
            display_reels(final_reels)
            print("====================")

            total_credit -= bet_amount_slots

            # Count symbols and calculate winnings
            results = final_reels
            symbol_count = {symbol: results.count(symbol) for symbol in set(results)}

            checker = False
            temp_result = 0
            result = 0
            win_amount1 = 0
            win_amount2 = 0
            win_amount3 = 0

            for symbol, count in symbol_count.items():
                if count == 3:
                    multiplier = multipliers.get(symbol, {}).get(3)
                    if multiplier is not None:
                        win_amount3 = bet_amount_slots * multiplier
                        print(f"\nWIN! You hit {symbol} three times. You won {win_amount3} credits!")
                        break
                elif count == 2:
                    multiplier = multipliers.get(symbol, {}).get(2)
                    if multiplier is not None:
                        win_amount2 = bet_amount_slots * multiplier
                        print(f"\nYou matched {symbol} on 2 slots. You won {win_amount2} credits!")
                        
                elif count == 1:
                    multiplier = multipliers.get(symbol, {}).get(1)
                    if multiplier is not None:
                        win_amount1 = bet_amount_slots * multiplier
                        temp_result += win_amount1
                        print(f"\nYou matched {symbol} on 1 slot. You won {win_amount1} credits!")
            
            result += round(temp_result,2) + round(win_amount2,2) + round(win_amount3,2)

            # Add the win amount to total credit
            total_credit += result
            total_credit = round(total_credit,1)
            print(f"You now have {GREEN}{total_credit}{RESET} credits")
            if result == 0:
                print("No matching symbols.")

        elif user_input == "b":
            slots()
            return
        elif user_input == "n":
            home()
            return
        else:
            print("You entered something else.")
            
# NEED TO DO
# add counter above board that shows how much they can currently withdraw
# whenever resetting the game all the numbers are still green 
# prolly just reset the colored row or grid

user_input_nums = []
def mines():
    global user_input_nums
    global isbomb_covered
    global total_credit
    global multiplier_selector
    clear_screen()
    print(f"Welcome to {GREEN}Mines{RESET}")
    print()
    print(f"In this game you try to pick the squares that dont have a bomb. {GREEN}Easy{RESET} mode has 1 bomb, {YELLOW}Medium{RESET} has 3, {RED}hard{RESET} mode has 10.")
    # Might change 
    
    
    print()
    print(f"You currently have {GREEN}{total_credit}{RESET}")
    print()
    # Needs checker
    mines_bet_amount = int(input("How much would you like to bet: "))
    total_credit -= mines_bet_amount
    print()
    mines_mode_selector = int(input(f"Enter the difficulty that you would to play. {GREEN}1 {RESET} for Easy, {YELLOW}2 {RESET} Medium, {RED}3{RESET} Hard, {CYAN}0{RESET} to leave."))
    
    # 1 bomb
    # low rig
    easy_multiplier = {
        0: 1,
        1: 1.03,
        2: 1.10,
        3: 1.23,
        4: 1.38,
        5: 1.55,
        6: 1.74,
        7: 1.95,
        8: 2.18,
        9: 2.43,
        10: 2.70,
        11: 3.03,
        12: 3.33,
        13: 3.70,
        14: 4.10,
        15: 4.53,
        16: 5.15,
        17: 6.65,
        18: 7.30,
        19: 8.90,
        20: 10.80,
        21: 13.00,
        22: 15.50,
        23: 18.40,
        24: 21.80,
        25: 25.70
    }

    # 5 bombs
    # mid rig
    normal_multiplier = {
        0: 1,
        1: 1.25,
        2: 1.56,
        3: 1.95,
        4: 2.44,
        5: 3.05,
        6: 3.81,
        7: 4.77,
        8: 5.96,
        9: 7.45,
        10: 9.31,
        11: 11.64,
        12: 14.55,
        13: 18.19,
        14: 20.59, 
        15: 23.29,  
        16: 26.36,  
        17: 29.79,  
        18: 33.71,  
        19: 38.12, 
        20: 43.02, 
    }

    # 12 bombs
    # hard rig
    hard_multiplier = {
        0: 1,
        1: 2.25,
        2: 3.49,
        3: 5.41,
        4: 8.39,
        5: 13.01,
        6: 20.16,
        7: 31.23,
        8: 48.40,
        9: 75.02,
        10: 116.77,
        11: 181.94,
        12: 282.01,
        13: 437.11,
    }
    multiplier_selector = {
        1:easy_multiplier,
        2:normal_multiplier,
        3:hard_multiplier,
    }
    # checks if any bombs are in user input
    # exmaple use
    # print(rig_selector())
    # if rig_selector()
    # sub_game_mine()
    # returns true if rig passes
   
    def rig_selector():
            #4%
        def easy_bomb_rig():
            checker1 = random.randint(1, 5)
            checker2 = random.randint(1, 5)
            return checker1 == checker2
            #2.7%
        def medium_bomb_rig():
            checker1 = random.randint(1, 6)
            checker2 = random.randint(1, 6)
            return checker1 == checker2
            # 6.25%
        def hard_bomb_rig():
            checker1 = random.randint(1, 4)
            checker2 = random.randint(1, 4)
            return checker1 == checker2

        rig_selector_dict = {
            1: easy_bomb_rig,
            2: medium_bomb_rig,
            3: hard_bomb_rig,
        }
        return rig_selector_dict[mines_mode_selector]()
    # make sure it takes into account if the rig returns true.
    # num is not a varible its just used in for loop

    isbomb_covered = True
    def bomb_check(user_input):
        global isbomb_covered
        global colored_row
        global bomb_area
        global grid
        # if bomb hit
        if user_input in bomb_area:
            isbomb_covered = False
            mines_display()   
        else:
            mines_display()
    # need to check if rig worked

    def mines_display():
        global isbomb_covered
        global bomb_area
        global user_input_nums
        global colored_row
        global total_credit
        global multiplier_selector

        grid = [num for num in range(1, 26)]

        clear_screen()

        bomb_uncovered = any(num in user_input_nums for num in bomb_area)

        # Display the grid in 5 rows of 5 numbers each
        for i in range(0, 25, 5): #5 10 15 20 25
            row = grid[i:i+5]
            colored_row = []
            for num in row:
                if num in user_input_nums:
                    if num in bomb_area:
                        if num == bomb_area or not isbomb_covered:
                            # Uncovered bomb (triggering or all bombs revealed)
                            colored_row.append(f"{RED}{str(num).rjust(2)}{RESET}")
                        else:
                            # Previously uncovered bombs
                            colored_row.append(f"{GREEN}{str(num).rjust(2)}{RESET}")
                    else:
                        # Uncovered safe number
                        colored_row.append(f"{GREEN}{str(num).rjust(2)}{RESET}")
                elif not isbomb_covered and num in bomb_area:
                    # Reveal all bombs after one bomb is triggered
                    colored_row.append(f"{RED}{str(num).rjust(2)}{RESET}")
                else:
                    # Not uncovered
                    colored_row.append(str(num).rjust(2))
            print(" | ".join(colored_row))
        # print when bomb is uncovered
        if not isbomb_covered:
            print(f"{RED}BOOM{RESET}")
            colored_row = []
            user_input_nums = []
            replay_prompt()
        # Check for invalid and same number input # 

        total = mines_bet_amount * multiplier_selector[mines_mode_selector][len(user_input_nums)]
        print(f"Current pot: {GREEN}{total}{RESET}")
        while True:
            try:
                user_input = input("Enter the Area you want to uncover (Enter to cash): ")
                if user_input == "":
                    print(f"You cashed out {GREEN}{total}{RESET}")
                    colored_row = []
                    user_input_nums = []
                    total_credit += total
                    replay_prompt()
                elif int (user_input) < 1 or int (user_input) > 25:
                    print("Invalid input. Please enter a number between 1 and 25.")
                elif int (user_input) in user_input_nums:
                    print("You've already uncovered that area. Please try a different one.")
                 # len(user_input_nums)
                else:
                    user_input = int (user_input)
                    user_input_nums.append(user_input)
                    bomb_check(user_input)
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def sub_game_mine():
        global bomb_area
        # 1 bomb
        def easy_mode():
            global total_credit
            global bomb_area
            bomb_area = []
            bomb_area.append(random.randint(1,25)) 
            mines_display()
        # 5 bomb
        def medium_mode():
            global total_credit
            global bomb_area
            bomb_area = []
            while len(bomb_area) != 5:
                temp_value = random.randint(1,25)
                if temp_value not in bomb_area:
                    bomb_area.append(temp_value)
            mines_display()
        # 12 bomb
        def hard_mode():
            global total_credit
            global bomb_area
            bomb_area = []
            while len(bomb_area) != 12:
                temp_value = random.randint(1,25)
                if temp_value not in bomb_area:
                    bomb_area.append(temp_value)
            mines_display()
        difficulty_selector = {
            1:easy_mode,
            2:medium_mode,
            3:hard_mode,
            # 4:home()
        }
        return difficulty_selector[mines_mode_selector]()
    
    sub_game_mine()

def crash():
    clear_screen()
    global total_credit
    global user_name
    global restart_crash
    global crash_win
    global crash_checker
    global banked_value
    
    explode_value = skewed_random(max_value, exponent)

    total_credit = round(total_credit)
    
    print(f"\nWelcome to {GREEN}Crash{RESET}\n")
    print(f"To play this game you have to press enter before the rocketship {RED}CRASHES!!{RESET}\n")
    time.sleep(0.5)
    print(f"You currently have {GREEN}{total_credit}{RESET} credits\n")
    
    while True:
        try:
            bet_amount_crash = float(input("How much would you like to bet: "))
            print()
            if bet_amount_crash <= 0 or bet_amount_crash > total_credit:
                print("Invalid bet amount.")
            else:
                break
        except ValueError:
                        print("Enter a valid input")
    total_credit -= bet_amount_crash
    
    counter = 4
    for _ in range(3):
        clear_screen()
        counter -= 1
        print(f"{YELLOW}{counter}...{RESET}")
        time.sleep(0.5)
        

    clear_screen()
    stop_flag = threading.Event()

    input_thread = threading.Thread(target=user_input_thread, args=(stop_flag,))
    input_thread.start()

    loss = display_exponential_change(max_value, stop_flag)

    input_thread.join()

    if crash_win == True:
        bet_amount_crash *= banked_value
        total_credit += bet_amount_crash
        temp_shown_value = round(bet_amount_crash)
        print("")
        time.sleep(0.5)
        print(f"You cashed out {GREEN}{temp_shown_value}{RESET}")
        print("")

    elif crash_win == False:
        print(f"{RED}You have lost...{RESET}")
        print("")

    while True:
        restart_crash = input("Would you like to play again? (p/n): ")
        if restart_crash.lower() == "p":
            crash_checker = False
            crash_win = False
            crash()
            return
        elif restart_crash.lower() == "n":
            home()
        else:
            print("Please select a valid input (p/b/n)")
# BUG/NEED TO DO
# when number displayed pop that number out of list so its not seen again
# when betting on numbers add checker so they dont enter same number twice.
def roulette():
    clear_screen()
    global first_played
    global total_credit
    global bet_number_roulette

    green_rig_check = False 
    
    counter = 4
    
    print(f"\nWelcome to {GREEN}Roulette{RESET}\n")
    print(f"To play this game bet on ether number and or color; You are able to bet on mutliple numbers or just one number, but you are only allowed to bet on one color.")
    time.sleep(0.5)
    print()
    print(f"         {YELLOW}MULTIPLIERS{RESET}")
    print()
    print(f"| {YELLOW}Amount of numbers{RESET} | {GREEN}Multipliers{RESET} |")
    print("|---------------------------------|")
    print("|         1         |      34x    |")
    print("|         2         |      17x    |")
    print("|         3         |      11x    |")
    print("|         4         |      8x     |")
    print("|         5         |      6x     |")
    print("|         6         |      4x     |")
    print()
    print(f"|       {YELLOW}Color{RESET}       | {GREEN}Multipliers{RESET} |")
    print("|---------------------------------|")
    print("|       Green       |      50x    |")
    print("|       Black       |      2x     |")
    print("|        Red        |      2x     |")
    print()
    print(f"You currently have {GREEN}{total_credit}{RESET} credits\n")

    number_multiplier = {
        1:34,
        2:17,
        3:11,
        4:8,
        5:6,
        6:4
    }
    color_multiplier = {
        "black":2,
        "red":2,
        "green":50,
    }
    
   
    #NEEDS CHECKER and return function
    while True:
        color_bet = False
        number_bet = False
        user_input_color = input(f"Would you like to place a bet on {GREEN}numbers?{RESET} (y/n): ")
        if user_input_color.lower() == "y":
            number_bet = True

        user_input_number = input(f"Would you like to place a bet on a {GREEN}color?{RESET} (y/n): ")
        if user_input_number.lower() == "y":
            color_bet = True
        if user_input_color.lower() not in ["y", "n"] or user_input_number.lower() not in ["y", "n"]:
            print("Enter a valid input.")
        else:
            break
    
    print()
    time.sleep(0.5)
    
    # NEEDS CHECKERS
    # number bet
    if number_bet:
        clear_screen()
        print("Keep in mind you have to place the same amount for each number.")
        while True:
            try:
                user_input_number_amount = int(input(f"How many numbers would you like to bet on {YELLOW}(1-6){RESET}: "))
                if user_input_number_amount <= 0 or user_input_number_amount > 6:
                    print("Invalid number choice.")
                else:
                    break
            except ValueError:
                    print("Enter a valid input")
        numbers_gussed = []
        for i in range(1,user_input_number_amount + 1):
            while True:
                try:
                    numbers_gussed_added = (int(input(f"Which number would you like to bet on {YELLOW}(1-30){RESET}: ")))
                    if numbers_gussed_added <= 0 or numbers_gussed_added > 30:
                        print("Invalid number choice.")
                    else:
                        numbers_gussed.append(numbers_gussed_added)
                        break
                except ValueError:
                    print("Enter a valid input")
            
        numbers_gussed = [str(num).zfill(2) for num in numbers_gussed]  
        temp_shown_value = total_credit / user_input_number_amount
        print(f"The maximum amount you can bet is {GREEN}{temp_shown_value}{RESET}")
        while True:
            try:
                bet_number_roulette = float(input("How much would you like to bet: "))
                if bet_number_roulette <= 0 or bet_number_roulette > temp_shown_value: 
                    print("Invalid number choice.")
                else:
                    break
            except ValueError:
                    print("Enter a valid input")
        
        print()
        number_bet_amount = bet_number_roulette * user_input_number_amount
        total_credit -= number_bet_amount
    # color bet
    # needs a checker for the bet amount for both of the things.
    if color_bet:
        clear_screen()
        # needs checker
        print("You can only bet on one color.")
        while True:
            user_input_color_amount = input(f"What color would you like to bet on({RED}red{RESET}/{BLACK}black{RESET}/{GREEN}green{RESET}): ")
            user_input_color_amount = user_input_color_amount.lower()
            if user_input_color_amount not in ["red","black","green"]:
                print("Invalid input.")
            else:
                break
        if user_input_color_amount == "green":
            green_rig_check == True       
        print(f"The maximum amount you can bet is {GREEN}{total_credit}{RESET}")
        while True:
            try:
                bet_color_roulette = float(input("How much would you like to bet: "))
                if bet_color_roulette <= 0 or bet_color_roulette > total_credit: 
                    print("Invalid number choice.")
                else:
                    break
            except ValueError:
                            print("Enter a valid input")
        total_credit -= bet_color_roulette
            
    if user_input_color == "n" and user_input_number == "n":
        time.sleep(.5)
        print("You have to bet on one of these elements.")
        time.sleep(1)
        roulette()
    
     # Define red and black numbers as two-digit integers
    red_numbers = [str(num).zfill(2) for num in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30]]
    black_numbers = [str(num).zfill(2) for num in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29]]
    green_number = [str(num).zfill(2) for num in [0]]
    # Initial display numbers (6 numbers) in the pattern RED-BLACK-RED-BLACK-RED
    
    for _ in range(3):
        clear_screen()
        counter -= 1
        print(f"{YELLOW}{counter}...{RESET}")
        time.sleep(0.5)
    number_display = []
    while len(number_display) < 5:
        for i in range(5):
            red_num = random.choice(red_numbers)
            black_num = random.choice(black_numbers)
            if len(number_display) < 5:
                if i % 2 == 0:  # Even index - Red
                    number_display.append((red_num, RED))
            if len(number_display) < 5:
                if i % 2 == 1:  # Odd index - Black
                    number_display.append((black_num, BLACK))
            if green_rig_check:
                if random.randint(1,16) == 1:
                    number_display.append((random.choice(green_number), GREEN))  
            elif not green_rig_check:
                if random.randint(1,6) == 1:
                    number_display.append((random.choice(green_number), GREEN))
    number_display = number_display[:5]

    # Roll the numbers 10 times, slowing down each time
    for roll in range(10):
        clear_screen()  # Clear the screen at the beginning of each roll
       

        # Shift numbers to the left
        number_display.pop(0)  # Remove the first element

        # Determine the color for the new number based on the last number's color
        last_color = number_display[-1][1]  # Get the color of the last number
        if last_color == RED:
            new_number = random.choice(black_numbers)
            number_display.append((new_number, BLACK))
        else:
            new_number = random.choice(red_numbers)
            number_display.append((new_number, RED))

        # Print numbers with their original colors
        for number, color in number_display:
            print(f"{color}{number}\033[0m", end=' ')

        # Print the ^ symbol under the winning number index
        winning_index = 2  # Set the winning index (3rd element)
        if roll == 9:
            print()
            print(" " * (winning_index * 3) + "^")
            winning_number = number_display[winning_index][0]
            winning_color = (
                "red" if winning_number in red_numbers
                else "black" if winning_number in black_numbers
                else "green"
            )
            if number_bet:
                if winning_number in numbers_gussed:
                    total_credit += bet_number_roulette * number_multiplier[user_input_number_amount]
                    print(f"\n{GREEN}You correctly guessed the right number.{RESET}")
                else:
                    print(f"\n{RED}You did not correctly guess the right number.{RESET}")
            if color_bet:
                
                if winning_color == user_input_color_amount:
                    total_credit += bet_color_roulette * color_multiplier[user_input_color_amount]
                    print(f"\n{GREEN}You correctly guessed the right color.{RESET}")
                else:
                    print(f"\n{RED}You did not correctly guess the right color.{RESET}")
            print(f"You now have {GREEN}{total_credit}{RESET}")
            replay_prompt()
        
        print()  # New line after printing numbers
        print(" " * (winning_index * 3) + "^")  # Adjust spacing based on index

        # Gradually increase sleep time
        time.sleep(0.5 + roll * 0.1)  # Start at 0.5s and add 0.1s for each roll


level = 1

# NEED TO DO
# Current thing I want to do is too add the path of bombs if one were too hit the bomb
# add a checker if they insta crash without picking a level
def tower():
    global total_credit
    global level
    clear_screen()
    total_credit = round(total_credit,2)
    tower_layout = [[0, 0, 0] for _ in range(7)]

    def bomb_check():
        global level
        if sub_tower_game == 0:   
            if bomb_area == user_input:
                #level = 1
                tower_layout[level-1][bomb_area-1] = 1
                display_tower()
                print(f"{RED}BOOM!{RESET} You hit the wrong area.")
                level = 1
                replay_prompt()
            else:
                level += 1
        elif sub_tower_game == 1:
            if bomb_area_1 == user_input or bomb_area_2 == user_input:
                tower_layout[level-1][bomb_area_1-1] = 1
                tower_layout[level-1][bomb_area_2-1] = 1
                display_tower()
                #level = 1
                print(f"{RED}BOOM!{RESET} You hit the wrong area.")
                level = 1
                replay_prompt()
            else:
                level += 1

              
          # Move to the next level
        display_tower()

    
    
    levels_easy_multiplier = {
        1: {1: 1.424},
        2: {1: 2.025},
        3: {1: 2.82},
        4: {1: 4.03},
        5: {1: 5.89},
        6: {1: 7.985},
        7: {1: 11.125},
    }
    levels_hard_multiplier = {
        1: {1: 3.09},
        2: {1: 4.044},
        3: {1: 5.85},
        4: {1: 7.89},
        5: {1: 9.945},
        6: {1: 13.25},
        7: {1: 15.65},
    }

    
    print(f"\nWelcome to {GREEN}Tower{RESET}\n")
    print(f"To play the game your objective is to make it to the top of the tower without hitting the wrong area.")
    print()
    time.sleep(0.2)
    print(f"You currently have {GREEN}{total_credit}{RESET} credits\n")

    win_level = 7  # Set the maximum level based on the new dictionary

    while True:
        try:
            bet_amount_tower = float(input("How much would you like to bet: "))
            rig_checker = False
            rig_amount = total_credit * .8
            if bet_amount_tower >= rig_amount:
                rig_checker = True
            print()
            if bet_amount_tower <= 0 or bet_amount_tower > total_credit:
                print("Invalid bet amount.")
            else:
                break
        except ValueError:
                        print("Enter a valid input")
    
    
    
    sub_tower_game = int(input(f"Enter {GREEN}0{RESET} for easy mode, {GREEN}1{RESET} for hard mode, {RED}2{RESET} to leave. "))
    if sub_tower_game == 2:
        home()
        return
    else:
        total_credit -= bet_amount_tower
    clear_screen()
    
    
    def display_tower():
        global level
        
        clear_screen()
        print("\nTower:")
        for i in range(win_level, 0, -1):  
            
            if i <= level:
                if sub_tower_game == 0:
                # Calculate the product of the multiplier and the bet amount
                    product = levels_easy_multiplier[i][1] * bet_amount_tower
                    platform_char = f"{product:.2f}"
                elif sub_tower_game == 1:
                    product = levels_hard_multiplier[i][1] * bet_amount_tower
                    platform_char = f"{product:.2f}"
                
            else:
                platform_char = ' '

            print(f"  {detect_color_tower(tower_layout[i-1][0])}{platform_char}   {detect_color_tower(tower_layout[i-1][1])}{platform_char}   {detect_color_tower(tower_layout[i-1][2])}{platform_char}{RESET}")  # the platforms
            
        print("")
        
          
    display_tower()
    # easy mode
    if sub_tower_game == 0:
        level = 1  
        while level <= win_level:
            user_input = int(input("What platform (1, 2, or 3): Enter 0 to cash: "))
            if user_input == 0:
                level -= 1
                product = levels_easy_multiplier[level][1] * bet_amount_tower
                total_credit += product
                print(f"You have cashed out {GREEN}{product}{RESET}")
                print()
                print(f"You currently have {GREEN}{total_credit}{RESET} total credits.")
                level = 1
                replay_prompt()
            
            bomb_area = random.randint(1, 3)  # Bomb placement on a platform
            tower_layout[level-1][bomb_area-1] = 1
            tower_layout[level-1][user_input-1] = 2
            if rig_checker:
                rig_num1 = random.randint(1,2)
                rig_num2 = random.randint(1,2)
                if rig_num1 == rig_num2:
                    bomb_area = user_input


            bomb_check()

        if level == win_level + 1:
            level -= 1
            product = levels_easy_multiplier[level][1] * bet_amount_tower
            total_credit += product
            print(f"You have cashed out {GREEN}{product}{RESET}")
            print()
            print(f"You currently have {GREEN}{total_credit}{RESET} total credits.")
            level = 1
            replay_prompt()
    # hard mode
    elif sub_tower_game == 1:   
        level = 1  
        while level <= win_level:
            bomb_area_list = [1,2,3]
            
            user_input = int(input("What platform (1, 2, or 3): Enter 0 to cash: "))
            if user_input == 0:
                level -= 1
                product = levels_hard_multiplier[level][1] * bet_amount_tower
                total_credit += product
                print(f"You have cashed out {GREEN}{product}{RESET}")
                print()
                print(f"You currently have {GREEN}{total_credit}{RESET} total credits.")
                level = 1
                replay_prompt()
            
            bomb_area_1 = random.choice(bomb_area_list)  # Bomb placement on a platform
            bomb_area_list.remove(bomb_area_1)
            bomb_area_2 = random.choice(bomb_area_list)
            

            tower_layout[level-1][bomb_area_1-1] = 1
            tower_layout[level-1][bomb_area_2-1] = 1
            tower_layout[level-1][user_input-1] = 2

            # rig 25%
            if rig_checker:
                rig_num1 = random.randint(1,2)
                rig_num2 = random.randint(1,2,3)
                if rig_num1 == rig_num2:
                    bomb_area = user_input
            
            bomb_check()

        if level == win_level + 1:
            level -= 1
            product = levels_hard_multiplier[level][1] * bet_amount_tower
            total_credit += product
            print(f"You have cashed out {product}")
            print()
            print(f"You currently have {total_credit} total credits.")
            level = 1
            replay_prompt()
# distionary of games
game_functions = {
    0: bank,
    1: dice_game,
    2: black_jack,
    3: keno,
    4: slots,
    5: mines,
    6: crash,
    7: roulette,
    8: tower,
}

def generate_leaderboard(csv_file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Check if the necessary columns exist
    if 'name' not in df.columns or 'credits' not in df.columns:
        raise ValueError("The CSV file must contain 'name' and 'credits' columns.")
    
    # Extract the relevant columns
    df = df[['name', 'credits']]
    
    # Ensure that 'credits' is numeric and handle any non-numeric values
    df['credits'] = pd.to_numeric(df['credits'], errors='coerce').fillna(0)
    
    # Sort the DataFrame by the 'credits' column in descending order
    df_sorted = df.sort_values(by='credits', ascending=False)
    
    # Select the top 10 entries
    top_entries = df_sorted.head(10)
    
    # Convert the top entries to a list of tuples
    entries = list(top_entries.itertuples(index=False, name=None))
    
    # Format the entries with colors and numbering
    formatted_leaderboard = format_entries_with_colors(entries)
    
    return formatted_leaderboard

def format_entries_with_colors(entries):
    # Convert each tuple into "rank. name,credits" format with color for the top three ranks
    formatted_entries = []
    for rank, (name, credits) in enumerate(entries, start=1):
        # Determine color based on rank
        if rank == 1:
            color = YELLOW
        elif rank == 2:
            color = BLUE
        elif rank == 3:
            color = BROWN
        else:
            color = RESET
        
        # Format the string with color and include rank
        formatted_entries.append(f"{color}{rank}. {name}, {credits}{RESET}")
    
    # Join all formatted entries with newline characters
    return "\n".join(formatted_entries)

def home():
    clear_screen()
    global user_name
    global names_and_credits
    global name_given
    global total_credit
    global game_selection
    global total_credit
    csv_file_path = 'bank.csv'
    print(f"{RED}Leaderboard of Fame{RESET}")
    #print(f"{RED}-------------------{RESET}")
    print(generate_leaderboard(csv_file_path))
    # Display the menu
    print("")
    print(f"Welcome to the {RED}Den of Ephemeral games{RESET}")
    print("Here is the selection of games")
    if name_given == True:
        total_credit = round(total_credit,2)
        print(f"You currently have {GREEN}{total_credit}{RESET} total CREDITS.")        
    print("")
    print(f"Bank:{GREEN}'0'{RESET}")
    print(f"Dice roller: {GREEN}'1'{RESET}")
    print(f"Black jack: {GREEN}'2'{RESET}")
    print(f"Keno: {GREEN}'3'{RESET}")
    print(f"Slots: {GREEN}'4'{RESET}")
    print(f"Mines: {GREEN}'5'{RESET}")
    print(f"Crash: {GREEN}'6'{RESET}")
    print(f"Roulette: {GREEN}'7'{RESET}")
    print(f"Tower: {GREEN}'8'{RESET}")

    if not name_given:
        total_credit = 0
        names_and_credits = extract_name_and_credits("bank.csv","")
        user_name = input("Enter your name: ")
        result = extract_name_and_credits("bank.csv", user_name)
        if result is True:
            total_credit = 0
            checker123 = True
        else:
            checker123 = False
            total_credit = 25
        name_given = True
    
    while True:
            try:
                game_selection = int(input("Which game would you like to play (type in the number next to the word): "))
            
            # Check if the selected game is valid

                if game_selection not in [game_functions]:
                    print("Please select a valid number.")

                if game_selection in game_functions:

                    if game_selection == 0:
                        game_functions[game_selection]()
                        break
                    elif total_credit == 0:
                        print("You have zero credits You are not allowed to play, you are going to the bank")
                        time.sleep(1)
                        save_variables(user_name)

                    # Call the appropriate game function   
                    game_functions[game_selection]()
                    return
                else:
                    print("Invalid selection. Please enter a number between 0 and 8.")
            except ValueError:
                print("Please enter a number")
                
                
user_name = ""   
names_and_credits = {}
names_and_profit_loss = {}
names_and_profit_loss_1 = {}
name_given = False
home()

##NEED
#TO
#DO
# bottle flip game
# add game hilo game where you guess higher or lower cards
# add blackjack sidebet if blackjack deals ace 
# blackjack ace situation bc double 11 == 22
# for all games add if statement for if 0 creds they got bank()
# want to add a results graph and total carrer where they can see the number of bets
# number of bet won etc
# global chat box with website
# carrer with total net profit
# all bets won
# all bets placed
# tower shows rest of path of bombs
# replace play again prompt get rid of option to go to bank
# possibly add a function for game over could use the game selcetion for the replay
# add a player vs player game
# in hmtl make it visual 
