import itertools
from scipy.spatial import distance



def actual_cordinates_of_boxes(bbox,im_height,im_width):

    # model gives us normalized cordinates of bbox so we will convert them to actual one

    ymin,xmin,ymax,xmax = (bbox[0] * im_height,bbox[1] * im_width,bbox[2] * im_height,bbox[3] * im_width)
    ymin, xmin, ymax, xmax = int(ymin),int(xmin),int(ymax),int(xmax)

    return (ymin,xmin,ymax,xmax)



def calculate_centroid_of_bbox(ymin,xmin,ymax,xmax):
    # calculate the centroid of bbox

    box_height = int(ymax - ymin)
    box_width = int(xmax - xmin)

    centroid_x = int(xmin + (box_width/2))
    centroid_y = int(ymin + (box_height/2))

    return (centroid_x,centroid_y)



def calculate_possible_permutation(listOfCentroids):

    # it find the all the permutation of centroids in r =  2
    # r = 2 means, here we want pair of 2 centroids.


    permute_list = []

    for permute in itertools.permutations(listOfCentroids,r=2):
        if permute[::-1] not in permute_list:
            permute_list.append(permute)

    return permute_list




def calculate_dist_between_two_centroids(cen1,cen2):
    # it calculates the distance between two centroid points.

    dist = distance.euclidean(cen1,cen2)
    return dist

def calculate_midpoint_of_dist_line(cen1,cen2):

    #it calculates the middle point of two centroid where we want to show the the distance measurement.

    midx = (cen1[0] + cen2[0])/2
    midy = (cen1[1] + cen2[1])/2

    return (midx,midy)










