from pyspark import SparkConf,SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile("ml-100k/u.data")
#user id | item id | rating | timestamp. 

ratings = lines.map(lambda x:x.split()[2])
result = ratings.countByValue()
print(list(result.items())[0:5])
print(dict(list(result.items())[0:5]))
sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key,value))