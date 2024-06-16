def put_pumpkin_seeds():
	world_size = get_world_size()
	flag_planted = False
	buy_grid_seed(Items.Pumpkin_Seed)

	for i in range(world_size):
		for j in range(world_size):
			if num_items(Items.Pumpkin_Seed) == 0:
				buy_seed(Items.Pumpkin_Seed)
			if try_plant(Entities.Pumpkin):
				flag_planted = True
			move(East)
		move(North)

	if not flag_planted:
		try_harvest()
		buy_grid_seed(Items.Pumpkin_Seed)
	
def farm_pumpkins(qnt = -1):
	#soil_grid()
	move_to_origin()

	while qnt == -1 or qnt > num_items(Items.Pumpkin):
		put_pumpkin_seeds()
		move_to_origin()

farm_pumpkins()
