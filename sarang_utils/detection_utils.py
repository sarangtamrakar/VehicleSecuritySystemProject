import cv2
import datetime
import tensorflow as tf
import itertools
import numpy as np



path_to_graph = r'C:\Users\saran\PycharmProjects\vehicle_security_system\frozen\frozen_inference_graph.pb'




def load_inference_graph():
    print('>>>>>>>>>>>loading graph..')
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(path_to_graph, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
        sess = tf.Session(graph=detection_graph)
        print('>>>>>>>>> graph is loaded')
    return detection_graph,sess



def run_image_on_graph(detection_graph,sess,image_np):
    # define input & output tensors...
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    image_expended = np.expand_dims(image_np, axis=0)

    (boxes, scores, classes, num) = sess.run([detection_boxes, detection_scores, detection_classes, num_detections],
                                             feed_dict={image_tensor: image_expended})

    return np.squeeze(boxes), np.squeeze(scores), np.squeeze(classes),num



def filter_classes(classes,boxes,scores,threshold_score,categories,num):
    idx = []
    for i in range(len(classes)):
        if classes[i] in categories and scores[i] >= threshold_score:
            idx.append(i)


    filtered_classes = classes[idx]
    filtered_scores = scores[idx]
    filtered_boxes = boxes[idx]
    filtered_num = len(idx)


    return filtered_classes,filtered_scores,filtered_boxes,filtered_num





