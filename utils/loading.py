import yaml
import json
import os

from easydict import EasyDict


def load_config_from_yaml(path):
    """
    Method to load the config file for
    neural network training
    :param path: yaml-filepath with configs stored
    :return: easydict containing config
    """
    c = yaml.load(open(path))
    config = EasyDict(c)

    return config


def load_config_from_json(path):
    """
    Method to load the config file
    from json files.
    :param path: path to json file
    :return: easydict containing config
    """
    with open(path, 'r') as file:
        data = json.load(file)
    config = EasyDict(data)
    return config


def load_experiment(path):
    config = load_config_from_json(path)
    return config


def load_config(path):

    if path[-4:] == 'yaml':
        return load_config_from_yaml(path)
    elif path[-4:] == 'json':
        return load_config_from_json(path)
    else:
        raise ValueError('Unsupported file format for config')