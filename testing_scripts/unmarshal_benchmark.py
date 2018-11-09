# -*- coding: utf-8 -*-

import cProfile
import yaml
import json
import pstats
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object

class benchmark:
    def __init__(self):

        self.animaldict = {'id': 1}
        with open('../../specs/zoo.yaml','r') as f:
            self.raw_spec = yaml.load(f)
        self.data = self.create_json()
        self.animal = self.raw_spec['definitions']['Animals']
        self.spec = Spec.from_dict(self.raw_spec)

    def create_json(self):
        with open('../../jsondata/animal10k.txt','r') as a:
            data = json.load(a)
        return data

    def benchmark(self):
        spec_animal = unmarshal_schema_object(self.spec,self.animal,self.data)
        print (spec_animal)
