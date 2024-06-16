def is_even(num):
	return num % 2 == 0

def try_harvest():
	if can_harvest(): 
		harvest()

def wait_until_grown():
	while not can_harvest():
		pass

def move_to(x,y):
	distance_east = x - get_pos_x() 
	distance_north = y - get_pos_y()
	size = get_world_size()
	if distance_east < size / 2 or (distance_east < 0 and abs(distance_east) > size / 2):
		move_direction = East
	else:
		move_direction = West
	while get_pos_x() != x:
		move(move_direction)
	if distance_north < size / 2 or (distance_north < 0 and abs(distance_north) > size / 2):
		move_direction = North
	else:
		move_direction = South
	while get_pos_y() != y:
		move(move_direction)
			


def move_to_origin():
	move_to(0, 0)

def raise_water_level(level):
	while get_water() < level:
		use_item(Items.Water_Tank)

def soil_grid():
	world_size = get_world_size()
	for i in range(world_size):
		for j in range(world_size):
			try_harvest()

			ground_type = get_ground_type()
			required_ground = Grounds.Soil

			if ground_type != required_ground:
				till()
			
			move(North)
		move(East)

def buy_seed(seed_item, qnt = 1):
	trade(seed_item, qnt)

def buy_grid_seed(seed_item):
	max_seeds = get_world_size() * get_world_size()
	num_seeds = num_items(seed_item)
	if num_seeds < max_seeds:
		buy_seed(seed_item, max_seeds - num_seeds)


def try_plant(entity):
	if get_entity_type() != entity:
		plant(entity)
		raise_water_level(1)
		return True
	return False

def put_and_harvest(entity = None, seed_item = None):
	world_size = get_world_size()
	buy_grid_seed(seed_item)

	for i in range(world_size):
		for j in range(world_size):
			try_harvest()
			try_plant(entity)
			move(East)
		move(North)
