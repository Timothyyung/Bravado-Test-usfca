#-*- coding: utf-8 -*-

import yaml, json, cProfile
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object



class benchmark_array:
        

    def __init__(self):
        with open('../specs/spec_array.yaml', 'r') as f:
            self.raw_spec = yaml.load(f)
        
        self.data = self.create_json()
        self.spec = Spec.from_dict(self.raw_spec)
        self.persons = self.raw_spec['definitions']['Persons']

       

    def create_json(self):
        with open('../jsondata/array10k.txt') as f:
            data = json.load(f)
        return data

    def benchmark(self):
        persons_obj = unmarshal_schema_object(self.spec, self.persons,self.data)
        #print (persons_obj)
 



