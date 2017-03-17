import pandas as pd
import random
import statsmodels.api as sm
from sklearn import linear_model as lm

#change the path of the read.csv file to appropriate input file
df = pd.read_csv("/home/mindstorm/Desktop/hw45/Default.csv")

def simplelogistic(df):
    df.columns = ["default","student","balance","income"]
    logit = lm.LogisticRegression(penalty="l1",C=1)
    result = logit.fit(df[['income','balance']],df['default'])
    print 'Answer to part a:\nIntercept:',result.intercept_[0]
    print 'Coefficients:\nincome:',result.coef_[0][0]
    print 'balance:',result.coef_[0][0]

simplelogistic(df)

def validation(df,times=1):
    print '\n\nAnswer to part b:'
    for i in range(0,times):
        boolArray = []
        testSample = random.sample(range(0,len(df),1),int(0.5*len(df)))
        df.columns = ["default","student","balance","income"]
        for i in range(0,len(df)):
            if i in testSample:
                boolArray.append(True)
            else:
                boolArray.append(False)

        testData = df[boolArray]

        for i in range(0,len(boolArray)):
            boolArray[i] = not(boolArray[i])
        trainData = df[boolArray]

        #logit = sm.Logit(trainData['default'], trainData[['income','balance']])
        logit = lm.LogisticRegression(penalty="l1",C=1)
        result = logit.fit(df[['income','balance']],df['default'])
        predictions = (result.predict(testData[['income','balance']]))

        predictionsArray = []
        for x in predictions:
            predictionsArray.append(x)

        for i in range(0,len(predictionsArray)):
            if predictionsArray[i] > 0.5:
                predictionsArray[i] = int(1)
            else:
                predictionsArray[i] = int(0)

        errors = []

        for i in range(0,len(predictionsArray)):
            if predictionsArray[i] != testData['default'].iloc[i]:
                errors.append(1)

        testError = float(len(errors))/float(len(testData['default']))
        print 'train error:',testError

#df = pd.read_csv("/home/mindstorm/Desktop/hw45/Default.csv")
validation(df,3)


def validation1(df,times=1):
    print '\n\n'
    print 'Test error including student attribute'
    for i in range(0,times):
        boolArray = []
        testSample = random.sample(range(0,len(df),1),int(0.5*len(df)))
        df.columns = ["default","student","balance","income"]
        for i in range(0,len(df)):
            if i in testSample:
                boolArray.append(True)
            else:
                boolArray.append(False)

        testData = df[boolArray]

        for i in range(0,len(boolArray)):
            boolArray[i] = not(boolArray[i])
        trainData = df[boolArray]
        
        logit = lm.LogisticRegression(penalty="l1",C=1)
        result = logit.fit(df[['student','income','balance']],df['default'])
        
        predictions = (result.predict(testData[['student','income','balance']]))

        predictionsArray = []
        for x in predictions:
            predictionsArray.append(x)

        for i in range(0,len(predictionsArray)):
            if predictionsArray[i] > 0.5:
                predictionsArray[i] = int(1)
            else:
                predictionsArray[i] = int(0)

        errors = []

        for i in range(0,len(predictionsArray)):
            if predictionsArray[i] != testData['default'].iloc[i]:
                errors.append(1)

        testError = float(len(errors))/float(len(testData['default']))
        print 'train error:',testError

#df = pd.read_csv("/home/mindstorm/Desktop/hw45/Default.csv")
validation1(df,3)