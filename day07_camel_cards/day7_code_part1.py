with open("day7_puzzle_input.txt", "r") as f:
	hands_raw = f.readlines()
hands_raw = [i.replace("\n", "") for i in hands_raw]

"""hands_raw = [
	"32T3K 765",
	"T55J5 684",
	"KK677 28",
	"KTJJT 220",
	"QQQJA 483"
]"""

card_strength = {
	"A": 12,
	"K": 11,
	"Q": 10,
	"J": 9,
	"T": 8,
	"9": 7,
	"8": 6,
	"7": 5,
	"6": 4,
	"5": 3,
	"4": 2,
	"3": 1,
	"2": 0
}


class Hand:
	def __init__(self, hand_text: str):
		hand_, bid = hand_text.split(" ")
		self.hand_str: str = hand_
		self.bid: int = int(bid)

		self.hand_dict = {}

		for card in self.hand_str:
			self.hand_dict[card] = self.hand_dict.get(card, 0) + 1

		if 5 in self.hand_dict.values():
			hand_type = 6  # five of a kind
		elif 4 in self.hand_dict.values():
			hand_type = 5  # four of a kind
		elif 3 in self.hand_dict.values() and 2 in self.hand_dict.values():
			hand_type = 4  # full house
		elif 3 in self.hand_dict.values():
			hand_type = 3  # three of a kind
		elif 2 in set([list(self.hand_dict.values()).count(i) for i in self.hand_dict.values()]):
			hand_type = 2  # two pairs
		elif 2 in self.hand_dict.values():
			hand_type = 1  # one pair
		else:
			hand_type = 0  # high card

		self.hand_type: int = hand_type

	def __lt__(self, other):
		if not isinstance(other, Hand):
			raise TypeError(f"You can only sort Hand with Hand. {other} is type {type(other)}, not Hand.")

		if self.hand_type == other.hand_type:
			for i in range(5):
				if self.hand_str[i] != other.hand_str[i]:
					return card_strength[self.hand_str[i]] < card_strength[other.hand_str[i]]
		else:
			return self.hand_type < other.hand_type

	def __str__(self):
		return f"{self.hand_str} - {self.bid} ({self.hand_type})"


hands = []
for hand in hands_raw:
	hands.append(Hand(hand))

hands = sorted(hands)
total = 0
for i in range(len(hands)):
	total += (i + 1) * hands[i].bid

print(total)
