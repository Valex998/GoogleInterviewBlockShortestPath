#So we want to buy an apartment in any of the given blocks, but we wish we have some points of interest close to our home
#We got the priority list which contains the points of interest we wish to be closer to
#We wanna buy an apartament in the block that is the closest to all of our important points of interest
#e.g. in the current input, we have the list of 4 blocks, each of 3 points of interest(we can't have a point of interest
#which is not in the blocks). So if our priorities are all 3 points, the best block should be the 3rd one or
#index 2 in the given tuple {"gym" : 0, "school" : 1, "store" : 0}, because the distance to school is 0 and in
#the next block (4th one or index 3 in the given tuple) we have the store to which the distance is 1 and in the previous
#block (2nd one or index 1 in the given tuple) we have the gym to which the distance is also 1 and so we have the maximum
#distance to a priority equal to 1


blocks = ({"gym" : 0, "school" : 1, "store" : 0},
          {"gym" : 1, "school" : 0, "store" : 0},
          {"gym" : 0, "school" : 1, "store" : 0},
          {"gym" : 0, "school" : 1, "store" : 1})

priority = ["gym", "school" , "store"]

totalDistance = [] #total distance from every block to the priorities

def checkDistance(prio):    #checks distance to the nearest prio
    pass

def checkPriority(block, prio):
    if prio.get(block) == 1:
        print("test")

checkPriority("gym", blocks[1])