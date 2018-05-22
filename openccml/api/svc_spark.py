from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, formula, x, max_iter): 
    locals()['dataset'] = '/root/TFG/openccml/datasets/titanic.csv'
    print(locals())
    result = wrapperv2.core(locals(), "svc_spark")
    result.svc_spark()
    file = result.parameter.getOutput()


def execute_post(dataset, formula, x, max_iter):
    locals()['dataset'] = '/root/TFG/openccml/datasets/titanic.csv'
    result = wrapperv2.core(locals(), "svc_spark")
    result.svc_spark()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/svc_spark.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/svc_spark.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/svc_spark.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/svc_spark.jsonld") as file:
            return file.read()
