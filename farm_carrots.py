
def farm_carrots(qnt = -1):
	move_to_origin()
	soil_grid()

	while qnt == -1 or qnt > num_items(Items.Carrots):
		move_to_origin()
		buy_grid_seed(Items.Carrot_Seed)
		put_and_harvest(Entities.Carrots, Items.Carrot_Seed)

farm_carrots()