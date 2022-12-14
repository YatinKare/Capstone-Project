import json
import os
import sys
import tensorflow as tf

strategy = tf.distribute.MultiWorkerMirroredStrategy()