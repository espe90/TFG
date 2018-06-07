from wrapperR import wrapperv2
from config.config import turtle_folder, jsonld_folder

def execute(dataset,train_file_name, min_len, max_len, step, Num_partitions, seed, tree_file_name, time_file_name, R, top_k, Classificator, shapelet_file_name, test_file_name, model_file_name): 
    locals()['dataset'] = '/root/TFG/openccml/datasets/iris.csv'
    print(locals())
    result = wrapperv2.core(locals(), "dfst")
    result.dfsr()
    file = result.parameter.getOutput()


def execute_post(dataset,train_file_name, min_len, max_len, step, Num_partitions, seed, tree_file_name, time_file_name, R, top_k, Classificator, shapelet_file_name, test_file_name, model_file_name): 
    locals()['dataset'] = '/root/TFG/openccmldatasets/iris.csv'
    result = wrapperv2.core(locals(), "dfst")
    result.dfst()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/dfst.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/dfst.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/dfst.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/dfst.jsonld") as file:
            return file.read()
