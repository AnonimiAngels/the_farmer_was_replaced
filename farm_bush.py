def farm_bushes(qnt = -1):
	move_to_origin()
	soil_grid()

	while qnt == -1 or qnt > num_items(Items.Wood):
		move_to_origin()
		put_and_harvest(Entities.Bush, Items.Wood)

farm_bushes()