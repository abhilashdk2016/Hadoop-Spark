from pyspark.sql import Row
from spark_session_config import spark
sc =  spark.sparkContext

lines =  sc.textFile("/p01/sample_data/people.txt")
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

schemaPeople = spark.createDataFrame(people)
schemaPeople.createOrReplaceTempView("people")

teenagers = spark.sql("SELECT name FROM people WHERE age>= 13 AND age<=19")
teenNames = teenagers.rdd.map(lambda p: "Name: "+p.name).collect()
for name in teenNames:
	print(name)
	
'''
Name: Justin
Name: Cheguevera

'''	
