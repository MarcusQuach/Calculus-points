# Import math library to get square root function
import math

# Define argument for x1, x2, y1, y2
def find_points(x1,x2,y1,y2):

# Define distance as d and use distance formula for 2 coordinates
    d = math.sqrt((x2 - x1)**2 + (y2-y1)**2)

    # Print distance
    print(d)

# Put x1, x2, y1, y2 as points for arguments
find_points(0,2,4,6)