from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset,x,alternative,k): 
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/ts2.csv'
    print(locals())
    result = wrapperv2.core(locals(), "adftest")
    result.adftest()
    file = result.parameter.getOutput()


def execute_post(dataset,x,alternative,k):
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/ts2.csv'
    result = wrapperv2.core(locals(), "adftest")
    result.adftest()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/adftest.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/adftest.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/adftest.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/adftest.jsonld") as file:
            return file.read()
