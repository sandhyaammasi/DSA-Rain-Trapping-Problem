height = [1,0,2,1,0,3,0,0,1]

def trapBrute(height) :
    area = 0
    for i in range(len(height)):
            max_left,max_right = 0,0
            for j in range(i,-1,-1):
                max_left = max(max_left,height[j])
            
            for j in range(i,len(height)):
                max_right = max(max_right,height[j])

            area+=min(max_right,max_left)-height[i]
     
    return area
print( trapBrute(height))  