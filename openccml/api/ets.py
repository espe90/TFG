from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset,y,model,damped,alpha,beta,gamma,phi,additive__only,var_lambda,biasadj,lower,upper,opt__crit,nmse,bounds,ic,restrict,allow__multiplicative__trend,use__initial__values):
    locals()['dataset'] = '/home/espe/openccml/wrapperR/ts2.csv'
    print(locals())
    result = wrapperv2.core(locals(), "ets")
    result.ets()
    file = result.parameter.getOutput()
 

def execute_post(dataset,y,model,damped,alpha,beta,gamma,phi,additive__only,var_lambda,biasadj,lower,upper,opt__crit,nmse,bounds,ic,restrict,allow__multiplicative__trend,use__initial__values):
    locals()['dataset'] = '/home/espe/openccml/wrapperR/ts2.csv'
    result = wrapperv2.core(locals(), "ets")
    result.ets()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/ets.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/ets.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/ets.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/ets.jsonld") as file:
            return file.read()
