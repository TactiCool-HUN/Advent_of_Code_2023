with open("day2_puzzle_input.txt", "r") as f:
	test_games = f.readlines()

"""test_games = [
	"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
	"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
	"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
	"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
	"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]"""

game_ids: list[int] = []

for game in test_games:
	game = game[5:]
	pos = game.index(":")
	game_id = int(game[:pos])

	shows = []
	for show in game[pos + 2:].split("; "):
		temp = {
			"red": 0,
			"blue": 0,
			"green": 0
		}
		show = show.split(", ")
		for color in show:
			amount = int(color[:2])
			for key in temp:
				if key in color:
					temp[key] = amount
		shows.append(temp)

	for show in shows:
		if show["red"] > 12:
			break
		elif show["green"] > 13:
			break
		elif show["blue"] > 14:
			break
	else:
		game_ids.append(game_id)

print(sum(game_ids))
