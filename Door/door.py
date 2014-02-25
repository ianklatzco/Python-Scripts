import doorimage #imports the door variable
import time #imports a library with time-wimey counts
import responses #imports lots of variables that will be concentated

print "This is a simple program reminiscent \
of Skyrim's various Dark Brotherhood access doors and \
their respective passwords. Give it a shot!"

#variables are defined here.
evaluate_illusion = "What is life's greatest illusion?"
evaluate_music = "What is the music of life?"
evaluate_color = "What is the color of night?"

illusion_correct = 1
music_correct = 1
color_correct = 1

illusion_answer = 0
music_answer = 0
color_answer = 0

response = 0
response_incorrect = "You are not worthy."

welc = "Welcome home."
#end variables

#functions are defined here
def welcome():
	print welc
	time.sleep(2.3)
	print doorimage.thedoor
	print
	time.sleep(2.3)

def intro():
	print
	print "Pick a door:"
	print
	print "1. Dawnstar Sanctuary."
	print "2. Falkreath Sanctuary."
	print "3. Morrowind Sanctuary. (incomplete)"
	print

def eval_illusion(): 
	print evaluate_illusion
	print
	print "1. %s\n2. %s\n3. %s\n4. %s\n" %(responses.illusion_correct_responses)

def eval_music():
	print evaluate_music
	print
	print "1. %s\n2. %s\n3. %s\n4. %s\n" %(responses.music_correct_responses)

def eval_color():
	print evaluate_color
	print
	print "1. %s\n2. %s\n3. %s\n4. %s\n" %(responses.color_correct_responses)
#and we're done with functions

#begin program----------------------------------------------------------------------------------------------------\
#initial menu, they pick the doors and are prompted to answer accordingly.

intro()

response = input("Enter a number: ")

#checks response placed in, asks for an answer
if response == 1:
	eval_illusion()
	illusion_answer = input("Enter a number: ")
elif response == 2:
	eval_music()
	music_answer = input("Enter a number: ")
elif response == 3:
	eval_color()
	print "Because placeholders are awesome! I couldn't find the other phrases."
	color_answer = input("Enter a number: ")

#prints door, welcome message
#an incorrect response yields a false message
if illusion_answer == illusion_correct or music_answer == music_correct or color_answer == color_correct:
	welcome()
else:
	print response_incorrect
	time.sleep(2.3)