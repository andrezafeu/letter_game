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

while True:
	secret_word = random.choice(words)
	start = input("\nPress enter/return to start a new game or enter Q to quit").lower()
	if start == 'q':
		break
	print("\nCan you guess what is the secret word? You have 7 guesses.")
	wrong_guesses = []
	right_guesses = []

	while len(wrong_guesses) < 7:
		for letter in secret_word:
			if letter in right_guesses:
				# end= '' allows to print multiple letters on same line
				print(letter, end='')
			else:
				print("_ ", end='')
		print('\nStrikes: {} out of 7\n'.format(len(wrong_guesses)))

		guess = input("Pick a letter: ").lower()

		if len(guess) != 1:
			print("You can only guess a single letter")
			continue
		elif guess in wrong_guesses or guess in right_guesses:
			print("You've already guessed that letter")
			continue
		elif not guess.isalpha():
			print("You can only guess letters")
			continue
		
		if guess in secret_word:
			right_guesses.append(guess)
			found = True
			for letter in secret_word:
				if letter not in right_guesses:
					found = False
			if found:
				print("Congratulations! The secret word is {}.".format(secret_word))
				break
		else:
			wrong_guesses.append(guess)
			print("This word doesn't have the letter {}.".format(guess))
	else:
		print("You ran out of guesses. The secret word was {}.".format(secret_word))