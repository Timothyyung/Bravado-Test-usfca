#-*- coding:utf-8 -*-

import yaml, json, cProfile
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object



class benchmark:
    def __init__(self,specpath,jsonpath):
        with open(specpath, 'r') as f:
            self.raw_spec = yaml.load(f)

        self.data = self.create_json(jsonpath)
        key = list(self.data.keys())
        self.spec = Spec.from_dict(self.raw_spec)
        self.obj = self.raw_spec['definitions'][key[0]]



    def create_json(self, jsonpath):
        with open(jsonpath) as f:
            data = json.load(f)
        return data


    def unmarshal(self):
        obj = unmarshal_schema_object(self.spec, self.obj,self.data)
        ###print (obj)
                 
