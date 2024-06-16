def put_tree_seeds(secondary = None):
	world_size = get_world_size()
	choosen_seed = Entities.Tree

	total_tiles = world_size * world_size
	needed_seeds = total_tiles - (total_tiles // 2)
	seeds = { None: None, Entities.Tree: None, Entities.Bush: None, Entities.Sunflower: Items.Sunflower_Seed, Entities.Grass: None, Entities.Carrots: Items.Carrot_Seed, Items.Pumpkin: Items.Pumpkin_Seed }

	if secondary != None and secondary in seeds and seeds[secondary] != None:
		buy_seeds(seeds[secondary], needed_seeds)
		
	for i in range(world_size):
		for j in range(world_size):
			try_harvest()
			
			choosen_seed = secondary 
			if is_even(i + j % world_size):
				choosen_seed = Entities.Tree
			
			if choosen_seed != None:
				try_plant(choosen_seed)
			move(East)
		move(North)
	
def farm_trees(qnt = -1, secondary = None):
	clear()
	soil_grid()

	while qnt == -1 or qnt > num_items(Items.Wood):
		move_to_origin()
		put_tree_seeds(secondary)

farm_trees()
