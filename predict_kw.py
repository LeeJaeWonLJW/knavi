#-*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

tf.app.flags.DEFINE_string("output_graph",
                           "./workspace/kw_graph.pb",
                           "학습된 신경망이 저장된 위치")
tf.app.flags.DEFINE_string("output_labels",
                           "./workspace/kw_labels.txt",
                           "학습할 레이블 데이터 파일")

FLAGS = tf.app.flags.FLAGS

def getScore(image):
    labels = [line.rstrip() for line in tf.gfile.GFile(FLAGS.output_labels)]

    with tf.gfile.FastGFile(FLAGS.output_graph, 'rb') as fp:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(fp.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        logits = sess.graph.get_tensor_by_name('final_result:0')
        prediction = sess.run(logits, {'DecodeJpeg/contents:0': image})

    score = list()
    for tmp in prediction[0]:
        score.append("%.2f" % (tmp * 100))
    return labels, score

if __name__ == "__main__":
    tf.app.run()
