import yaml, json, cProfile
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object



class benchmark_inherited:
    def __init__(self):
        with open('../specs/spec_inherited.yaml', 'r') as f:
            self.raw_spec = yaml.load(f)

        self.data = self.create_json()
        self.spec = Spec.from_dict(self.raw_spec)
        self.petlist = self.raw_spec['definitions']['PetList']

   

    def create_json(self):
        with open('../jsondata/inherited10k.txt') as f:
            data = json.load(f)
        return data        


    def benchmark(self):    
        school_obj = unmarshal_schema_object(self.spec, self.petlist,self.data)
        #print (school_obj)
