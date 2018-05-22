from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, x, formula, layers): 
    locals()['dataset'] = '/root/TFG/openccml/datasets/iris.csv'
    print(locals())
    result = wrapperv2.core(locals(), "mlp_spark")
    result.mlp_spark()
    file = result.parameter.getOutput()


def execute_post(dataset, x, formula, layers):
    locals()['dataset'] = '/root/TFG/openccml/datasets/iris.csv'
    result = wrapperv2.core(locals(), "mlp_spark")
    result.mlp_spark()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/mlp_spark.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/mlp_spark.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/mlp_spark.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/mlp_spark.jsonld") as file:
            return file.read()
