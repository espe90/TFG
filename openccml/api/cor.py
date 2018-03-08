from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder


def execute(dataset, x, y, use, method):
    locals()['dataset'] = '/home/espe/openccml/datasets/mtcars.csv'
    print(locals())
    result = wrapperv2.core(locals(), "cor")
    result.cor()
    file = result.parameter.getOutput()

def execute_post(dataset, x, y, use, method):
    locals()['dataset'] = '/home/espe/openccml/dataset/mtcars.csv'
    result = wrapperv2.core(locals(), "cor")
    result.cor()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/cor.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/cor.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/cor.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/cor.jsonld") as file:
            return file.read()
