from pyspark import SparkContext

sc = SparkContext()

rawData=sc.textFile('/oasis/projects/nsf/sun116/addankn/forestdata/',5)


data = rawData.map(lambda x:list(map(int,x.split(',')))).map(lambda x: [Vectors.dense(x[:-1]),x[-1]-1])

from pyspark.mllib.regression import LabeledPoint

from pyspark.mllib.linalg import Vectors

import pyspark.mllib as mllib


data = rawData.map(lambda x:list(map(float,x.split(',')))).map(lambda x:LabeledPoint(x[-1]-1.0,Vectors.dense(list(map(int,x[:-1])))))
 
 
trainData,cvData,testData=data.randomSplit([0.8,0.1,0.1])

trainData.cache()
cvData.cache()
testData.cache()

from pyspark.mllib.tree import DecisionTree



model = DecisionTree.trainClassifier(trainData, numClasses=7, categoricalFeaturesInfo={},impurity='gini', maxDepth=5, maxBins=32)


from pyspark.mllib import evaluation

predictionstest=model.predict(testData.map(lambda x: x.features)).zip(testData.map(lambda x:x.label)).collect()

predictions=model.predict(cvData.map(lambda x: x.features)).zip(cvData.map(lambda x:x.label)).collect()

correctionpredictions = [1 if i[1]==i[0] else 0 for i in predictions]
correctionpredictionstest = [1 if i[1]==i[0] else 0 for i in predictionstest]

print "cv data precision={}".format(float(sum(correctionpredictions))/len(correctionpredictions))
print "test data precision={}".format(float(sum(correctionpredictionstest))/len(correctionpredictionstest))