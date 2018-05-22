from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset,y,d,D,max__p,max__q,max__P,max__Q,max__order,max__d,max__D,start__p,start__q,start__P,start__Q,stationary,seasonal,ic,stepwise,trace,approximation,truncate,xreg,test,seasonal__test,allowdrift,allowmean,var_lambda,biasadj,parallel,num__cores): 
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/ts2.csv'
    print(locals())
    result = wrapperv2.core(locals(), "autoarima")
    result.autoarima()
    file = result.parameter.getOutput()
 

def execute_post(dataset,y,d,D,max__p,max__q,max__P,max__Q,max__order,max__d,max__D,start__p,start__q,start__P,start__Q,stationary,seasonal,ic,stepwise,trace,approximation,truncate,xreg,test,seasonal__test,allowdrift,allowmean,var_lambda,biasadj,parallel,num__cores):
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/ts2.csv'
    result = wrapperv2.core(locals(), "autoarima")
    result.autoarima()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/autoarima.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/autoarima.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/autoarima.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/autoarima.jsonld") as file:
            return file.read()
