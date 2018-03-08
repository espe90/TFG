from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, formula, data, subset, na__action, size, rang, decay, maxit): 
    locals()['dataset'] = '/home/espe/openccml/wrapperR/iris.csv'
    print(locals())
    result = wrapperv2.core(locals(), "nnet")
    result.nnet()
    file = result.parameter.getOutput()
    #with open(file) as pmml:
    #    return pmml.read()


def execute_post(dataset,formula, data, subset, na__action, size, rang, decay, maxit):
    locals()['dataset'] = '/home/espe/openccml/wrapperR/iris.csv'
    result = wrapperv2.core(locals(), "nnet")
    result.nnet()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/nnet.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/nnet.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/nnet.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/nnet.jsonld") as file:
            return file.read()
