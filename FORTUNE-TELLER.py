
import random
dice = ("Without a doubt", "It is certain", "It is decidedly so","Yes", "For Sure", "No", "Dont count on it", "Try asking again","Reply hazy, try again", "Confucious says 'No'", "Better not tell you now","Cannot predict now","Concentrate and ask again","My reply is no","Outlook not so good","Very doubtful","Outlook is good","Most likely","As I see it, yes","I do not understand the question")
answer_set=set([])
while True:
	choice = raw_input("Type 'ask' to ask a question. Type 'quit' to quit.\n")
	if choice == "ask":
		raw_input("Please enter your question:\n")
		roll = random.randint(0, len(dice) -1 )
		answer = dice[roll]
		answer_set.add(answer)
		print answer
		raw_input()
	elif choice == "quit":
		true = 0
		raw_input()
	else:
		print "Error -- Try again\n"
	sorted_list = sorted(answer_set)
	print "Your answer's sorted:", sorted_list
	print "Your answer's sorted: ", ','.join(sorted_list)
