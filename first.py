# print("hello ")
name = "isha"
roll_number = 102
percentage = 89.5

is_student = True
# print("name:",name ,"roll_number:",roll_number,"percentage:",percentage,"is_student:",is_student,sep="-")

# print(type(name)) #str
# print(type(roll_number))# integer
# print(type(percentage ))  #float
# print(type(is_student)) #boolean

# n1 = int(input("Enter n1: "))
# n2 = int(input("Enter n2: "))
# print("sum of n1 and n2 is :",n1+n2)

#program volume of sphere
# r  =  float(input("Enter thr radius in cm : "))
# volume = (4/3)*3.14 *(r**3)
# # print("Volume of sphere is :", volume ,"cm^3")

a = 5
b=3
c = 4
a= str(a)
b=  str(b)
c = str(c)
# print("valuesof a , b and c is as a string :", str(a)+ str(b)+str(c))

#convert temprecture into faharenheit
# temp = float(input("Enter temperature in celsius : "))
# f = (temp *9/50) +32
# print("temperature in faharenheit is :",f,"°f")
###
     ###tic toa gqme

####





# from random import randrange


# def display_board(board):
# 	print("+-------" * 3,"+", sep="")
# 	for row in range(3):
# 		print("|       " * 3,"|", sep="")
# 		for col in range(3):
# 			print("|   " + str(board[row][col]) + "   ", end="")
# 		print("|")
# 		print("|       " * 3,"|",sep="")
# 		print("+-------" * 3,"+",sep="")


# def enter_move(board):
# 	ok = False	# fake assumption - we need it to enter the loop
# 	while not ok:
# 		move = input("Enter your move: ") 
# 		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
# 		if not ok:
# 			print("Bad move - repeat your input!") # no, it isn't - do the input again
# 			continue
# 		move = int(move) - 1 	# cell's number from 0 to 8
# 		row = move // 3 	# cell's row
# 		col = move % 3		# cell's column
# 		sign = board[row][col]	# check the selected square
# 		ok = sign not in ['O','X'] 
# 		if not ok:	# it's occupied - to the input again
# 			print("Field already occupied - repeat your input!")
# 			continue
# 	board[row][col] = 'O' 	# set '0' at the selected square


# def make_list_of_free_fields(board):
# 	free = []	
# 	for row in range(3): # iterate through rows
# 		for col in range(3): # iterate through columns
# 			if board[row][col] not in ['O','X']: # is the cell free?
# 				free.append((row,col)) # yes, it is - append new tuple to the list
# 	return free


# def victory_for(board,sgn):
# 	if sgn == "X":	# are we looking for X?
# 		who = 'me'	# yes - it's computer's side
# 	elif sgn == "O": # ... or for O?
# 		who = 'you'	# yes - it's our side
# 	else:
# 		who = None	# we should not fall here!
# 	cross1 = cross2 = True  # for diagonals
# 	for rc in range(3):
# 		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
# 			return who
# 		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
# 			return who
# 		if board[rc][rc] != sgn: # check 1st diagonal
# 			cross1 = False
# 		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
# 			cross2 = False
# 	if cross1 or cross2:
# 		return who
# 	return None


# def draw_move(board):
# 	free = make_list_of_free_fields(board) # make a list of free fields
# 	cnt = len(free)
# 	if cnt > 0:	
# 		this = randrange(cnt)
# 		row, col = free[this]
# 		board[row][col] = 'X'


# board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
# board[1][1] = 'X' # set first 'X' in the middle
# free = make_list_of_free_fields(board)
# human_turn = True # which turn is it now?
# while len(free):
# 	display_board(board)
# 	if human_turn:
# 		enter_move(board)
# 		victor = victory_for(board,'O')
# 	else:	
# 		draw_move(board)
# 		victor = victory_for(board,'X')
# 	if victor != None:
# 		break
# 	human_turn = not human_turn		
# 	free = make_list_of_free_fields(board)

# display_board(board)
# if victor == 'you':
# 	print("You won!")
# elif victor == 'me':
# 	print("I won")
# else:
# 	print("Tie!")

# write the numbers like 1,000 insted of 1000 
# x= float(input("Enter x:"))
# y= float(input("Enter y:"))

# z = round(x + y)
# print(f"{z:,}")

# round of number by using round function  and formatiing string
# by round function
x = 2
y = 3
z = round(x/y,2)
# print("z is:",z)

#  by formting string
x = 2
y = 3
z = 2/3
# print(f"{z:.2f}") 

# def greet(name ="stranger"):
#     print(f"hello! {name}")
    
    
# name = input("Enter your name:")
# greet(name)

###top to bottom approach

# def main():
#     n = int (input("Enter n : "))
#     # print_column(n)
#     # print_row(n)
#     print_square(n)

# def print_square(size):
#     for i in range(size):
#         print("🟥" * size)
        

# #     # for _ in range(height):
# #     #     print("#")\
# #     print("#\n"* height, end="")

# main()

# try:
#     n = int(input("Enter a number:"))
#     print(f"n is {n}")
# except ValueError:
#     print("oh😒! Invlaid number.")

# import random
#     # suffle cards by using random module
# cards = ["jack","queen","king","ace"] 
# random.shuffle(cards)
# for card in cards:
#     # print(f" {card}") 
 


import statistics
data = [88,100]
# print(statistics.median(data))

# important(take input without any prompt)
import sys
# print("hello, my name is", sys.argv[1])




import cowsay
import sys
# if len(sys.argv) ==2:
#     cowsay.trex("hello, " + sys.argv[1])



# birth_year = int(input("Enter your birth year: "))
# # color = input("Enter your favorite color: ")
# # print(f"{name} likes {color}")
# age = 2026 -birth_year
# print(f"you are {age} years old.")

#  covert pounds into kilograms
# weight_in_pounds = float(input('enter your weight in pounds: '))
# weight_in_kg = weight_in_pounds * 0.453592
# print(f"your weight in kilograms is {weight_in_kg:.2f} kg")

# convert kilogram into pounds
# weight_in_kg = float(input("ENter yor weight in kilogram: "))
# weight_in_pounds = weight_in_kg / 0.453592
# print(f"your weight in pounds is {weight_in_pounds:.2f} lbs.")

# course = "ayushi"
# print(course[:])
name  = "jennifer"
# print(name[-1: 3:-1])

first_name = "john smith"
# print(f"{first_name}  is a coder.")
# print(len(first_name ))
# first_name = first_name.upper()
# print(first_name)
# first_name = first_name.lower()
# print(first_name)
# first_name = first_name.title()
# print(first_name)
# first_name = first_name.capitalize()
# print(first_name)
# new_name = first_name.replace("John","ayushi")
# print(new_name)

# print((10+ 3)*2)
import  math
x = -2.9
# print(round(x))
# print(abs(x)) # gives absollute value and always retuen poisitive value
# print(math.ceil(x))
# print(math.floor(2.5))


# house_price = 1000000
# good_credit = False
# if good_credit:
#     down_payment = (0.1)*house_price
# else:
#     down_payment = (0.2)*house_price
# print(f"Down payment is : ${ down_payment}")

# temperature = 30
# if temperature >=30:
#     print("It's a hot day🥵.")
# elif temperature<10:
#     print("It's a cold day🥶.")
# else:
#     print("It neither a cold or nor a hot day😊.")
# name = "ayu"
# name_len  = len(name)
# if name_len <3:
#     print("Name must be at least 3 characters.")
# elif name_len > 50:
#     print("Name can be a maximum of 50 characters.")
# else:
#     print("name looks good!")

# weight = float(input("What's your weight? "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper()=="L":
#     print(f"your weight is {weight*0.454:.2f} kg.")
# else:
#     print(f"your weight is {weight/0.454 :.2f} lbs.")


# minor project to guess a number between 1 to 9 in 3 attmepts
# i = 0
# guess = 9
# while i<3:
    
#     user_guess= int(input("Guess a number between 1 to 9: "))


#     if user_guess ==  guess:
#         print("you won😍!")
#         break
#     i +=1
# else:
#     print("oh no!, you lost😔")    


# minor project to create a car game

# start = False

# while True:
#      command = input(">")
#      if command.lower() == 'start':
     
#           if start:
#                print("car is already started.....")
#           else:
#                print("car started...🚗")
#                start = True

#      elif command.lower() == 'stop':
#           if not start:
#                print("car is already stopped....")
#           else:
#                print(" car stopped🛑.")
#                start = False
#      elif command.lower() == 'help':
#           print("start - to start the car \nstop - to stop the car \nquit - to exit")   
#      elif command.lower()== 'quit':
#           break
#      else:
#           print("I don't understand .......")

# printing f with loop
# for i in range(5):
#     if i ==0 or i==2 :
#         print("x" *5,end="")
#         print()
#     else:
#         print("x"*2,end=" ")
#         print()


#    priting f with looop and list    
# num = [5,2,5,2,2]
# for i in num:
#     print("x"* i)

# printng f with nested loop and list
# for i in num:
#     for _ in range(i):
#         print("x",end="")
#     print()

# num = [2,2,2,2,6]
# for i in num:
#     for _ in range(i):
#         print("x",end="")
#     print()

#  this program is to find th elargest number in list
# list = [784,488,34,4,5]
# max = list[0]
# for i in list:
#     if max < i:
#         max = i

# print(f"Largest number is {max}.")

# ist = [784,488,34,4,5]
# min = list[0]
# for i in list:
#     if min >i:
#         min = i

# print(f"minimum number is {min}.")

# matrix =[for i in range(3) for j in range(3)]

list = [1,2,3,4,5]
list.append(6)
list.insert(0,20)
new_list = [7,8,9]  
list.extend(new_list)  # list +=new_list and  list+=[7,8,9] also or list.extend([7,8,9]) cfwork here
# we can use extend and + operator to add multiple  
print(list)