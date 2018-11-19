#-*- coding: utf-8 -*-

import yaml, json, cProfile
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object



class benchmark_array_primitives:
    def __init__(self):
        with open('../specs/spec_array_primitives.yaml', 'r') as f:
            self.raw_spec = yaml.load(f)

        self.data = self.create_json()
        self.spec = Spec.from_dict(self.raw_spec)
        self.guests = self.raw_spec['definitions']['Guests']



    def create_json(self):
        with open('../jsondata/array_primitives10k.txt') as f:
            data = json.load(f)
        return data

    def benchmark(self):
        guests_obj = unmarshal_schema_object(self.spec, self.guests, self.data)
        #print(guests_obj)
