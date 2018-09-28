# -*- coding: utf-8 -*-

import yaml, json, cProfile
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object


def unmarshal_test(data):
    with open('./spec_array.yaml', 'r') as f:
        raw_spec = yaml.load(f)
    spec = Spec.from_dict(raw_spec)
    persons = raw_spec['definitions']['Persons']

    persons_obj = unmarshal_schema_object(spec, persons,data)
    print(persons_obj)

if __name__ == "__main__":
    with open('./jsondata/array10k.txt') as f:
        data = json.load(f)
    #unmarshal_test(data)
    cProfile.run('unmarshal_test(data)', sort='tottime')

