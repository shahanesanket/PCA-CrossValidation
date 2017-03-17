library(pixmap)
#setwd("C:/Users/Sanket Shahane/Google Drive/MS/FDS/Homework/HW5/HW45R/faces-corrected")

#place the correct file path below
filenameList<-list.files("C:/Users/Sanket Shahane/Google Drive/MS/FDS/Homework/HW5/HW45R/faces-corrected")

imagesarray <- array(NA,dim=c(length(as.vector(getChannels(read.pnm(filenameList[1])))),length(filenameList)))

for(i in 1:length(filenameList)){
  imagesarray[,i] = as.vector(getChannels(read.pnm(filenameList[i])))
}

meanImage <- rowMeans(imagesarray)

i=1
for(i in 1:length(imagesarray[1,])){
  imagesarray[,i] <- imagesarray[,i] - meanImage
}

covariancematrix <- cov(imagesarray)

eigenVector <- eigen(covariancematrix)
eigenFaces <- matrix(NA,nrow = 45045,ncol = 10)

i=1
for(i in 1:10){
  eigenFaces[,i] <- imagesarray %*% eigenVector$vectors[,i]
}
i=1
for(i in 1:10){
  plot(pixmapGrey(matrix(eigenFaces[,i],nrow=231)))
}