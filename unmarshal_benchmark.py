# -*- coding: utf-8 -*-

import cProfile
import yaml
import json
import pstats
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object

class benchmark:
    def __init__(self,data):
        
        self.animaldict = {'id': 1}
        with open('zoo.yaml','r') as f:
            self.raw_spec = yaml.load(f)
        self.data = data
        self.animal = self.raw_spec['definitions']['Animals']
        self.spec = Spec.from_dict(self.raw_spec,config = {'use_models' : True,})

    def unmarshal__10k(self):
        spec_animal = unmarshal_schema_object(self.spec,self.animal,self.data)
        
        



if __name__ == "__main__":
    with open('animal10k.txt', 'r') as a:
        data =json.load(a)

    bench = benchmark(data)

    cProfile.run('bench.unmarshal__10k()','restats')
