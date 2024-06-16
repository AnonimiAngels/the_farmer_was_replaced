
def farm_hay(qnt = -1):
	move_to_origin()
	soil_grid()

	while qnt == -1 or qnt > num_items(Items.Hay):
		try_harvest()
		try_plant(Entities.Grass)

farm_hay()