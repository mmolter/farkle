import random

from collections import Counter
from itertools import repeat
from statistics import mean, median, mode

from matplotlib import pyplot as plt

def is_five(roll):
	'''Return 5 if roll contains a five.'''
	return [5] if 5 in roll else False

def is_one(roll):
	'''Return 1 if roll contains a one.'''
	return [1] if 1 in roll else False

def is_x_of_kind(roll, x, kind=0):
	'''Return [A, A,..(x)] if roll contains x of a kind.'''
	kinds = [k for k, v in Counter(roll).items() if v == x and (k == kind or kind == 0)]

	return [kinds[0]] * x if len(kinds) > 0 else False

def is_three_ones(roll):
	'''Return [1, 1, 1] if roll contains three ones.'''
	return is_three_of_kind(roll, 1)

def is_three_twos(roll):
	''' Return [2, 2, 2] if roll contains three twos.'''
	return is_three_of_kind(roll, 2)

def is_three_threes(roll):
	''' Return [3, 3, 3] if roll contains three threes.'''
	return is_three_of_kind(roll, 3)

def is_three_fours(roll):
	''' Return [4, 4, 4] if roll contains three fours.'''
	return is_three_of_kind(roll, 4)

def is_three_fives(roll):
	''' Return [5, 5, 5] if roll contains three fives.'''
	return is_three_of_kind(roll, 5)

def is_three_sixes(roll):
	''' Return [6, 6, 6] if roll contains three sixes.'''
	return is_three_of_kind(roll, 6)

def is_three_of_kind(roll, kind=0):
	''' Return [A, A, A] if roll contains three of a kind.'''
	return is_x_of_kind(roll, x=3, kind=kind)

def is_four_of_kind(roll):
	''' Return [A, A, A, A] if roll contains four of a kind.'''
	return is_x_of_kind(roll, x=4)

def is_five_of_kind(roll):
	''' Return [A, A, A, A] if roll contains five of a kind.'''
	return is_x_of_kind(roll, x=5)

def is_six_of_kind(roll):
	''' Return [A, A, A, A, A, A] if roll contains six of a kind.'''
	return is_x_of_kind(roll, x=6)

def is_straight(roll):
	'''Return [1, 2, 3, 4, 5, 6] if roll contains a straight (1-6).'''
	return [1, 2, 3, 4, 5, 6] if sorted(roll) == [1, 2, 3, 4, 5, 6] else False

def is_three_pairs(roll):
	'''Return [A, A, B, B, C, C] if roll contains three pairs.'''
	pairs = [k for k, v in Counter(roll).items() if v == 2]

	if len(pairs) == 3:
		A = pairs[0]
		B = pairs[1]
		C = pairs[2]

		return [A, A, B, B, C, C]
	else:
		return False

def is_two_triplets(roll):
	'''Return [A, A, A, B, B, B] if roll contains two triplets.'''
	triplets = [k for k, v in Counter(roll).items() if v == 3]

	if len(triplets) == 2:
		A = triplets[0]
		B = triplets[1]

		return [A, A, A, B, B, B]
	else:
		return False

def is_pair_and_four_kind(roll):
	'''Return [A, A, B, B, B, B] if roll contains a pair and a four of a kind.'''
	counts = Counter(roll).items()
	pairs = [k for k, v in counts if v == 2]
	fours = [k for k, v in counts if v == 4]

	if len(pairs) == 1 and len(fours) == 1:
		A = pairs[0]
		B = fours[0]

		return [A, A, B, B, B, B]
	else:
		return False

def is_farkle(roll):
	'''Return 'True' if roll contains not scoring dice; is a Farkle.'''
	if (is_one(roll) 
		or is_five(roll) 
		or is_straight(roll) 
		or is_two_triplets(roll) 
		or is_three_pairs(roll) 
		or is_pair_and_four_kind(roll)):
		return False

	if any([is_x_of_kind(roll, x=v) for v in [3, 4, 5, 6]]):
		return False

	return True

def roll(hand, new=False):
	return random.choices([1, 2, 3, 4, 5, 6], k=6 if new else len(hand))

def attempt(hand, func, verbose=True):

	if func(hand):
		if verbose: print(hand)
		for dice in func(hand):
			hand.remove(dice)	
		if verbose: print(hand)
	else:
		return 0

	if func == is_one:
		if verbose: print('One! 100 pts.')
		return 100
	elif func == is_five:
		if verbose: print('Five! 50 pts.')
		return 50
	elif func == is_two_triplets:
		if verbose: print('Two triplets! 2,500 pts.')
		return 2500
	elif func == is_pair_and_four_kind:
		if verbose: print('Pair and four of a kind! 1,500 pts.')
		return 1500
	elif func == is_straight:
		if verbose: print('Straight! 1,500 pts.')
		return 1500
	elif func == is_three_pairs:
		if verbose: print('Three pairs! 1,500 pts.')
		return 1500
	elif func == is_six_of_kind:
		if verbose: print('Six of a kind! 3,000 pts.')
		return 3000
	elif func == is_five_of_kind:
		if verbose: print('Five of a kind! 2,000 pts.')
		return 2000
	elif func == is_four_of_kind:
		if verbose: print('Four of a kind! 1,000 pts.')
		return 1000
	elif func == is_three_ones:
		if verbose: print('Three ones! 100 pts.')
		return 100
	elif func == is_three_twos:
		if verbose: print('Three twos! 200 pts.')
		return 200
	elif func == is_three_threes:
		if verbose: print('Three threes! 300 pts.')
		return 300
	elif func == is_three_fours:
		if verbose: print('Three fours! 400 pts.')
		return 400
	elif func == is_three_fives:
		if verbose: print('Three fives! 500 pts.')
		return 500
	elif func == is_three_sixes:
		if verbose: print('Three sixes! 600 pts.')
		return 600

def play_mode_A(cuttoff=0):

	hand = roll([1, 2, 3, 4, 5, 6])
	score = 0

	while True:
		if len(hand):
			hand = roll(hand)
		else:
			hand = roll(hand, new=True)

		points =  0
		points += attempt(hand, is_six_of_kind)
		points += attempt(hand, is_five_of_kind)
		points += attempt(hand, is_two_triplets)
		points += attempt(hand, is_pair_and_four_kind)
		points += attempt(hand, is_straight)
		points += attempt(hand, is_four_of_kind)
		points += attempt(hand, is_three_sixes)
		points += attempt(hand, is_three_fives)
		points += attempt(hand, is_three_fours)
		points += attempt(hand, is_three_threes)
		points += attempt(hand, is_three_ones)
		points += attempt(hand, is_three_twos)

		while is_one(hand) or is_five(hand):
			points += attempt(hand, is_one)
			points += attempt(hand, is_five)

		if not points:
			return 0 if cuttoff else score

		score += points
		if cuttoff and score > cuttoff:
			return score

 
if __name__ == '__main__':
	play_mode_A()
