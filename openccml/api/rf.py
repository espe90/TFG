from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset, formula, na__action, subset, ntree, mtry, replace, classwt, cutoff, strata, sampsize, nodesize, maxnodes, importance, localImp, nPerm, proximity, oob__prox, norm__votes, keep__forest, keep__inbag): 
    print(locals())
    result = wrapperv2.core(locals(), "rf")
    result.rf()
    file = result.parameter.getOutput()


def execute_post(dataset, formula, na__action, subset, ntree, mtry, replace, classwt, cutoff, strata, sampsize, nodesize, maxnodes, importance, localImp, nPerm, proximity, oob__prox, norm__votes, keep__forest, keep__inbag):
    locals()['dataset'] = '/root/TFG/openccml/wrapperR/iris.csv'
    result = wrapperv2.core(locals(), "rf")
    result.rf()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/rf.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/rf.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/rf.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/rf.jsonld") as file:
            return file.read()
