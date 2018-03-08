from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset,x): 
    locals()['dataset'] = '/home/espe/openccml/wrapperR/ts2.csv'
    print(locals())
    result = wrapperv2.core(locals(), "shapiro")
    result.shapiro()
    file = result.parameter.getOutput()


def execute_post(dataset,x):
    locals()['dataset'] = '/home/espe/openccml/wrapperR/ts2.csv'
    result = wrapperv2.core(locals(), "shapiro")
    result.shapiro()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/shapiro.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/shapiro.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/shapiro.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/shapiro.jsonld") as file:
            return file.read()
