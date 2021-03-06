from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

import numpy as np

from pyspark.mllib.stat import Statistics

conf = SparkConf().setMaster("local").setAppName("MyAPP")
sc = SparkContext(conf=conf)

data =  sc. parallelize([(1, 'a'), (1, 'b'), (2, 'c'), (2, 'd'), (2, 'e'), (3, 'f')])
fractions = {1:0.1, 2:0.6, 3:0.3}
approxSample = data.sampleByKey(False, fractions)
print approxSample


