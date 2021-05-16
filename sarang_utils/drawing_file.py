import cv2
from sarang_utils.social_distancing import actual_cordinates_of_boxes,calculate_centroid_of_bbox
from sarang_utils.social_distancing import calculate_possible_permutation,calculate_dist_between_two_centroids,calculate_midpoint_of_dist_line
from playsound import playsound



def draw_boxes_on_objects(boxes,scores,classes,image_np,num):



    color = 0
    color1 = (0,0,255)
    color2 = (255,0,0)
    avg_width = 40
    im_height,im_width = image_np.shape[:2]
    obj_count = 0

    for i in range(num):

        if classes[i] == 1:
            id = 'person'
            avg_width = 16.1
            obj_count += 1

        elif classes[i] == 2:
            id = 'bicycle'
            avg_width = 16.0
            obj_count += 1

        elif classes[i] == 3:
            id = 'car'
            avg_width = 36.0
            obj_count += 1

        elif  classes[i] == 4:
            id = 'motorcycle'
            avg_width = 18
            obj_count += 1

        elif  classes[i] == 6:
            id = 'bus'
            avg_width = 100.0
            obj_count += 1

        else:
            id = 'truck'
            avg_width = 102.0
            obj_count += 1





    # we will calculate the cordinates of each bbox & centroid & save it to the list.
    centroids = []
    cordinates = []

    for box in boxes:
        cordi = actual_cordinates_of_boxes(box,im_height,im_width)
        centroid = calculate_centroid_of_bbox(cordi[0],cordi[1],cordi[2],cordi[3])
        centroids.append(centroid)
        cordinates.append(cordi)




    # we will calculate the all possible permutation of centroids in pairs.
    permutation = calculate_possible_permutation(centroids)
    # draw boxes on image_np
    for cordi,centroid,perm,score in zip(cordinates,centroids,permutation,scores):
        dist = calculate_dist_between_two_centroids(perm[0],perm[1])
        mid = calculate_midpoint_of_dist_line(perm[0],perm[1])

        if dist < 50:
            cv2.rectangle(img=image_np, pt1=(int(cordi[1]), int(cordi[0])), pt2=(int(cordi[3]), int(cordi[2])),color=color1, thickness=2, lineType=8)
            cv2.putText(img=image_np,text='score : {0:0.2f}'.format(score),org=(int(cordi[1]),int(cordi[0]-5)),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.50,color=color1,thickness=1,lineType=8)
            cv2.putText(img=image_np, text='class : {}'.format(id), org=(int(cordi[1]), int(cordi[0] - 20)),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.50, color=color1, thickness=1, lineType=8)
            cv2.circle(img=image_np,center=centroid,radius=2,color=color1,thickness=2,lineType=8)
            cv2.line(img=image_np, pt1=(int(perm[0][0]), int(perm[0][1])), pt2=(perm[1][0], perm[1][1]),color=color1, thickness=2, lineType=8)
            cv2.putText(img=image_np, text=" {}".format(int(dist)), org=(int(mid[0]), int(mid[1])),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.50, color=(0,0,0), thickness=1, lineType=8)
            playsound('sarang_utils/alert.wav')

        elif dist >50:
            cv2.rectangle(img=image_np, pt1=(int(cordi[1]), int(cordi[0])), pt2=(int(cordi[3]), int(cordi[2])),color=color2, thickness=2, lineType=8)
            cv2.putText(img=image_np, text='score : {0:0.2f}'.format(score), org=(int(cordi[1]), int(cordi[0] - 5)),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.50, color=color2, thickness=1, lineType=8)
            cv2.putText(img=image_np, text='class : {}'.format(id), org=(int(cordi[1]), int(cordi[0] - 20)),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.50, color=color2, thickness=1, lineType=8)
            cv2.circle(img=image_np, center=centroid, radius=2, color=color2, thickness=2, lineType=8)
            cv2.line(img=image_np, pt1=(int(perm[0][0]), int(perm[0][1])), pt2=(perm[1][0], perm[1][1]),color=color2, thickness=1, lineType=8)
            cv2.putText(img=image_np, text=" {}".format(dist), org=(int(mid[0]), int(mid[1])),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.50, color=(0,0,0), thickness=1, lineType=8)

        else:
            pass

    return obj_count


def draw_fps_on_frame(fps,frame):
    cv2.putText(img=frame,text='FPS : {0:0.2f}'.format(fps),org=(30,30),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.50,color=(255,0,0),thickness=2,lineType=8)











