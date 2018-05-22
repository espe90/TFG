from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset,x, order,seasonal, xreg, include__mean, transform__pars, fixed, init, method, optim__method, optim__control, kappa): 
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/ts2.csv'
    print(locals())
    result = wrapperv2.core(locals(), "arima")
    result.arima()
    file = result.parameter.getOutput()
    #with open(file) as pmml:
    #    return pmml.read()


def execute_post(dataset,x, order,seasonal, xreg, include__mean, transform__pars, fixed, init, method, optim__method, optim__control, kappa):
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/ts2.csv'
    result = wrapperv2.core(locals(), "arima")
    result.arima()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/arima.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/arima.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/arima.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/arima.jsonld") as file:
            return file.read()
