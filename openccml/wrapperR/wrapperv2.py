# Copyright 2017 DiCITS UGR
# Author: Manuel Parra, Ruben Castro, Esperanza Jimenez
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""RWrapper"""

import csv
import rpy2.robjects as ro
from dataset import *
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
import pandas as pd



class core:

	"""
	Package CORE of R. Includes methods from the CORE of R, and not included on additional Packages
	"""
	

	def __init__(self, dictionary, method):
		self.parameter = Dataset(dictionary, method)
	
	def lm (self):
		lm = ro.r("""
			
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
	        	resultfit = lm({1}, data=dataset)
	        	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/lm.rds")
			capture.output(resultfit, file ="lm.txt")	        	
			print(resultfit)
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def cor(self):
		cor = ro.r("""
			dataset = read.csv(file="{0}", header = TRUE, sep=',')			
			resultfit = cor(x=dataset$mpg,y=dataset$disp)
	        	saveRDS(resultfit, file ="/root/TFG/openccml/models/cor.rds")
			capture.output(resultfit, file ="cor.txt")	        	
			print(resultfit)
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def arima(self):
		arima = ro.r("""
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
	        	resultfit = arima({1}, x=dataset)
			saveRDS(resultfit, file ="/root/TFG/openccml/models/arima.rds")
			capture.output(resultfit, file ="arima.txt")
			print(resultfit)
					
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def autoarima(self):
		autoarima = ro.r("""
			library("forecast")			
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
	        	resultfit = auto.arima(y=dataset)
			saveRDS(resultfit, file ="/root/TFG/openccml/models/autoarima.rds")
			capture.output(resultfit, file ="autoarima.txt")
			print(resultfit)					
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))
	
	def acf(self):
		acf = ro.r("""
			library("forecast")			
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
			jpeg("acf.jpeg")
	        	resultfit = Acf(x=dataset)
			dev.off()
			plot(resultfit)
			capture.output(resultfit, file ="acf.txt")			
			print(resultfit)					
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def pacf(self):
		pacf = ro.r("""
			library("forecast")			
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
			jpeg("pacf.jpeg")
	        	resultfit = Pacf(x=dataset)
			dev.off()
			plot(resultfit)
			capture.output(resultfit, file ="pacf.txt")
			print(resultfit)					
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def ccf(self):
		ccf = ro.r("""
			library("forecast")			
			dataset1 = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset2 = read.csv(file="{1}", header = TRUE, sep=' ')
			x=dataset1[,1]
			y=dataset2[,1]
			jpeg("ccf.jpeg")
	        	resultfit = Ccf(x,y)
			dev.off()
			plot(resultfit)
			capture.output(resultfit, file ="ccf.txt")
			print(resultfit)					
     	""".format(self.parameter.dataset['ruta'], self.parameter.dataset['ruta'],self.parameter.parameters, self.parameter.outputPMML))
	
	def ets(self):
		ets = ro.r("""
			library("forecast")			
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
	        	resultfit = ets(y=dataset)
			saveRDS(resultfit, file ="/root/TFG/openccml/models/ets.rds")
			capture.output(resultfit, file ="ets.txt")
			print(resultfit)					
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))	
	
	def adftest(self):
		adf_test = ro.r("""
			library("tseries")			
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
	        	resultfit = adf.test(x=dataset)
			capture.output(resultfit, file ="ets.txt")
			print(resultfit)					
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def jarque(self):
		jarque = ro.r("""
			library("tseries")			
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
	        	resultfit = jarque.bera.test(x=dataset)
			capture.output(resultfit, file ="jarque.txt")
			print(resultfit)					
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))
	
	def shapiro(self):
		shapiro = ro.r("""			
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
	        	resultfit = shapiro.test(x=dataset)
			capture.output(resultfit, file ="shapiro.txt")
			print(resultfit)					
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))	

	def box(self):
		box = ro.r("""		
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
	        	resultfit = Box.test(x=dataset)
			capture.output(resultfit, file ="box.txt")
			print(resultfit)				
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def dtw(self):
		dtw = ro.r("""
			library("dtw")
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset1=dataset[,1]
			dataset2=dataset[,2]
	        	resultfit = dtw(x=dataset1,y=dataset2)
			jpeg("dtw.jpeg")
			plot(resultfit$index1,resultfit$index2,main="Warping function")
			dev.off()
			capture.output(resultfit, file ="dtw.txt")	
			print(resultfit)				
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))
	
	def rf(self):
		rf = ro.r("""
			library("randomForest")
			library("r2pmml")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			set.seed(71)
			resultfit = randomForest({1},data=dataset,importance=TRUE,proximity=TRUE)
			r2pmml(resultfit, file ="/root/TFG/openccml/pmmls/rf.pmml")
			saveRDS(resultfit, file ="/root/TFG/openccml/models/rf.rds")
			capture.output(resultfit, file ="rf.txt")
			print(resultfit)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))
	
	def svm(self):
		svm = ro.r("""
			library("e1071")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			resultfit = svm({1}, data = dataset)
			saveRDS(resultfit, file ="/root/TFG/openccml/models/svm.rds")
			capture.output(resultfit, file ="svm.txt")
			print(resultfit)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def stl(self):
		stl = ro.r("""
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			values=dataset[,1]
			serie=ts(values,frequency=12)
			model=stl(serie,{1})
			plot(model)
			jpeg("stl.jpeg")
			plot(model)
			dev.off()
			saveRDS(model, file ="/root/TFG/openccml/models/stl.rds")
			capture.output(model, file ="stl.txt")
			print(model)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def nnet(self):
		nnet = ro.r("""
			library("nnet")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			set.seed(101)
			indices = sample(1:nrow(dataset),size=105)
			train = dataset[indices,]
			model=nnet({1}, data = train, decay = 5e-4, trace=F)
			saveRDS(model, file ="/root/TFG/openccml/models/nnet.rds")
			capture.output(model, file ="nnet.txt")
			print(model)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def neuralnet(self):
		neuralnet = ro.r("""
			library("neuralnet")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			head(dataset)
			trainset = dataset[1:800, ] 
			model=neuralnet({1}, trainset)
			saveRDS(model, file ="/root/TFG/openccml/models/neuralnet.rds")
			capture.output(model, file ="neuralnet.txt")
			plot(model, rep = "best")
			jpeg("nn.jpeg")
			plot(model, rep = "best")
			dev.off()
			print(model)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))
	
	def rbf(self):
		rbf = ro.r("""
			library("RSNNS")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			data = dataset[sample(nrow(iris)),]
			Values = data[,1:4]
			Targets = decodeClassLabels(data[,5])
			data = splitForTrainingAndTest(Values, Targets, ratio=0.15)
			data = normTrainingAndTestSet(data)
			model = rbf(data$inputsTrain, data$targetsTrain, {1}, maxit=200)
			summary(model)
			jpeg("rbf.jpeg")
			plotIterativeError(model)
			dev.off()
			plotIterativeError(model)			
			saveRDS(model, file ="/root/TFG/openccml/models/rbf.rds")
			capture.output(model, file ="rbf.txt")
			print(model)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def mlp(self):
		mlp = ro.r("""
			library("RSNNS")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			data = dataset[sample(1:nrow(dataset),length(1:nrow(dataset))),1:ncol(dataset)]
			Values = data[,1:4]
			Targets = decodeClassLabels(data[,5])
			data = splitForTrainingAndTest(Values, Targets, ratio=0.15)
			data = normTrainingAndTestSet(data)
			model = mlp(data$inputsTrain, data$targetsTrain, {1}, maxit=50, learnFuncParams=c(0.1))
			summary(model)
			jpeg("mlp.jpeg")
			plotIterativeError(model)
			dev.off()
			plotIterativeError(model)			
			saveRDS(model, file ="/root/TFG/openccml/models/mlp.rds")
			capture.output(model, file ="mlp.txt")
			print(model)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def predict(self):
		predict = ro.r("""	
			dataset = readRDS(file="{0}")		
			resultfit = predict(dataset,n.ahead=12)	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/predict.rds")	
			capture.output(resultfit, file ="predict.txt")	
			print(resultfit)	
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def predictarima(self):
		predictarima = ro.r("""	
			dataset = read.csv(file="{0}", header = TRUE, sep=',')		
			dataset = dataset[,3]
			model = arima(x=dataset, {1})
			saveRDS(model, file ="/root/TFG/openccml/models/arima.rds")
			print(model)
			resultfit = predict(model,n.ahead=12)	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/predictarima.rds")	
			capture.output(resultfit, file ="predictarima.txt")
			print(resultfit)
							
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def predictlm(self):
		predictlm = ro.r("""	
			dataset = read.csv(file="{0}", header = TRUE, sep=',')		
			model = lm(data=dataset,"{1}")
			saveRDS(model, file ="/root/TFG/openccml/models/lm.rds")
			print(model)
			resultfit = predict(model)	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/predictlm.rds")
			capture.output(resultfit, file ="predictlm.txt")	
			print(resultfit)							
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def predictRF(self):
		predictRF = ro.r("""
			library("randomForest")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			set.seed(71)
			model = randomForest({1},data=dataset,importance=TRUE,proximity=TRUE)
			saveRDS(model, file ="/root/TFG/openccml/models/rf.rds")
			print(model)
			resultfit = predict(model)	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/predictRF.rds")
			capture.output(resultfit, file ="predictRF.txt")	
			print(resultfit)							
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))
	
	def predictMLP(self):
		predictMLP = ro.r("""
			library("RSNNS")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			data = dataset[sample(1:nrow(dataset),length(1:nrow(dataset))),1:ncol(dataset)]
			Values = data[,1:4]
			Targets = decodeClassLabels(data[,5])
			data = splitForTrainingAndTest(Values, Targets, ratio=0.15)
			data = normTrainingAndTestSet(data)
			model = mlp(data$inputsTrain, data$targetsTrain, {1}, maxit=50, learnFuncParams=c(0.1))
			summary(model)
			saveRDS(model, file ="/root/TFG/openccml/models/mlp.rds")
			print(model)
			resultfit = predict(model)	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/predictMLP.rds")
			capture.output(resultfit, file ="predictMLP.txt")	
			print(resultfit)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def predictETS(self):
		predictETS = ro.r("""
			library("forecast")			
			dataset = read.csv(file="{0}", header = TRUE, sep=' ')
			dataset=dataset[,1]
	        	model = ets(y=dataset)
			saveRDS(model, file ="/root/TFG/openccml/models/ets.rds")
			print(model)
			resultfit = predict(model)	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/predictETS.rds")
			capture.output(resultfit, file ="predictETS.txt")	
			print(resultfit)					
     	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def predictRBF(self):
		predictRBF = ro.r("""
			library("RSNNS")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			data = dataset[sample(nrow(iris)),]
			Values = data[,1:4]
			Targets = decodeClassLabels(data[,5])
			data = splitForTrainingAndTest(Values, Targets, ratio=0.15)
			data = normTrainingAndTestSet(data)
			model = rbf(data$inputsTrain, data$targetsTrain, {1}, maxit=200)
			summary(model)
			saveRDS(model, file ="/root/TFG/openccml/models/rbf.rds")
			capture.output(model, file ="rbf.txt")
			print(model)
			resultfit = predict(model)	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/predictRBF.rds")
			capture.output(resultfit, file ="predictRBF.txt")	
			print(resultfit)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def predictSVM(self):
		predictSVM = ro.r("""
			library("e1071")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			model = svm({1}, data=dataset)
			saveRDS(model, file ="/root/TFG/openccml/models/svm.rds")
			capture.output(model, file ="svm.txt")
			print(model)
			resultfit = predict(model)	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/predictSVM.rds")
			capture.output(resultfit, file ="predictSVM.txt")	
			print(resultfit)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def predictnnet(self):
		predictnnet = ro.r("""
			library("nnet")
			dataset = read.csv(file="{0}", header = TRUE, sep=',')
			set.seed(101)
			indices = sample(1:nrow(dataset),size=105)
			train = dataset[indices,]
			model=nnet({1}, size=2, data = train, decay = 5e-4, trace=F)
			saveRDS(model, file ="/root/TFG/openccml/models/nnet.rds")
			capture.output(model, file ="nnet.txt")
			print(model)
			resultfit = predict(model)	
			saveRDS(resultfit, file ="/root/TFG/openccml/models/predictnnet.rds")
			capture.output(resultfit, file ="predictnnet.txt")	
			print(resultfit)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def rf_spark(self):
		rf_spark = ro.r("""
			library(sparklyr)
			sc <- spark_connect(master="local")
			df <- spark_read_csv(sc,"table","{0}",overwrite=TRUE)
			print(df)
			model <- ml_random_forest(df,{1})
			print(model)
			saveRDS(model, file ="/root/TFG/openccml/models/rf_spark.rds")
			capture.output(model, file ="rf_spark.txt")
			spark_disconnect(sc)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def lr_spark(self):
		lr_spark = ro.r("""
			library(sparklyr)
			sc <- spark_connect(master="local")
			df <- spark_read_csv(sc,"table","{0}",overwrite=TRUE)
			print(df)
			model <- ml_linear_regression(df,{1})
			print(model)
			saveRDS(model, file ="/root/TFG/openccml/models/lr_spark.rds")
			capture.output(model, file ="lr_spark.txt")
			spark_disconnect(sc)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))

	def svc_spark(self):
		svc_spark = ro.r("""
			library(sparklyr)
			sc <- spark_connect(master="local")
			df <- spark_read_csv(sc,"table","{0}",overwrite=TRUE)
			print(df)
			model <- ml_linear_svc(df,{1})
			print(model)
			saveRDS(model, file ="/root/TFG/openccml/models/svc_spark.rds")
			capture.output(model, file ="svc_spark.txt")
			spark_disconnect(sc)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))
	
	def mlp_spark(self):
		mlp_spark = ro.r("""
			library(sparklyr)
			sc <- spark_connect(master="local")
			df <- spark_read_csv(sc,"table","{0}",overwrite=TRUE)
			print(df)
			model <- ml_multilayer_perceptron(df,{1})
			print(model)
			saveRDS(model, file ="/root/TFG/openccml/models/mlp_spark.rds")
			capture.output(model, file ="mlp_spark.txt")
			spark_disconnect(sc)
	""".format(self.parameter.dataset['ruta'], self.parameter.parameters, self.parameter.outputPMML))


#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv','formula': 'species~petal_width','layers':'c(1,2,3)'}
#p = core(entrada, "mlp_spark")
#p.mlp_spark()

#entrada = {'dataset': '/root/TFG/openccml/datasets/titanic.csv','formula': 'Survived~.}
#p = core(entrada, "svc_spark")
#p.svc_spark()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv','formula': 'species~petal_width'}
#p = core(entrada, "lr_spark")
#p.lr_spark()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv','formula': 'species~petal_width'}
#p = core(entrada, "lm")
#p.lm()

#entrada = {'dataset': '/root/TFG/openccml/datasets/mtcars.csv'}
#p = core(entrada, "cor")
#p.cor()
	
#entrada = {'dataset': '/root/TFG/openccml/datasets/ts1.csv','order':'c(0,1,0)'}
#p = core(entrada, "arima")
#p.arima()

#entrada = {'dataset': '/root/TFG/openccml/datasets/datos.csv'}
#p = core(entrada, "dtw")
#p.dtw()

#entrada = {'dataset':'/root/TFG/openccml/datasets/ts1.csv'}
#p = core(entrada, "ets")
#p.ets()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv','formula':'species~.'}
#p = core(entrada, "rf")
#p.rf()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv', 'formula': 'species~.', 'na__action' :'na.omit'}
#p = core(entrada, "svm")
#p.svm()

#entrada = {'dataset': '/root/TFG/openccml/datasets/nottem.csv', 's__window': '"periodic"', 'robust': 'TRUE'}
#p = core(entrada, "stl")
#p.stl()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv', 'formula': 'species~.','size':'2'}
#p = core(entrada, "nnet")
#p.nnet()

#entrada = {'dataset': '/root/TFG/openccml/datasets/creditset.csv', 'formula': 'default10yr ~ LTI + age'}
#p = core(entrada, "neuralnet")
#p.neuralnet()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv', 'size':'40'}
#p = core(entrada, "rbf")
#p.rbf()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv', 'size':'5'}
#p = core(entrada, "mlp")
#p.mlp()

#entrada={'dataset':'/root/TFG/openccml/models/arima.rds'}
#p= core(entrada, "predict")
#p.predict()

#entrada = {'dataset': '/root/TFG/openccml/datasets/air.csv','order':'c(0,1,0)'}
#p = core(entrada, "predictarima")
#p.predictarima()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv','formula':'species~petal_width'}
#p = core(entrada, "predictlm")
#p.predictlm()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv','formula':'species~.'}
#p = core(entrada, "predictRF")
#p.predictRF()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv','formula':'species~.'}
#p = core(entrada, "predictMLP")
#p.predictMLP()

#entrada = {'dataset':'/root/TFG/openccml/datasets/ts1.csv'}
#p = core(entrada, "predictETS")
#p.predictETS()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv', 'size':'40'}
#p = core(entrada, "predictRBF")
#p.predictRBF()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv', 'formula': 'species~petal_width'}
#p = core(entrada, "predictSVM")
#p.predictSVM()

#entrada = {'dataset': '/root/TFG/openccml/datasets/iris.csv', 'formula': 'species~.'}
#p = core(entrada, "predictnnet")
#p.predictnnet()
