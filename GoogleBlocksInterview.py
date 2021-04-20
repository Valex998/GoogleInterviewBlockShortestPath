#So we want to buy an apartment in any of the given blocks, but we wish to have some points of interest close to our home
#We got the priority list which contains the points of interest we wish to be closer to
#We wanna buy an apartament in the block that is the closest to all of our important points of interest(priorities)
#e.g. in the current input, we have the list of 4 blocks, each of 3 points of interest(we can't have a point of interest
#which is not in the blocks). So if our priorities are all 3 points, the best block should be the 3rd one (or
#index 2)in the given tuple) {"gym" : 0, "school" : 1, "store" : 0}, because the distance to the school is 0 and in
#the next block (4th one or index 3 in the given tuple) we have the store to which the distance is 1 and in the previous
#block (2nd one or index 1 in the given tuple) we have the gym to which the distance is also 1 and so we have the maximum
#distance to a priority equal to 1


blocks = ({"gym" : 0, "school" : 1, "store" : 0},
          {"gym" : 1, "school" : 0, "store" : 0},
          {"gym" : 0, "school" : 1, "store" : 0},
          {"gym" : 0, "school" : 1, "store" : 1})

priorities = ["gym", "school" , "store"]

maximumDistance = [] #maximum Distance to any point of interests, the index coresponds to the tuple blocks
shortestPath = [0, 1]

for i in range(len(blocks)):
    maximumDistance.append(0)

def checkDistance(priority, cbi):    #checks distance to the nearest prio, cbi stands for current block index
    distance = 0
    ok = 0
    if blocks[cbi].get(priority) != 1:
        distance = 1
        while ok == 0:
            if cbi + distance < len(blocks):
                if blocks[cbi + distance].get(priority) == 1:
                    ok = 1
            if cbi - distance >= 0 and ok != 1:
                if blocks[cbi - distance].get(priority) == 1:
                    ok = 1
            if ok == 1:
                break
            distance += 1

    if distance >= maximumDistance[cbi]:
        maximumDistance[cbi] = distance

for i  in range(len(blocks)):
    for priority in priorities:
        checkDistance(priority, i)

indices = [i for i,x in enumerate(maximumDistance) if x == min(maximumDistance)]

print("The best blocks are:")
for i in indices:
    print(f"Index {i} of blocks tuple: {blocks[i]}\n")
