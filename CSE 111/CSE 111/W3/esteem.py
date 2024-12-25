
def get_question(prompt):
	prompts = ['1. I feel that I am a person of worth, at least on an equal plane with others.',
               '2. I feel that I have a number of good qualities.',
               '3. All in all, I am inclined to feel that I am a failure.',
               '4. I am able to do things as well as most other people.',
               '5. I feel I do not have much to be proud of.',
               '6. I take a positive attitude toward myself.',
               '7. On the whole, I am satisfied with myself.',
               '8. I wish I could have more respect for myself.',
               '9. I certainly feel useless at times.',
               '10. At times I think I am no good at all.']
if prompt in [0,1,3,5,6]:
		positive = True
else:
      	positive = False
return prompts[prompt], positive

def get_answer():
  	user_input = ''
while user_input not in ['A','a','d','D']:
    	user_input = input('Enter D, d, a, or A: ')
return user_input
  
def get_score(user_input, positive):
    if positive:
            score = positive_score(user_input)
    else:
      	    score = negative_score(user_input)
    return score
  
def positive_score(user_input):
	if user_input == "A":
		running_score = 3
	elif user_input == "a":
            running_score = 2
	elif user_input == "d":
		running_score = 1 
	elif user_input == "D":
            running_score = 0

def negative_score(user_input):
    if user_input == "A":
        running_score = 0
    elif user_input == "a":
        running_score = 1
    elif user_input == "d":
        running_score = 2
    elif user_input == "D":
        running_score = 3




def main():
	running_score = 0
for  i in range(10):
    	question = get_question(i)
print(question[0])
answer = get_answer()
running_score += get_score(answer, question[1])
    
print(f'Your score is: {running_score}.')
if running_score >= 15:
    	print("Your self-esteem is in a healthy range.")
elif running_score <= 15:
		print("you self-esteem is low, you need more friends.")
main()