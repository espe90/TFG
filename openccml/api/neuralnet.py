from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, formula, data, err__fct, linear__output, likelihood): 
    locals()['dataset'] = '/home/espe/openccml/wrapperR/creditset.csv'
    print(locals())
    result = wrapperv2.core(locals(), "neuralnet")
    result.neuralnet()
    file = result.parameter.getOutput()
    #with open(file) as pmml:
    #    return pmml.read()


def execute_post(dataset,formula, data, err__fct, linear__output, likelihood):
    locals()['dataset'] = '/home/espe/openccml/wrapperR/creditset.csv'
    result = wrapperv2.core(locals(), "neuralnet")
    result.neuralnet()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/neuralnet.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/neuralnet.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/neuralnet.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/neuralnet.jsonld") as file:
            return file.read()
