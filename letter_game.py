import random

words = [
	'apple',
	'melon',
	'banana',
	'orange',
	'lime',
	'lemon',
	'coconut',
	'strawberry',
	'blueberry',
	'blackberry'
	]

secret_word = random.choice(words)
	
while True:
	start = input("\nPress enter/return to start a new game or enter Q to quit").lower()
	if start == 'q':
		break
	print("\nCan you guess what is the secret word? You have 7 guesses.")
	wrong_guesses = []
	right_guesses = []

	while len(wrong_guesses) < 7 and len(right_guesses) < len(secret_word):
		for letter in secret_word:
			if letter in right_guesses:
				# end= '' allows to print multiple letters on same line
				print(letter, end='')
			else:
				print("_ ", end='')
		print('\nStrikes: {} out of 7\n'.format(len(wrong_guesses)))

		guess = input("Pick a letter: ").lower()

		if guess in secret_word:
			right_guesses.append(guess)
			if len(right_guesses) == len(secret_word):
				print("Congratulations! The secret word is {}.".format(secret_word))
				break
		else:
			wrong_guesses.append(guess)
			print("This word doesn't have the letter {}.".format(guess))
	else:
		print("You ran out of guesses. The secret word was {}.".format(secret_word))