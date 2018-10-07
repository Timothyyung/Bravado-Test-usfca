# -*- coding: utf-8 -*-

import cProfile
import yaml
import json
import timeit
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object
from unmarshal import benchmark

if __name__ == "__main__":
    setup_dict = []
    paths = []
    with open('paths.txt', 'r') as f:
        paths = f.read().splitlines()



    
    
    for i in range(0,len(paths),2):
        bench = benchmark(paths[i],paths[i+1])
        #bench.unmarshal()
        print(paths[i], paths[i+1])
        times = timeit.timeit(bench.unmarshal,number=10)
        print('benchmark {}'.format(times))

