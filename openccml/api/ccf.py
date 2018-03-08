from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset1,dataset2,x,y,lag__max,var_type,plot,na__action,demean): 
    locals()['dataset1'] = '/home/espe/openccml/wrapperR/ts1.csv'
    locals()['dataset2'] = '/home/espe/openccml/wrapperR/ts2.csv'
    print(locals())
    result = wrapperv2.core(locals(), "ccf")
    result.ccf()
    file = result.parameter.getOutput()


def execute_post(dataset1,dataset2,x,y,lag__max,var_type,plot,na__action,demean):
    locals()['dataset1'] = '/home/espe/openccml/wrapperR/ts1.csv'
    locals()['dataset2'] = '/home/espe/openccml/wrapperR/ts2.csv'
    result = wrapperv2.core(locals(), "ccf")
    result.ccf()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/ccf.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/ccf.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/ccf.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/ccf.jsonld") as file:
            return file.read()
