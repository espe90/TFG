from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, x, s__window, t__window, t__jump, robust): 
    locals()['dataset'] = '/home/espe/openccml/wrapperR/nottem.csv'
    print(locals())
    result = wrapperv2.core(locals(), "stl")
    result.stl()
    file = result.parameter.getOutput()
    #with open(file) as pmml:
    #    return pmml.read()


def execute_post(dataset, x, s__window, t__window, t__jump, robust):
    locals()['dataset'] = '/home/espe/openccml/wrapperR/nottem.csv'
    result = wrapperv2.core(locals(), "stl")
    result.stl()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/stl.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/stl.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/stl.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/stl.jsonld") as file:
            return file.read()
