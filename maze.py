# From: https://gist.github.com/zapakh/9a9b39a07964bbd27ab8cbd05ca35501

# Make sure you have enough Fertilizer before starting.
def do_maze(iterations=1):
	# Define some geometry help for later
	opp = {North: South, East: West,
	       South: North, West: East}
	dx = {North: 0, East: 1, South: 0, West: -1}
	dy = {North: 1, East: 0, South: -1, West: 0}

	# Start a Maze.
	num_fertilizer(iterations + iterations * 0.25)
	clear()
	move_to_origin()
	harvest()
	plant(Entities.Bush)
	while get_entity_type() == Entities.Bush:
		use_item(Items.Fertilizer)
		

	x, y = get_pos_x(), get_pos_y()
	goalx, goaly = None, None
	while iterations > 0:
		while get_entity_type() == Entities.Treasure:
			if measure() == None:
				# We've hit the recycling limit.
				iterations = 0
				break
			goalx, goaly = measure()
			# Recycle the maze
			iterations -= 1
			if iterations <= 0:
				break
			while not use_item(Items.Fertilizer):
				pass

		# Use depth-first search, but avoid cycles by keeping
		# track of where we've been, and not revisiting those.
		#
		# https://en.wikipedia.org/wiki/Depth-first_search
		#
		# Our search is "in situ", meaning the literal position
		# of the drone tracks our position in the search.

		stack = [([North, East, South, West], None)]
		visited = {(get_pos_x(), get_pos_y())}

		# Each item in the stack is a 2-tuple containing
		#    * A list of directions to try from this position
		#    * The direction back to the previous position
		#
		# Pushing (appending) an item onto the stack means
		# that we will eventually try all the directions in
		# the list, and then go back to the previous one.
		#
		# Unless we find the Treasure first, of course.

		while get_entity_type() != Entities.Treasure:
			dirs, back = stack[-1]  # stack peek
			oldx = x
			oldy = y
			dir = None
			# Which way do we try next?
			while len(dirs) > 0:
				dir = dirs.pop()
				x = oldx + dx[dir]
				y = oldy + dy[dir]
				if (x, y) in visited or not move(dir):
					# Can't go there.  Try another one.
					dir = None
					continue
				else:
					# Can go there.  Let's go there.
					break
			if dir == None:
				# Time to backtrack.
				stack.pop()   # Get rid of the node we peeked
				if back == None:
					print("I give up!")
					while True:
						do_a_flip()
				move(back)
				x = oldx + dx[back]
				y = oldy + dy[back]
			else:
				# We've made a forward step.  (x, y) have
				# already been updated to our new position.
				visited.add((x, y))
				# Push a stack item to guide the search from here.
				stack.append(
					(get_ranked_dirs(x, y, goalx, goaly, opp[dir]),
					 opp[dir]))
	harvest()

# Helper function, broken out for readability.
def get_ranked_dirs(pos_x, pos_y, goal_x, goal_y, exclude=None):
	if goal_x == None:
		# Fake the priorities since we have no guidance.
		all_dirs = [(1, North), (2, East), (3, South), (4, West)]
	else:
		# The small added amounts break ties, so that min()
		# will not attempt to compare the directions directly,
		# which would cause a crash.
		all_dirs = [
			(goal_y - pos_y + 0.1, North),
			(goal_x - pos_x + 0.2, East),
			(pos_y - goal_y + 0.3, South),
			(pos_x - goal_x + 0.4, West)]

	# The returned list puts our favorite directions at the end
	# so they are the first returned by pop().
	ranked_dirs = []
	for i in range(len(all_dirs)):
		worst_dir = min(all_dirs)
		all_dirs.remove(worst_dir)
		if worst_dir[1] != exclude:
			ranked_dirs.append(worst_dir[1])

	return ranked_dirs
		
def checkmove(X,Y):
	if X != get_pos_x():
		return True
	if Y != get_pos_y():
		return True
	return False

# This function will farm pumpkins until we have the desired amount of fertilizer.
def num_fertilizer(num):
	missing = num - num_items(Items.Fertilizer)
	if missing <= 0:
		return
	# We need 10 pumpkins to get 1 fertilizer
	farm_pumpkins(missing * 10)
	trade(Items.Fertilizer, missing)

iterations = 299
do_maze(iterations)