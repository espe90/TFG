from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset,x,y): 
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/datos.csv'
    print(locals())
    result = wrapperv2.core(locals(), "dtw")
    result.dtw()
    file = result.parameter.getOutput()


def execute_post(dataset,x,y):
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/datos.csv'
    result = wrapperv2.core(locals(), "dtw")
    result.dtw()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/dtw.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/dtw.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/dtw.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/dtw.jsonld") as file:
            return file.read()
