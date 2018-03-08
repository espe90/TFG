from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, x, order): 
    locals()['dataset'] = '/home/espe/openccml/wrapperR/air.csv'
    print(locals())
    result = wrapperv2.core(locals(), "predictarima")
    result.predictarima()
    file = result.parameter.getOutput()
    #with open(file) as pmml:
    #    return pmml.read()


def execute_post(dataset, x, order):
    locals()['dataset'] = '/home/espe/openccml/wrapperR/air.csv'
    result = wrapperv2.core(locals(), "predictarima")
    result.predictarima()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/predictarima.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/predictarima.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/predictarima.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/predictarima.jsonld") as file:
            return file.read()
