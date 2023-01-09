#!/usr/bin/python
from configparser import ConfigParser


def config_db(filename='parameters.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def config_broker(filename='parameters.ini', section='broker'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    broker = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            broker[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return broker
