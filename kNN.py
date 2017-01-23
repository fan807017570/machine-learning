from numpy import *
import operator
import pdb
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
        group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
        labels=['A','A','B','B']
	return group,labels
def classify(inX,dataSet,labels,k):
        dataSetSize=dataSet.shape[0]
	diffMat=tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	print sqDistances
	distances=sqDistances**0.5
	print distances
	sortedDistances=distances.argsort()#the index of distance
	classCount={}
	for i in range (k):
		#pdb.set_trace()
		voteIlabel=labels[sortedDistances[i]]
		classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
	print classCount
def file2matrix(filename):
	fr=open(filename)
	arrayLines=fr.readlines()
	numberOfLines=len(arrayLines)
	matrix=zeros((numberOfLines,3))
	classLabelVector = []
	index=0
	for line in arrayLines:
		line = line.strip()
		listFromLine=line.split("\t")
		matrix[index:]=listFromLine[0:3]	
		classLabelVector.append(int(listFromLine[-1]))
		index+=1
	return matrix,classLabelVector
def autoNorm(dataSet):
	minVals	=dataSet.min(0)
	#print minVals
	maxVals=dataSet.max(0)
	#print maxVals
	ranges=maxVals-minVals
	normDataSet=zeros(shape(dataSet))
	m=dataSet.shape[0]
	normDataSet=dataSet-tile(minVals,(m,1))
	normDataSet=normDataSet/tile(ranges,(m,1))
	return normDataSet
if __name__=="__main__":
        print ("this is main of module ")
        #group,labels=createDataSet()
        #classify([0,0],group,labels,3)
	datingDataMatrix,datingLabels=file2matrix("datingTestSet2.txt");
	#print  datingDataMatrix
	#pdb.set_trace()
	ax1=autoNorm(datingDataMatrix[:,0])
	ax2=autoNorm(datingDataMatrix[:,1])
	print ax1 
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(ax1,ax2)
	plt.show()
	#print  datingLabels	
