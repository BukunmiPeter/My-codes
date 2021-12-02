#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Part #1
- Create a board for tic tac toe that looks something like this
 x| |
  |o|
  | |x

(Hint: you can use "\n" to print on a new line )

- User can enter a space between 1-9 and an x will appear in that spot
- User can then do the same and an 0 will appear 
-----------------------------------------------------------------------
board = [" "]*9
def draw_board(board):
    row_1 = "{}|{}|{}".format(board[0], board[1], board[2])
    row_2 = "{}|{}|{}".format(board[3], board[4], board[5])
    row_3 = "{}|{}|{}".format(board[6], board[7], board[8])

    print(row_1 + "\n" + row_2 + "\n" + row_3)
draw_board(board) 
while 1==1:
    x_user = int(input("Choose your space between 1-9"))
    x_user -=1   
    board[x_user]= "x"
    draw_board(board)   
    o_user = int(input("Choose your space between 1-9"))
    o_user -=1   
    board[o_user]= "o"
    draw_board(board)  

------------------------------------------------------------------
==================================================================
Part #2
- If User tries to enter a space that is already taken, they are not allowed and have to try again
- If user gets three in a row, game ends and the winner is announced

-------------------------------------------------------------------------------------------
board = [" "]*9
def draw_board(board):
    row_1 = "{}|{}|{}".format(board[0], board[1], board[2])
    row_2 = "{}|{}|{}".format(board[3], board[4], board[5])
    row_3 = "{}|{}|{}".format(board[6], board[7], board[8])

    print(row_1 + "\n" + row_2 + "\n" + row_3)
    def user_move(board, user_type):
    user_choice = int(input("Choose your space between 1-9"))- 1
    if board[user_choice] !=" ":
        print("Space is taken. Try again")
        user_move(board,user_type)
    else:
        board[user_choice]= user_type
    
    def check_win(board, x_o):
    if board[0] == x_o and board[1] == x_o and board[2] == x_o or board[3] == x_o and board[4] == x_o and board[5] == x_o or board[6] == x_o and board[7] == x_o and board[8] ==x_o  or board[0] == x_o and board[3] == x_o and board[6] ==x_o or board[1] == x_o and board[4]== x_o and board[7] == x_or or board[0] == x_o and board[4] == x_o and board[8] ==x_o  or board[2] == x_o and board[4] == x_o and board[6] == x_o:
        play= False
    else:
        play= True
    return play
    
    board = [" "]*9
draw_board(board) 
play = True
while play ==True:
    user_move(board, "x")
    play = check_win(board, "x")
    if play== False:
        continue
    draw_board(board)   
    user_move(board, "o")
    play= check_win(board, "o")
    draw_board(board)
print("End of the game")
==================================================================

Part #3
- User can choose whether to play with a friend (using the same keyboard) or against the computer 
- Design the computer to make its own moves.






"""


# In[4]:


#a = "x |  | \n |o | \n |  |x"



# In[1]:


board = [" "]*9


# In[2]:


def draw_board(board):
    row_1 = "{}|{}|{}".format(board[0], board[1], board[2])
    row_2 = "{}|{}|{}".format(board[3], board[4], board[5])
    row_3 = "{}|{}|{}".format(board[6], board[7], board[8])

    print(row_1 + "\n" + row_2 + "\n" + row_3)


# In[3]:


def user_move(board, user_type):
    user_choice = int(input("Choose your space between 1-9"))- 1
    if board[user_choice] !=" ":
        print("Space is taken. Try again")
        user_move(board,user_type)
    else:
        board[user_choice]= user_type
        available_spaces.remove(user_choice)


# In[4]:


def comp_move(board,user_type):
    computer_choice = random.choice(available_spaces)
    board[computer_choice] = user_type
    available_spaces.remove(computer_choice)


# In[5]:


def check_win(board, x_o):
    if board[0] == x_o and board[1] == x_o and board[2] == x_o or board[3] == x_o and board[4] == x_o and board[5] == x_o or board[6] == x_o and board[7] == x_o and board[8] ==x_o  or board[0] == x_o and board[3] == x_o and board[6] ==x_o or board[1] == x_o and board[4]== x_o and board[7] == x_or or board[0] == x_o and board[4] == x_o and board[8] ==x_o  or board[2] == x_o and board[4] == x_o and board[6] == x_o:
        play= False
        print("Hooray! {} has won.". format(x_o))
    else:
        play= True
    return play


# In[6]:


import random
board = [" "]*9
available_spaces = [0,1,2,3,4,5,6,7,8]
draw_board(board) 
play = True
comp_or_friend = input("Would you like to play against a computer of friend?(c or f)")
while play ==True:
    
    user_move(board, "x")
    play = check_win(board, "x")
    if play== False:
        continue
    draw_board(board) 
    if comp_or_friend == "f":
        user_move(board, "o")
    elif comp_or_friend == "c":
        comp_move(board,"o")
    play= check_win(board, "o")
    draw_board(board)
print("End of the game")


# In[ ]:





# In[ ]:




