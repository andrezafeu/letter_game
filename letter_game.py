import random

words = [
	'apple',
	'melon',
	'banana',
	'organge',
	'lime',
	'lemon',
	'coconut',
	'strawberry',
	'blueberry',
	'blackberry'
	]

secret_word = random.choice(words)

def start_game():	
	print("Can you guess what is the secret word?")
	word_in_construction = "_ " * len(secret_word)
	print(word_in_construction)

start_game()