def put_sunflowers_seeds():
	size = get_world_size()
	scores = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[]}
	put_and_harvest(Entities.Sunflower, Items.Sunflower_Seed)
	
	for i in range(size):
		for j in range(size):
			wait_until_grown()
			petals=measure()
			scores[petals].append([get_pos_x(), get_pos_y()])
			move(East)
		move(North)

	for score in range(15, 0, -1):
		for location in scores[score]:
			move_to(location[0], location[1])
			harvest()
			

def do_sunflowers(qnt = -1):
	clear()
	soil_grid()

	while qnt == -1 or qnt > num_items(Items.Power):
		move_to_origin()
		put_sunflowers_seeds()

do_sunflowers()