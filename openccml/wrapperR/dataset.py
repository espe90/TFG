import os.path
import csv
import pandas as pd
import re
import numpy as np

class Dataset():
	def __init__(self, dictionary, method):
		self.dictionary = dictionary
		self.method = method
		self.dataset = {}
		self.delimiter = {}
		self.parameters = {}
		self.outputPMML = ""
		self.checkAll()		

	'''
		Comprueba que la ruta especificada del dataset exista
	'''
	def checkDatasetExists(self):
		if not os.path.isfile(self.dataset['ruta']):
			raise Exception("El fichero pasado no existe en la ruta")

	'''
		Comprueba que se tenga permisos de lectura
	'''
	def checkReadPermission(self):
		if not os.access(self.dataset['ruta'], os.R_OK) :
			raise Exception("No tenemos permisos de lectura")

	'''
		Comprobamos si tiene header el dataset
	'''
	def checkHeader(self):
		dataset = self.readDataset()
		for a in dataset.columns:
			if(not self.instring(a)):
				raise Exception("No tenemos header")

	'''
		Expresion regular que comprueba si los header leidos son string(el valor válido) o un numero entero o float(en cual caso no habria header)
	'''
	def instring (self, headerValue):
		if re.match ('^\d+$', headerValue) or re.match ('^\d+\.\d+$', headerValue):
			return False			
		else:
			return True

	'''
		Lee el dataset 
	'''
	def readDataset(self):
		return pd.read_csv(self.dataset['ruta'], delimiter = ',')

	'''
		Chequea todas las funciones
	'''
	def checkAll(self):
		try:
			
			if self.method == "lm":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.getParametersDataset('formula')
				self.LMFunction()
				self.returnParsedParameters()
			if self.method == "cor":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.corFunction()
				self.returnParsedParameters()
			if self.method == "arima":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.arimaFunction()
				self.returnParsedParameters()
			if self.method == "autoarima":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.autoarimaFunction()
				self.returnParsedParameters()
			if self.method == "acf":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.acfFunction()
				self.returnParsedParameters()
			if self.method == "pacf":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.pacfFunction()
				self.returnParsedParameters()
			if self.method == "ccf":
				self.splitDatasetParameters('dataset1')
				self.splitDatasetParameters('dataset2')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.ccfFunction()
				self.returnParsedParameters()
			if self.method == "ets":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.etsFunction()
				self.returnParsedParameters()
			if self.method == "adftest":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.adftestFunction()
				self.returnParsedParameters()
			if self.method == "jarque":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.jarqueFunction()
				self.returnParsedParameters()
			if self.method == "shapiro":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.shapiroFunction()
				self.returnParsedParameters()
			if self.method == "box":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.boxFunction()
				self.returnParsedParameters()
			if self.method == "dtw":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.dtwFunction()
				self.returnParsedParameters()
			if self.method == "rf":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.getParametersDataset('formula')
				self.rfFunction()
				self.returnParsedParameters()
			if self.method=="predict":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.predictFunction()
			if self.method == "predictarima":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()
				self.predictarimaFunction()
				self.returnParsedParameters()
			if self.method == "predictlm":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()				
				self.getParametersDataset('formula')
				self.predictlmFunction()				
				self.returnParsedParameters()
			if self.method == "predictRF":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()				
				self.getParametersDataset('formula')
				self.predictRFFunction()				
				self.returnParsedParameters()
			if self.method == "predictMLP":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()				
				self.getParametersDataset('formula')
				self.predictMLPFunction()				
				self.returnParsedParameters()
			if self.method == "predictETS":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()			
				self.predictETSFunction()				
				self.returnParsedParameters()	
			if self.method == "predictRBF":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()			
				self.predictRBFFunction()				
				self.returnParsedParameters()
			if self.method == "predictSVM":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()			
				self.predictSVMFunction()				
				self.returnParsedParameters()
			if self.method == "predictnnet":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()	
				self.getParametersDataset('formula')		
				self.predictnnetFunction()				
				self.returnParsedParameters()
			if self.method == "svm":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()				
				self.getParametersDataset('formula')
				self.svmFunction()				
				self.returnParsedParameters()
			if self.method == "stl":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()		
				self.stlFunction()				
				self.returnParsedParameters()			
			if self.method == "nnet":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()		
				self.nnetFunction()				
				self.returnParsedParameters()
			if self.method == "neuralnet":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()		
				self.neuralnetFunction()				
				self.returnParsedParameters()
			if self.method == "rbf":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()		
				self.rbfFunction()				
				self.returnParsedParameters()
			if self.method == "mlp":
				self.splitDatasetParameters('dataset')
				self.checkDatasetExists()
				self.checkReadPermission()
				self.checkHeader()		
				self.mlpFunction()				
				self.returnParsedParameters()
	
			self.outputPMML=self.setOutput()

		except Exception:
			raise Exception("Fallo en el checkeo global")

	'''
		Parsea los parametros que tengan __ por . y construye los parametros con clave=valor
	'''
	def returnParsedParameters(self):
		d = ''
		for key, value in self.parameters.items():
			if value != 'NULL':
				d += key.replace("__", ".") + ' = ' + value + ','

		self.parameters = d[:-1]

	'''
		Desgrana el campo formula para que los nombres de las columnas puedan ser leidas en formato array
	'''
	def getParametersDataset(self, field):
		dataset = self.readDataset()
		formula = re.split('-|/|~|\+', self.parameters[field])
		return formula


	'''
		Comprueba los campos que necesita la función en cuestion (Regresión Lineal) con los parametros pasados, 
		además comprobamos si estos parametros pueden o no pueden ser nulos y si son opcionales u obligatorios.
	'''
	def generalFunction(self, campos):
		#Campos de la funcion LM
		
		#lectura del dataset
		dataset = self.readDataset()

		for campo in campos:	
			#Si es obligatorio comprobamos los campos tanto en el dataset(formula), como en los parametros de entrada
			if campo[1] == 'obligatory':
				#Compruebo los campos de la funcion con los parametros pasados al servicio web
				if campo[0] not in self.parameters.keys():
					raise Exception ("No existe ese campo en los parametros pasados " + campo[0])

				#Si el campo es formula comprobamos que los campos internos de formula esten en el dataset pasado
				elif campo[0] == 'formula':
					param = self.getParametersDataset('formula')
					algo = [False for a in param if a not in dataset.columns]
					if False in algo:
						raise Exception ("No existen esas columnas")
			#Cuando es opcional comprobamos solo los parametros de entrada con los campos
			elif campo[1] == 'opcional':
				if campo[0] not in self.parameters.keys():
					raise Exception ("No existe ese campo en los parametros pasados " , campo[0])


			#Comprueba si los parametros pasados pueden ser null o no. En caso de no poderlo ser lanza una excepción
			if campo[2] == 'not null':
				if not self.parameters[campo[0]] or self.parameters[campo[0]] == 'NULL':
					raise Exception ("No puede ser el parametro " + campo[0] + " null ")

		if len(self.parameters) > len(campos):
			raise Exception ("Se enviaron mas parámetros de los que corresponden")

	def LMFunction(self):
		campos = [
			('formula', 'obligatory', 'not null'),
			('subset', 'optional', 'null'),
			('weights', 'optional', 'null'),
			('na__action', 'optional', 'null')
		]
		self.generalFunction(campos)

	'''
		ALmacena el nombre del dataset sin la extension y añadiendole la extension pmml donde se guardara el modelo 
	'''
	def setOutput(self):
		if self.method == "lm":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "cor":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "arima":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "autoarima":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "acf":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "pacf":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "ccf":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "ets":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "adftest":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "jarque":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "shapiro":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "box":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "dtw":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "rf":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "predict":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "predictarima":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "predictlm":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "predictRF":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "predictMLP":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "predictETS":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "predictRBF":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "predictSVM":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "predictnnet":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "svm":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "stl":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "nnet":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "neuralnet":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "rbf":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
		elif self.method == "mlp":
			return os.path.splitext(self.dataset['ruta'])[0] + '.pmml'
	'''
		Devuelve el nombre del fichero de salida PMML
	'''
	def getOutput(self):
		return self.outputPMML

	'''
		Divide el diccionario enviado en dos partes: 
			- Dataset con la ruta y el delimitador 
			- Parametros de entrada
		Asigna cada uno de estos en el correspondiente atributo
	'''
	def splitDatasetParameters(self, nameDataset):
		dataset = {}
		parameters = {}

		if nameDataset in self.dictionary.keys():
			dataset['ruta'] = self.dictionary[nameDataset]
			del self.dictionary[nameDataset]
			if 'delimiter' in self.dictionary.keys():
				dataset['delimiter'] = self.dictionary['delimiter']
				del self.dictionary['delimiter']
			else:
				dataset['delimiter'] = ''
		else:
			raise Exception ("No existe un dataset ")
		parameters = self.dictionary
		self.dataset = dataset
		self.parameters = parameters
		self.delimiter = dataset['delimiter']

	def corFunction(self):
		campos = [
			('x', 'obligatory', 'null'),
			('y', 'optional', 'null'),
			('use', 'optional', 'null'),
			('method', 'optional', 'null')
		]
		
	def arimaFunction(self):
		campos = [
			('x', 'optional', 'null'),
			('order', 'obligatory', 'null'),
			('seasonal', 'optional','null'),
			('xreg', 'optional','null'),
			('include__mean', 'optional','null'),
  			('transform__pars', 'optional','null'),
			('fixed', 'optional','null'),
			('init', 'optional','null'),
			('method', 'optional', 'null'),
			('optim__method', 'optional','null'),
			('optim__control', 'optional','null'),
			('kappa', 'optional','null')
		]
		self.generalFunction(campos)

	def autoarimaFunction(self):
		campos = [
			('y', 'optional', 'null'),
			('d', 'optional', 'null'),
			('D', 'optional','null'),
			('max__p', 'optional','null'),
			('max__q', 'optional','null'),
  			('max__P', 'optional','null'),
			('max__Q', 'optional','null'),
			('max__order', 'optional','null'),
			('max__d', 'optional', 'null'),
			('max__D', 'optional','null'),
			('start__p', 'optional','null'),
			('start__q', 'optional','null'),
			('start__P', 'optional','null'),
			('start__Q', 'optional','null'),
			('stationary', 'optional','null'),
			('seasonal', 'optional','null'),
			('ic', 'optional','null'),
			('stepwise', 'optional','null'),
			('trace', 'optional','null'),
			('approximation', 'optional','null'),
			('truncate', 'optional','null'),
			('xreg', 'optional','null'),
			('test', 'optional','null'),
			('seasonal__test', 'optional','null'),
			('allowdrift', 'optional','null'),
			('allowmean', 'optional','null'),
			('var_lambda', 'optional','null'),
			('biasadj', 'optional','null'),
			('parallel', 'optional','null'),
			('num__cores', 'optional','null')
		]
		self.generalFunction(campos)

	def acfFunction(self):
		campos = [
			('x', 'optional', 'null'),
			('lag__max', 'optional', 'null'),
			('var_type', 'optional','null'),
			('plot', 'optional','null'),
			('na__action', 'optional','null'),
  			('demean', 'optional','null')
		]
		self.generalFunction(campos)

	def pacfFunction(self):
		campos = [
			('x', 'optional', 'null'),
			('lag__max', 'optional', 'null'),
			('var_type', 'optional','null'),
			('plot', 'optional','null'),
			('na__action', 'optional','null'),
  			('demean', 'optional','null')
		]
		self.generalFunction(campos)

	def ccfFunction(self):
		campos = [
			('x', 'optional', 'null'),
			('y', 'optional', 'null'),
			('lag__max', 'optional', 'null'),
			('var_type', 'optional','null'),
			('plot', 'optional','null'),
			('na__action', 'optional','null'),
  			('demean', 'optional','null')
		]
		self.generalFunction(campos)

	def etsFunction(self):
		campos = [
			('y', 'optional', 'null'),
			('model', 'optional', 'null'),
			('damped', 'optional','null'),
			('var_alpha', 'optional','null'),
			('var_beta', 'optional','null'),
  			('var_gamma', 'optional','null'),
			('var_phi', 'optional','null'),
			('additive__only', 'optional','null'),
			('var_lambda', 'optional', 'null'),
			('biasadj', 'optional','null'),
			('lower', 'optional','null'),
			('upper', 'optional','null'),
			('opt__crit', 'optional','null'),
			('nmse', 'optional','null'),
			('bounds', 'optional','null'),
			('ic', 'optional','null'),
			('restrict', 'optional','null'),
			('allow__multiplicative__trend', 'optional','null'),
			('use__initial__values', 'optional','null')
		]
		self.generalFunction(campos)

	def adftestFunction(self):
		campos = [
			('x', 'optional', 'null'),
			('alternative', 'optional', 'null'),
			('k', 'optional','null')
		]
		self.generalFunction(campos)

	def jarqueFunction(self):
		campos = [
			('x', 'optional', 'null')
		]
		self.generalFunction(campos)
	
	def shapiroFunction(self):
		campos = [
			('x', 'optional', 'null')
		]
		self.generalFunction(campos)

	def boxFunction(self):
		campos = [
			('x', 'optional', 'null'),
			('lag', 'optional', 'null'),
			('var_type', 'optional', 'null'),
			('fitdf', 'optional', 'null')
		]
		self.generalFunction(campos)

	def dtwFunction(self):
		campos = [
			('x', 'optional', 'null'),
			('y', 'optional', 'null')
		]
		self.generalFunction(campos)

	def rfFunction(self):
		campos = [
			('formula', 'obligatory', 'null'),
			('na__action', 'optional', 'null'),
			('subset', 'optional', 'null'),
			('ntree', 'optional', 'null'),
			('mtry', 'optional', 'null'),
			('replace', 'optional', 'null'),
			('classwt', 'optional', 'null'),
			('cutoff', 'optional', 'null'),
			('strata', 'optional', 'null'),
			('sampsize', 'optional', 'null'),
			('nodesize', 'optional', 'null'),
			('maxnodes', 'optional', 'null'),
			('importance', 'optional', 'null'),
			('localImp', 'optional', 'null'),
			('nPerm', 'optional', 'null', ),
			('proximity', 'optional', 'null'),
			('oob__prox', 'optional', 'null'),
			('norm__votes', 'optional', 'null'),
			('keep__forest', 'optional', 'null'),
			('keep__inbag', 'optional', 'null')
		]

	def predictFunction(self):
		campos = [
			('model', 'optional', 'null')
		]

	def predictarimaFunction(self):
		campos = [
			('x', 'optional', 'null'),
			('order', 'optional', 'null')
		]
		self.generalFunction(campos)

	def predictlmFunction(self):
		campos = [
			('formula', 'optional', 'null')
		]
		self.generalFunction(campos)

	def predictRFFunction(self):
		campos = [
			('formula', 'optional', 'null')
		]
		self.generalFunction(campos)
	
	def predictMLPFunction(self):
		campos = [
			('formula', 'optional', 'null')
		]
		self.generalFunction(campos)

	def predictETSFunction(self):
		campos = [
			('formula', 'optional', 'null')
		]
		self.generalFunction(campos)
	
	def predictRBFFunction(self):
		campos = [
			('formula', 'optional', 'null')
		]
		self.generalFunction(campos)
	
	def predictSVMFunction(self):
		campos = [
			('formula', 'optional', 'null')
		]
		self.generalFunction(campos)

	def predictnnetFunction(self):
		campos = [
			('formula', 'optional', 'null')
		]
		self.generalFunction(campos)
	
	def svmFunction(self):
		campos = [
			('formula', 'obligatory', 'not null'),
			('na__action', 'optional', 'null')

		]
		
	
	def stlFunction(self):
		campos = [
			('x', 'obligatory', 'not null'),
			('s__window', 'optional', 'null'),
			('t__window', 'optional', 'null'),
			('t__jump', 'optional', 'null'),
			('robust', 'optional', 'null')

		]
	
	def nnetFunction(self):
		campos = [
			('formula', 'obligatory', 'not null'),
			('data', 'optional', 'null'),
			('subset', 'optional', 'null'),
			('na__action', 'optional', 'null'),
			('size', 'optional', 'null'),
			('rang', 'optional', 'null'),
			('decay', 'optional', 'null'),
			('maxit', 'optional', 'null')
		]

	def neuralnetFunction(self):
		campos = [
			('formula', 'obligatory', 'not null'),
			('data', 'optional', 'null'),
			('err__fct', 'optional', 'null'),
			('linear__output', 'optional', 'null'),
			('likelihood', 'optional', 'null')
		]
	
	def rbfFunction(self):
		campos = [
			('x', 'obligatory', 'not null'),
			('y', 'obligatory', 'not null'),
			('size', 'optional', 'null'),
			('maxit', 'optional', 'null'),
			('initFuncParams', 'optional', 'null'),
			('learnFuncParams', 'optional', 'null'),
			('linOut', 'optional', 'null')
		]
	def mlpFunction(self):
		campos = [
			('x', 'obligatory', 'not null'),
			('y', 'obligatory', 'not null'),
			('size', 'optional', 'null'),
			('maxit', 'optional', 'null'),
			('initFuncParams', 'optional', 'null'),
			('learnFuncParams', 'optional', 'null'),
			('linOut', 'optional', 'null')
		]

