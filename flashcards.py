import sys
#access command line arguments--> in sys.argv list
import random
if len(sys.argv)<2:
	print("Please supply flashcard file...")
	exit(1)
#need flashcard file and lives in sys.argv
# file must be comma seperated and on seperate lines (format needs to work)
flashcard_filename=sys.argv[1]
f=open(flashcard_filename, "r")
#read in data from flashcard info provided
question_dict={}

for line in f:
	entry=line.strip().split(",") #comma dilimmitted -so splitted to make a dict
	question = entry[0]
	answer = entry [1]
	question_dict[question]=answer #store in dict
f.close()

#ready to start!
print("Welcome to the flashcard quizzer!")
print("At any time, type 'quit' to quit")
print('')

questions= list(question_dict.keys())


while True:
	question= random.choice(questions)
	answer= question_dict[question]

	print("Question: "+question)
	user_input= input("Your Guess: ")
	if user_input == 'quit':
		print("Thanks for playing! Bye.")
		break
	elif user_input == answer:
		print("Great job, you are correct!")
	else:
		print("Sorry, the answer is actually "+ answer)