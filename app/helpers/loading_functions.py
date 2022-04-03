#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Tue Sep 21 09:59:49 2022
@author: Géraldine Geoffroy
Automate the data harvest from remote url
"""
import pandas as pd
import json
import requests

def get_remote_csv(dataurl,csvsep=',',encoding='utf8'):
    df = pd.read_csv(dataurl,sep=csvsep,encoding='utf8')
    return df

def get_remote_simple_json(dataurl):
    resp = requests.get(dataurl).text
    data = json.loads(resp)
    df = pd.DataFrame(data)
    return df


def get_remote_nested_json(dataurl,depth=2):
    resp = requests.get(dataurl).text
    data = json.loads(resp)
    df = pd.json_normalize(data, max_level=depth)
    return df

def get_static_simple_json(file):
    df = pd.read_json(file)
    return df

def get_static_nested_json(file,depth=2):
    df = pd.json_normalize(file, max_level=depth)
    return df