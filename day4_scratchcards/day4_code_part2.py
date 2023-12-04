class Card:
	def __init__(self, card_id, given, winning):
		self.card_id: int = card_id
		self.given: list[int] = given
		self.winning: list[int] = winning
		self.hits: int = 0

		for number in self.given:
			if number in self.winning:
				self.hits += 1


def recursive_solve(all_cards: list[Card], cards: list[Card]) -> int:
	solved_cards = 0
	for card in cards:
		give_cards = all_cards[card.card_id + 1:card.card_id + 1 + card.hits]
		solved_cards += recursive_solve(all_cards, give_cards) + 1

	return solved_cards


def main():
	with open("day4_puzzle_input.txt", "r") as f:
		cards_raw = f.readlines()

	"""cards_raw = [
		"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
		"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
		"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
		"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
		"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
		"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
	]"""

	cards = []
	for i, card in enumerate(cards_raw):
		card = card.split(": ")[1]
		winning, given = card.split(" | ")

		winning = [int(winning[i:i + 2]) for i in range(0, len(winning), 3)]
		given = [int(given[i:i + 2]) for i in range(0, len(given), 3)]

		cards.append(Card(i, given, winning))

	total_cards = recursive_solve(cards, cards)

	print(total_cards)


main()
