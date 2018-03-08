from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset,x,lag__max,var_type,plot,na__action,demean): 
    locals()['dataset'] = '/home/espe/openccml/wrapperR/ts2.csv'
    print(locals())
    result = wrapperv2.core(locals(), "acf")
    result.acf()
    file = result.parameter.getOutput()


def execute_post(dataset,x,lag__max,var_type,plot,na__action,demean):
    locals()['dataset'] = '/home/espe/openccml/wrapperR/ts2.csv'
    result = wrapperv2.core(locals(), "acf")
    result.acf()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/acf.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/acf.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/acf.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/acf.jsonld") as file:
            return file.read()
