from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, x, y, size, maxit, initFuncParams, learnFuncParams, linOut): 
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/iris.csv'
    print(locals())
    result = wrapperv2.core(locals(), "mlp")
    result.mlp()
    file = result.parameter.getOutput()
    #with open(file) as pmml:
    #    return pmml.read()


def execute_post(dataset, x, y, size, maxit, initFuncParams, learnFuncParams, linOut):
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/iris.csv'
    result = wrapperv2.core(locals(), "mlp")
    result.mlp()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/mlp.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/mlp.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/mlp.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/mlp.jsonld") as file:
            return file.read()
