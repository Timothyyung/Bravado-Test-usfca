import yaml, json, cProfile
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object


def unmarshal_test(data):
    with open('../specs/spec_nested.yaml', 'r') as f:
        raw_spec = yaml.load(f)
    spec = Spec.from_dict(raw_spec)
    school = raw_spec['definitions']['School']

    school_obj = unmarshal_schema_object(spec, school,data)
    #print(school_obj)

if __name__ == "__main__":
    with open('../jsondata/nested10k.txt') as f:
        data = json.load(f)
    #unmarshal_test(data)
    cProfile.run('unmarshal_test(data)', sort='tottime')
