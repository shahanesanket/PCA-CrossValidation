validationset1<- function(times=1)
{
  set.seed(100)
  library(ISLR)
  head(Default)
  dataset = Default
  logistic <- glm(default~income+balance,data=dataset,family=binomial)
  print(summary(logistic))
  if(times>=1)
  {
    for(i in seq(1,times,1))
    {
      train = sample(nrow(dataset),nrow(dataset)/2)
      
      trainlogistic <- glm(default~income+balance,data=dataset,family=binomial,subset = train)
      summary(trainlogistic)
      
      dataset.test = dataset[-train,]
      
      logistic.predictions = predict(trainlogistic,dataset.test,type="response")
      head(logistic.predictions)
      
      test.defaultlabels = dataset$default[-train]
      head(test.defaultlabels)
      
      test.prediction = rep("No",5000)
      test.prediction[logistic.predictions>0.5]='Yes'
      head(test.prediction)#this is the label after running the model on the test data
      
      table(test.prediction,test.defaultlabels)
      print("Test error:")
      print(mean(test.prediction != test.defaultlabels))
      
    }
  }
  #the above value is the test error
}

#the results obtained by running the model three times is more or less the same around 0.02 it vaires a little beyond that
#which is expected as validation set are randomly choosen and the model fit on the train data gives different results as
#the training data itself changes.


validationset1<- function(times=1)
{
  set.seed(100)
  library(ISLR)
  head(Default)
  dataset = Default
  logistic <- glm(default~income+balance+student,data=dataset,family=binomial)
  print(summary(logistic))
  if(times>=1)
  {
    for(i in seq(1,times,1))
    {
      train = sample(nrow(dataset),nrow(dataset)/2)
      
      trainlogistic <- glm(default~income+balance+student,data=dataset,family=binomial,subset = train)
      summary(trainlogistic)
      
      dataset.test = dataset[-train,]
      
      logistic.predictions = predict(trainlogistic,dataset.test,type="response")
      head(logistic.predictions)
      
      test.defaultlabels = dataset$default[-train]
      head(test.defaultlabels)
      
      test.prediction = rep("No",5000)
      test.prediction[logistic.predictions>0.5]='Yes'
      head(test.prediction)#this is the label after running the model on the test data
      
      table(test.prediction,test.defaultlabels)
      print("Test error:")
      print(mean(test.prediction != test.defaultlabels))
      
    }
  }
  #the above value is the test error
}

#the inclusion of student does not help much in reducing the test error.