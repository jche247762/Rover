from planet import Planet
from rover import Rover
from terrain import Tile

def load_level(filename):
	"""
	Loads the level and returns an object of your choosing
	"""
	structure_correct=True
	pt = Planet("dummy", 0, 0)
	rov = Rover(0, 0, 0)
	with open(filename, 'r') as myfile:
		lines=myfile.readlines()
		if lines[len(lines)-1]=='\n':
			del lines[len(lines)-1]
		for i in lines:
			if i.strip()=='[tiles]':
				index_tiles=lines.index(i)+1
		if not lines[0].strip() == "[planet]":
			return False, None, None

		try:
			if not lines[1].split(",")[0] == "name": return False, None, None
			if not lines[2].split(",")[0] == "width": return False, None, None
			if not lines[3].split(",")[0] == "height": return False, None, None
			if not lines[4].split(",")[0] == "rover": return False, None, None

			planet_name = lines[1].strip().split(",")[1]
			width = int(lines[2].strip().split(",")[1])
			height = int(lines[3].strip().split(",")[1])
			rov_x = int(lines[4].strip().split(",")[1])
			rov_y = int(lines[4].strip().split(",")[2])

			if width < 5 or height < 5: return False, None, None          # 4 fields

			if len(lines) != width * height + index_tiles: return False, None, None
			if width < rov_x or height < rov_y or rov_x < 0 or rov_y < 0: return False, None, None

			pt = Planet(planet_name, width, height)

			for i in range(index_tiles, len(lines)):
				row = int((i - index_tiles) / width)
				col = int((i - index_tiles) % width)
				pt.tiles[row][col].type = lines[i].strip().split(",")[0]
				pt.tiles[row][col].elv = [int(e) for e in lines[i].strip().split(",")[1:]]
			rov = Rover(rov_x, rov_y, pt.tiles[rov_x][rov_y].elv)
			pt.tiles[rov_x][rov_y].explored = True
			pt.ratio += 1

		except Exception as e:
			print(e)
			return False, None, None

	return structure_correct, pt, rov
					
					
					
				
	


	
	
