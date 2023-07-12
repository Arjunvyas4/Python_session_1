#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def input_function():
    user_input = input("rock  paper  scissors")
    return user_input.lower()


# In[6]:


def random_select():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice


# In[3]:


def winner_function(user_input, computer_choice):
    if user_input == computer_choice:
        return "It's a tie!"
    elif user_input == 'rock':
        if computer_choice == 'scissors':
            return "You win!"
        else:
            return "Computer wins!"
    elif user_input == 'paper':
        if computer_choice == 'rock':
            return "You win!"
        else:
            return "Computer wins!"
    elif user_input == 'scissors':
        if computer_choice == 'paper':
            return "You win!"
        else:
            return "Computer wins!"
    else:
        return "Invalid input! You entered an incorrect choice."


# In[4]:


def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == 'yes'


# In[7]:


def main():
    print("Welcome to Rock, Paper, Scissors!")

    play_game = True

    while play_game:
        user_input = input_function()
        computer_choice = random_select()

        print("Your choice:", user_input)
        print("Computer's choice:", computer_choice)

        result = winner_function(user_input, computer_choice)
        print(result)

        play_game = play_again()

    print("Thank you for playing!")

if __name__ == '__main__':
    main()


# In[ ]:




