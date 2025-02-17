# # Lesson 5 - Introduction to For Loop and range()
# space=(" ")
# # ## Recap 1: Automated Birthday Invitation

# # You run a small business that creates personalized digital
# # birthday invitation cards. To automate the process, you decide
# # to write a Python program. 

# # This program should ask the user for:
# # 1. birthday person's name
# # 2. the age that they are turning that year
# # 3. personal message from the sender

# # Finally, the program prints out a personalized invitation
# # message.

# # ### Sample output:
# # "Happy th birthday ! "

# # ---------------------------------------------------------------

# # ## Task 1: Name Cheer

# # Your school's Sports Day is coming up and you are coding a
# # program to cheer your schoolmates up.

# # Your program needs to:
# # 1. Using input(), ask the user for their namee e.g. 
# # 2. Print a cheer as shown below:
   
# #     ### Example:
# #     What is your name? [Input: "Dave"]
# #     Give me a D!
# #     Give me a a!
# #     Give me a v!
# #     Give me a e!
# #     What do we have?
# #     Dave is the best!

# # Note:
# #     Notice how "Give me a..." is repeated!
# #     Which function should you be using?

# # ---------------------------------------------------------------

# # ## Task 2: Repeated Sentence Loop

# # Print the sentence "I like chicken rice." 100 times using the
# # 'for' loop

# # ---------------------------------------------------------------

# # ## Task 3: Sentence Repetition Loop with Order of Code
# # ##         Sequence

# # Using the 'for' loop, print the following sentences sequence
# # 100 times:
# # "I like cake."
# # "Give me more"

# # ---------------------------------------------------------------

# # ## Task 4: range(stop)

# # Using the 'for' loop, print the numbers from 0 - 59

# # Question:
# # How many numbers are printed? 

# # ---------------------------------------------------------------

# # ## Task 5: range(start, stop)

# # **Task 5a**:
# # Print numbers from 1 to 5 using a 'for' loop.

# # **Task 5b**:
# # Print numbers from 51 to 100 using a 'for' loop.

# # **Task 5c**:
# # Print numbers from 18 to 29 using a 'for' loop.

# # ---------------------------------------------------------------

# # ## Task 6: range(start, stop, step)

# # **Task 6a**:
# # Use a 'for' loop to print numbers from 2 to 24 in multiples of 2.

# # **Task 6b**:
# # Use a 'for' loop to print numbers from 8 to 96 in multiples of 8.

# # **Task 6c**:
# # Use a 'for' loop to print numbers from 5 to 1 in descending order.

# # ---------------------------------------------------------------

# # ## Task 7: Countdown timer

# # **Task 7a**:
# # Imagine you are the race official and to start the race, you
# # must say the following:

# #     Ready!
# #     3
# #     2
# #     1

# # Using a 'for' loop, recreate the above sequence.

# # **Task 7b**:
# # Create a countdown timer that counts from 10 to 1.
# # When the timer hits 1, print "Boo!"

# # ---------------------------------------------------------------

# # ## Task 8: User-Defined Range Counter

# # Using input(), ask the user for 2 numbers and store them in the
# # variables:
# # 1. start
# # 2. stop

# # Write a 'for' loop to count from **start** to **stop**

# # Note:
# # What happens if the user inputs a higher start number than stop?
# # Modify your code to be able to handle that scenario.

# # ---------------------------------------------------------------

# # ## Task 9: Accumulative Sum in Loop

# # 1. Create a variable 'num' and assign the integer "0" to it
# # 2. Create a 'for' loop that repeats 10 times
# # 3. Add the sum of 'num' and the loop's parameter and print out
# #    the value.
# # 4. Observe what happens.

# # Example:
# # 1st iteration
# #     num = num + i
# #     print(num)

# # 2nd iteration
# #     num = num + i
# #     print(num)

# # ...

# # 10th iteration
# #     num = num + i
# #     print(num)

# # Output:
# #     0
# #     1
# #     3
# #     6
# #     10
# #     15
# #     21
# #     28
# #     36
# #     45
# # fname=input("your first name")
# # lname=input("your last name")
# # print(fname+space+lname)
# # age=input("what is your age?")
# # name=input("wat is your name?")
# # print("user"+space+name+space+"is"+space+age+space+"years old")


# # Get input from the user
# # age = input("Enter the age they are turning this year: ")
# # name = input("Enter the name of the birthday person: ")
# # message = input("Enter your personal message for them: ")

# # # Construct the birthday message without the brackets
# # birthday_message = f"happy {age}th birthday {name}! {message}"

# # # Print out the final message
# # print("\nHere is your birthday message:\n")
# # print(birthday_message)
# # Get the user's age
# # age = int(input("Enter your age: "))

# # # Check if the age is above 21
# # if age > 21:
# #     print("You are okay.")
# # else:
# #     print("No.")
# import os
# import random
# import time
# import sys

# # Game settings
# SCREEN_WIDTH = 30
# SCREEN_HEIGHT = 10
# PIPE_WIDTH = 5
# BIRD_CHAR = "O"
# PIPE_CHAR = "#"
# BACKGROUND_CHAR = "."

# # Initialize the game state
# bird_pos = SCREEN_HEIGHT // 2  # Bird starts in the middle
# bird_velocity = 0
# gravity = 1
# jump_strength = -2
# pipe_gap = 3
# pipe_x = SCREEN_WIDTH
# score = 0
# game_over = False

# def clear_screen():
#     """Clears the console screen"""
#     os.system('cls' if os.name == 'nt' else 'clear')

# def draw_screen():
#     """Draws the game screen"""
#     global bird_pos, pipe_x, pipe_gap

#     # Create the game screen as a list of lists
#     screen = [[BACKGROUND_CHAR] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]

#     # Draw the bird
#     screen[bird_pos][2] = BIRD_CHAR

#     # Draw pipes
#     pipe_top = random.randint(1, SCREEN_HEIGHT - pipe_gap - 1)
#     for y in range(SCREEN_HEIGHT):
#         if y < pipe_top or y >= pipe_top + pipe_gap:
#             if pipe_x < SCREEN_WIDTH:
#                 screen[y][pipe_x] = PIPE_CHAR

#     # Print the screen
#     for row in screen:
#         print("".join(row))

#     print(f"Score: {score}")

# def update_game():
#     """Update the game state, including bird movement and pipe movement"""
#     global bird_pos, bird_velocity, pipe_x, score, game_over

#     # Bird gravity and movement
#     bird_velocity += gravity
#     bird_pos += bird_velocity

#     # Prevent bird from going out of bounds (top/bottom of screen)
#     if bird_pos < 0:
#         bird_pos = 0
#         bird_velocity = 0
#     if bird_pos >= SCREEN_HEIGHT:
#         bird_pos = SCREEN_HEIGHT - 1
#         bird_velocity = 0

#     # Move the pipe to the left
#     pipe_x -= 1
#     if pipe_x < 0:
#         pipe_x = SCREEN_WIDTH
#         score += 1  # Increase score when pipe goes off screen

#     # Check for collision
#     pipe_top = random.randint(1, SCREEN_HEIGHT - pipe_gap - 1)
#     for y in range(SCREEN_HEIGHT):
#         if pipe_x == 2 and (y < pipe_top or y >= pipe_top + pipe_gap):
#             if y == bird_pos:
#                 game_over = True

# def game_loop():
#     """Runs the main game loop"""
#     global game_over

#     while not game_over:
#         clear_screen()
#         draw_screen()

#         # Get user input (check for spacebar or Enter key)
#         input_key = input("Press Enter to Jump (or q to quit): ")
#         if input_key.lower() == "q":
#             break
#         if input_key == "":
#             bird_velocity = jump_strength  # Make the bird jump

#         # Update the game
#         update_game()

#         # Delay to control game speed
#         time.sleep(0.1)

#     print("\nGame Over!")
#     print(f"Final Score: {score}")

# # Start the game
# if __name__ == "__main__":qwerty

#     game_loop()   


# for count in range(10000):
#     print("I will buy pizza")

# name=input("what is your name")
# for abc in name:
#     print("give me a "+abc)

# print("what do we have")
# # print(name+" is the best")
# for task in range(100):
#     print("I like air")
#     print("give me more")
# for number in range(457):
#     print(number)

# for number in range(457):
#      print(number)
# for number in range(457):
#          print(number)
# for number in range(457):
#              print(number)
# for number in range (51,101):
#      print(number)
# for number in range (step,2):
#      print (number)
# # Task 6: range(start, stop, step)

# **Task 6a**:
# Use a 'for' loop to print numbers from 2 to 24 in multiples of 2.
# for num in range(2,25,2):
#     print(num)
# **Task 6b**:
# Use a 'for' loop to print numbers from 8 to 96 in multiples of 8.
# for num in range(8,97,8):
#     print(num)
# **Task 6c**:
# Use a 'for' loop to print numbers from 5 to 1 in descending order.
# for num in range (10,0,1):
#     print(num)
# a=input("start")
# a=int(a)
# b=input("stop")
b=int(input("how many students do you have?"))
for q in range(b):
    score=int(input("how much does this sutudent have?"))
    sumscore=sumscore+score
print ()




















































