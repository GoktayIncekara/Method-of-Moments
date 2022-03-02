import numpy as np
import matplotlib.pyplot as plt

p = 0.3
n = 40
 
def calculateMean(sampleList):      #It calculates the mean of a given list
    sum = 0
    for i in sampleList:
        sum += i
    mean = sum / len(sampleList)
    return mean

def calculateVariance(sampleList):          #It calculates the variance of a given list with the help of calculateMean function
    sampleMean = calculateMean(sampleList)
    variance = 0
    for i in sampleList:
        variance += ((sampleMean-i) ** 2)
    sampleVariance = variance / len(sampleList)
    return sampleVariance

def calculateStandardDeviation(sampleList):     #It calculates the standart deviation of a given list
    sampleStandardDeviation = (calculateVariance(sampleList) ** 0.5)
    return sampleStandardDeviation

def binomialDistribution(sampleSize):
    estimatedPList = []         #We will store our estimated p values in here
    estimatedNList = []         #We will store our estimated n values in here
    
    for i in range(1000):       #Experiment will be repeated 1000 times
        helper = []
        for j in range(sampleSize):
            binomialResults = []    #We will store our 1 and 0 values from the binomial distribution in here
            for k in range(n):
                u = np.random.rand()
                x = u<p
                binomialResults.append(int(x))
            binomialResultsSum = sum(binomialResults)      #We sum them
            helper.append(binomialResultsSum)              #Append the sum into the helper list
            
        sampleMean = calculateMean(helper)                  
        
        sampleVariance = calculateVariance(helper)
        
        estimatedP = 1 - (sampleVariance / sampleMean)  #Our estimated p value
        estimatedPList.append(estimatedP)
        
        estimatedN = sampleMean / estimatedP            #Our estimated n value
        estimatedNList.append(estimatedN)
        
    #After 1000 experiment has finished, we have 1000 estimated p and 1000 estimated in estimatedPList and estimatedNList accordingly
    estimatedPMean = calculateMean(estimatedPList)
    estimatedPStandartDeviation = calculateStandardDeviation(estimatedPList)
    estimatedNMean = calculateMean(estimatedNList)
    estimatedNStandartDeviation = calculateStandardDeviation(estimatedNList)
    
    print("Mean for estimated p for sample size of " + str(sampleSize)+ " is "+ str(estimatedPMean))
    print("Standard deviation for estimated p for sample size of " + str(sampleSize)+ " is "+ str(estimatedPStandartDeviation))
    print("Mean for estimated n for sample size of " + str(sampleSize)+ " is "+ str(estimatedNMean))
    print("Standard deviation for estimated n for sample size of " + str(sampleSize)+ " is "+ str(estimatedNStandartDeviation))
    
    return estimatedPList,estimatedNList

size200P, size200N = binomialDistribution(200)   #First one is estimatedPList and the second one is estimatedNList
size800P, size800N = binomialDistribution(800)
size3200P,size3200N = binomialDistribution(3200)
plt.figure()
plt.title("Histogram for estimated p")
plt.hist(size200P,bins =100,range = (0.1,0.5),label = '200', density=True)
plt.legend(loc = 'upper right')
plt.hist(size800P,bins =100,range = (0.1,0.5),label = '800', density=True)
plt.legend(loc = 'upper right')
plt.hist(size3200P,bins =100,range = (0.1,0.5),label = '3200', density=True)
plt.legend(loc = 'upper right')
plt.figure()
plt.title("Histogram for estimated n")
plt.hist(size200N,bins =100,range = (20,140),label = '200', density=True)
plt.legend(loc = 'upper right')
plt.hist(size800N,bins =100,range = (20,140),label = '800', density=True)
plt.legend(loc = 'upper right')
plt.hist(size3200N,bins =100,range = (20,140),label = '3200', density=True)
plt.legend(loc = 'upper right')
plt.show()


    
    
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
