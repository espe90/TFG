from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, formula, na__action): 
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/iris.csv'
    print(locals())
    result = wrapperv2.core(locals(), "svm")
    result.svm()
    file = result.parameter.getOutput()
    #with open(file) as pmml:
    #    return pmml.read()


def execute_post(dataset, formula, na__action):
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/air.csv'
    result = wrapperv2.core(locals(), "svm")
    result.svm()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/svm.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/svm.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/svm.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/svm.jsonld") as file:
            return file.read()
