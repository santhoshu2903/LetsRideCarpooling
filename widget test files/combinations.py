locations=[1,2,3,4,5]

def effected_locations(locations, from_location,to_location):
    from_index=locations.index(from_location)
    to_index = locations.index(to_location)
    print(from_index,to_index)
    end_index=len(locations)-1
    effected_locations=[]
    for i in range(0,end_index+1):
        for j in range(from_index,end_index+1):
            if i>to_index or i==to_index or j==from_index :
                continue
            elif j<i or i==j:
                continue
            print(i,j)
            effected_locations.append([locations[i],locations[j]])
                           
    return effected_locations
       
print(effected_locations(locations,2,3))
           