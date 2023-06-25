from a1_support import *


def display_game(game, grid_size):
    dash = WALL_HORIZONTAL * (grid_size * 4 + 4)
    print(" ", end=" ")
    for i in range(grid_size):
        if i < 9:
            print(WALL_VERTICAL, i + 1, end=" ")
        elif i >= 9:
            print(WALL_VERTICAL, i + 1, end="")
        if i+1 == grid_size:
            print(WALL_VERTICAL)
    print(dash)

    for i in range(grid_size):
        print(ALPHA[i], end=" ")
        for j in range(grid_size):
            print(WALL_VERTICAL, game[j + (i * 3)], end=" ")
        print(WALL_VERTICAL)
        print(dash)


# Function that returns indexes
def return_cell_index(action, grid_size):

    row_list = []
    for i in range(grid_size):
        row_list.append(i + 1)

    col_list = []
    for i in range(grid_size):
        col_list.append(ALPHA[i])

    if len(action) <= 3:
        if len(action) == 2:
            if action[0] in col_list and int(action[1]) in row_list:
                col_index = col_list.index(action[0])
                row_index = row_list.index(int(action[1]))
            else:
                return None

        else:
            if action[0] in col_list and int(action[1:]) in row_list:
                col_index = col_list.index(action[0])
                row_index = row_list.index(int(action[1:]))
            else:
                return None

    else:
        if action[2] in col_list and int(action[3:]) in row_list:
            col_index = col_list.index(action[2])
            row_index = row_list.index(int(action[3:]))
        else:
            return None

    if (col_index is not None) and (row_index is not None):
        tuple_index = (col_index, row_index)
        return tuple_index
    else:
        return None


def parse_position(action, grid_size):
    if len(action) >= 2:
        if action[0].isupper() and action[1].isdigit():
            index = return_cell_index(action, grid_size)
            return index

        elif action[0] == 'f' and action[2].isupper() and action[3].isdigit():
            index = return_cell_index(action, grid_size)
            return index

        elif action == ':)':
            display_game('~' * grid_size ** 2,grid_size)
        else:
            print(INVALID)
    else:
        print(INVALID)


def position_to_index(position, grid_size):
    list_of_position = []
    for i in range(grid_size):
        for j in range(grid_size):
            position_tuple = (i, j)
            list_of_position.append(position_tuple)
    #print(list_of_position)

    for i in list_of_position:
        if position == i:
            return list_of_position.index(i)


def replace_character_at_index(game, index, character):
    if index in range(len(game)):
        game = game[:index] + character + game[index + 1:]
        return game


def flag_cell(game, index):
    if game[index] == UNEXPOSED:
        game = game[:index] + FLAG + game[index + 1:]
        return game
    elif game[index] == FLAG:
        game = game[:index] + UNEXPOSED + game[index + 1:]
        return game


def index_in_direction(index, grid_size, direction):
    a = int(grid_size**2)
    index_range = list(range(a))
    if any(direction in i for i in DIRECTIONS):
        if direction == UP:
            upd_index = int(index) - int(grid_size)
            if upd_index in index_range:
                return upd_index

        if direction == DOWN:
            upd_index = int(index) + int(grid_size)
            if upd_index in index_range:
                return upd_index

        if direction == LEFT:
            upd_index = int(index) - 1
            if (upd_index in index_range) and (int(index) % int(grid_size) != 0):
                return upd_index

        if direction == RIGHT:
            upd_index = int(index) + 1
            if (upd_index in index_range) and (int(index+1) % int(grid_size) != 0):
                return upd_index

        if direction == f"{UP}-{LEFT}":
            upd_index = (int(index) - int(grid_size)) - 1
            if upd_index in index_range:
                return upd_index

        if direction == f"{UP}-{RIGHT}":
            upd_index = (int(index) - int(grid_size)) + 1
            if (upd_index in index_range) and (int(index) - int(grid_size) > 0)\
                    and (int(index+1) % int(grid_size) != 0):
                return upd_index

        if direction == f"{DOWN}-{LEFT}":
            upd_index = (int(index) + int(grid_size)) - 1
            if (upd_index in index_range) and (int(index) % int(grid_size) != 0):
                return upd_index

        if direction == f"{DOWN}-{RIGHT}":
            upd_index = (int(index) + int(grid_size)) + 1
            if (upd_index in index_range) and (int(index+1) % int(grid_size) != 0):
                return upd_index

    else:
        return None


def neighbour_directions(index, grid_size):
    index = int(index)
    grid_size = int(grid_size)
    index_list = list(range(grid_size**2))
    neighbour_list = []

    top_left = index_list[0]
    top_right = index_list[0] + (grid_size-1)
    bottom_left = top_right * grid_size
    bottom_right = index_list[-1]

    middle = int(index_list[-1] / 2)

    left = index - 1
    right = index + 1
    up = index - grid_size
    down = index + grid_size

    if index == int(top_left):
        diag = index + (grid_size + 1)
        neighbour_list.append(right)
        neighbour_list.append(down)
        neighbour_list.append(diag)
        return neighbour_list

    if index == int(top_right):
        diag = (index + grid_size) - 1
        neighbour_list.append(left)
        neighbour_list.append(down)
        neighbour_list.append(diag)
        return  neighbour_list

    if index == int(bottom_left):
        diag = index - (grid_size - 1)
        neighbour_list.append(right)
        neighbour_list.append(up)
        neighbour_list.append(diag)
        return neighbour_list

    if index == int(bottom_right):
        diag = index - (grid_size + 1)
        neighbour_list.append(left)
        neighbour_list.append(up)
        neighbour_list.append(diag)
        return neighbour_list

    #if grid_size % 2 != 0:
    if index == middle:
        neighbour_list.append(middle - (grid_size + 1))
        neighbour_list.append(middle - grid_size)
        neighbour_list.append(middle - (grid_size - 1))
        neighbour_list.append(middle - 1)
        neighbour_list.append(middle + 1)
        neighbour_list.append(middle + (grid_size - 1))
        neighbour_list.append(middle + grid_size)
        neighbour_list.append(middle + (grid_size + 1))
        return neighbour_list

    if index != middle and index != int(bottom_right) and index != int(bottom_left)\
        and index != int(top_right) and index != int(top_left):

        for i in DIRECTIONS:
            abc = index_in_direction(index, grid_size, i)
            if abc != None:
                neighbour_list.append(abc)
        return neighbour_list

def big_fun_search(game, grid_size, pokemon_locations, index):
	"""Searching adjacent cells to see if there are any Pokemon"s present.

	Using some sick algorithms.

	Find all cells which should be revealed when a cell is selected.

	For cells which have a zero value (i.e. no neighbouring pokemons) all the cell"s
	neighbours are revealed. If one of the neighbouring cells is also zero then
	all of that cell"s neighbours are also revealed. This repeats until no
	zero value neighbours exist.

	For cells which have a non-zero value (i.e. cells with neighbour pokemons), only
	the cell itself is revealed.

	Parameters:
		game (str): Game string.
		grid_size (int): Size of game.
		pokemon_locations (tuple<int, ...>): Tuple of all Pokemon's locations.
		index (int): Index of the currently selected cell

	Returns:
		(list<int>): List of cells to turn visible.
	"""
	queue = [index]
	discovered = [index]
	visible = []

	if game[index] == FLAG:
		return queue

	number = number_at_cell(game, pokemon_locations, grid_size, index)
	if number != 0:
		return queue

	while queue:
		node = queue.pop()
		for neighbour in neighbour_directions(node, grid_size):
			if neighbour in discovered or neighbour is None:
				continue

			discovered.append(neighbour)
			if game[neighbour] != FLAG:
				number = number_at_cell(game, pokemon_locations, grid_size, neighbour)
				if number == 0:
					queue.append(neighbour)
			visible.append(neighbour)
	return visible


def number_at_cell(game, pokemon_locations, grid_size, index):

    neighbour_list = neighbour_directions(index,grid_size)
    count = 0
    for i in pokemon_locations:
        for j in neighbour_list:
            if i == j:
                count = count + 1
    return count


def check_win(game, pokemon_locations):
    str_list = []
    final_list = []
    for i, c in enumerate(game):
        str_list.append(i)

    for i in str_list:
        if i not in pokemon_locations:
            final_list.append(i)

    counter = 0
    flag_counter = 0
    unexposed_flag = 0

    for i in str_list:
        if i in pokemon_locations and game[i] == FLAG:
            counter += 1
        elif game[i] == UNEXPOSED:
            unexposed_flag = 1

    for ele in game:
        if ele == FLAG:
            flag_counter += 1

    if unexposed_flag == 1 and counter == len(pokemon_locations):
        return False
    if flag_counter == len(game):
        return False
    if flag_counter == 0:
        return False
    elif counter == len(pokemon_locations):
        return True


def main():
    #pass
    grid_size = int(input("Please input the size of the grid: "))
    no_of_pokemons = int(input("Please input the number of pokemons: "))

    game = '~' * grid_size ** 2
    #pokemons = generate_pokemons(grid_size, no_of_pokemons)
    pokemons = (0,3,1)
    #print(pokemons)

    display_game(game, grid_size)
    print()

    while True:
        action = input("Please input action: ")

        if action == 'h':
            print(HELP_TEXT)
            display_game(game, grid_size)
            print()

        elif action == 'q':
            ui = input("You sure about that buddy? (y/n): ")
            if ui == 'y':
                print("Catch you on the flip side.")
                break
            elif ui == 'n':
                print("Let's keep going.")
                display_game(game, grid_size)
                print()
            else:
                print(INVALID)
                display_game(game, grid_size)
                print()

        elif len(action) != 0 and action[0].isupper():
            row_col_tuple = parse_position(action, grid_size)
            integer = position_to_index(row_col_tuple, grid_size)

            if integer in pokemons and game[integer] != FLAG:
                for i in pokemons:
                    game = replace_character_at_index(game, i, POKEMON)

                display_game(game, grid_size)
                print("You have scared away all the pokemons.")
                break

            elif game[integer] == FLAG:
                display_game(game, grid_size)
                print()

            else:
                first = number_at_cell(game, pokemons, grid_size, integer)
                replacement = []

                if first == 0:
                    game = replace_character_at_index(game, integer, str(first))

                    bfs = big_fun_search(game, grid_size, pokemons, integer)

                    for i in bfs:
                        if game[i] == FLAG:
                            replacement.append(i)
                            game = replace_character_at_index(game, i, FLAG)

                            nac = []
                            for i in bfs:
                                number = number_at_cell(game, pokemons, grid_size, i)
                                nac.append(number)

                            for i in bfs:
                                drashti = nac[int(bfs.index(i))]
                                drashti = str(drashti)
                                game = replace_character_at_index(game, i, drashti)

                            for i in replacement:
                                game = replace_character_at_index(game, i, FLAG)

                        else:
                            nac = []
                            for i in bfs:
                                number = number_at_cell(game, pokemons, grid_size, i)
                                nac.append(number)

                            for i in bfs:
                                drashti = nac[int(bfs.index(i))]
                                drashti = str(drashti)
                                game = replace_character_at_index(game, i, drashti)

                            for i in replacement:
                                game = replace_character_at_index(game, i, FLAG)

                else:
                    game = replace_character_at_index(game, integer, str(first))

                display_game(game, grid_size)
                print()


        elif len(action) != 0 and action[0] == 'f' and action[3].isdigit():
            row_col_tuple = parse_position(action, grid_size)
            integer = position_to_index(row_col_tuple, grid_size)

            game = flag_cell(game, integer)
            display_game(game, grid_size)
            print()

        elif action == ':)':
            print("It's rewind time.")
            game = '~' * grid_size ** 2
            display_game(game, grid_size)
            print()

        else:
            parse_position(action, grid_size)
            display_game(game, grid_size)
            print()

if __name__ == "__main__":
    main()
