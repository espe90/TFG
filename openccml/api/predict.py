from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, model): 
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/models/arima.rds'
    print(locals())
    result = wrapperv2.core(locals(), "predict")
    result.predict()
    file = result.parameter.getOutput()
    #with open(file) as pmml:
    #    return pmml.read()


def execute_post(dataset, model):
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/models/arima.rds'
    result = wrapperv2.core(locals(), "predict")
    result.predict()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/predict.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/predict.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/predict.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/predict.jsonld") as file:
            return file.read()
