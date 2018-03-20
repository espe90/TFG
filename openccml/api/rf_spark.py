from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, formula, num_trees, x, max_depth): 
    print(locals())
    result = wrapperv2.core(locals(), "rf_sparkR")
    result.rf_sparkR()
    file = result.parameter.getOutput()


def execute_post(dataset, formula, num_trees, x, max_depth):
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/iris.csv'
    result = wrapperv2.core(locals(), "rf_sparkR")
    result.rf_sparkR()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/rf_sparkR.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/rf_sparkR.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/rf_sparkR.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/rf_sparkR.jsonld") as file:
            return file.read()
