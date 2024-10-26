grid = ("pooobgggg""pobobgddd""pobbbggdd""plllyyydd""plplysssd""pppcyyysd""ccccccssd""ccccccddd""ccccccccc")

# determining list of distinct elements in grid
distinct_elements_of_grid=[]
for line in grid:
    distinct_elements_of_grid +=line
distinct_elements_of_grid=list(set(distinct_elements_of_grid))
print(distinct_elements_of_grid)
    
# determining coordinates of each element on the grid
element_coords = []
for element in range(0,len(distinct_elements_of_grid)):
    tmp_element_coords = []
    for line in range(0,len(grid)):
        for column in range(0,len(grid[line])):
            if grid[line][column]==distinct_elements_of_grid[element]:
                tmp_element_coords.append(tuple([line,column]))
    element_coords.append(tmp_element_coords)
print(element_coords)

# recursive function to loop through possible combinations, validate them, and print the possible coordinate combinations:
def finding_coord_combination(coords, coord_combination, num):
    if(num==0):
        
        for each_coord in range(0,len(coords[num])):
            tmp_coord_combination = []
            if each_coord > 0:
                coord_combination.pop()
            coord_combination.append(coords[num][each_coord])
            tmp_coord_combination.extend(coord_combination)
            tmp_coord_combination.sort()
            valid_combination = 1
            
            if(len(set(list(list(zip(*tmp_coord_combination))[0]))) == len(tmp_coord_combination) and len(set(list(list(zip(*tmp_coord_combination))[1]))) == len(tmp_coord_combination)):

                for element in range(0, len(tmp_coord_combination)-1):

                    if(element<len(tmp_coord_combination)-1):

                        if (tmp_coord_combination[element][1] == tmp_coord_combination[element+1][1]+1 or tmp_coord_combination[element][1] == tmp_coord_combination[element+1][1]-1):
                            
                            valid_combination = 0
                            break
                        
                if valid_combination == 1:

                    color_list=[]

                    for color in tmp_coord_combination:

                        color_list.append(grid[color[0]][color[1]])

                    if(len(list(set(color_list))) == len(tmp_coord_combination)):

                        print("Coordinates of Queens are:",tmp_coord_combination)
                        break
    else:

        for each_coord in range(0,len(coords[num])):

            if each_coord > 0:

                coord_combination.pop()

            coord_combination.append(coords[num][each_coord])
            finding_coord_combination(coords,coord_combination,num-1)
            coord_combination.pop()

coord_combinations = []
finding_coord_combination(element_coords,coord_combinations,len(element_coords)-1)


            
