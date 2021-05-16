from sarang_utils import detection_utils
from sarang_utils import drawing_file
from sarang_utils import social_distancing
from argparse import ArgumentParser
import cv2
from datetime import datetime
import numpy as np




parser = ArgumentParser()
parser.add_argument('-d','--display',default=1,help='display the video',type=int,dest='display')
args = vars(parser.parse_args()) # vars convert it into dictionary.

#load inference graph
detection_graph,sess = detection_utils.load_inference_graph()

if __name__ == '__main__':
    vid = cv2.VideoCapture(r'C:\Users\saran\PycharmProjects\vehicle_security_system\video3.mp4')

    # initial frame
    frame_count = 0

    # starting time
    start_time = datetime.now()
    score_thresh = 0.30
    categories = [1,2,3,4,6,8]
    fps = 0
    while True:
        istrue,frame =vid.read()
        frame = cv2.resize(frame,dsize=(600,600))
        frame = np.array(frame)
        # convert into RGB..
        #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        # im_height & im_width
        im_height,im_width = frame.shape[:2]

        # run the image through the inference graph
        boxes,scores,classes,num = detection_utils.run_image_on_graph(detection_graph,sess,frame)

        filtered_classes,filtered_scores,filtered_boxes,num = detection_utils.filter_classes(classes,boxes,scores,score_thresh,categories,num)

        num_objs = drawing_file.draw_boxes_on_objects(filtered_boxes,filtered_scores,filtered_classes,frame,num)

        cv2.putText(frame,text='num of objects {}'.format(num_objs),org=(10,10),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.50,color=(0,0,255),thickness=2,lineType=8)

        total_time = (datetime.now() - start_time).total_seconds()
        frame_count = frame_count+1

        fps = frame_count / total_time



        if args['display']:
            drawing_file.draw_fps_on_frame(fps,frame)
            cv2.imshow('Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    print("avg fps :",fps)











