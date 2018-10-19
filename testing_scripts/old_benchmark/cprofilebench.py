# -*- coding: utf-8 -*-

import cProfile
import yaml
import json
import timeit
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object
from unmarshal_array import benchmark_array
from unmarshal_benchmark import benchmark
from unmarshal_nested import benchmark_nested
from unmarshal_inherited import benchmark_inherited

if __name__ == "__main__":
    setup_dict = []

    bench = benchmark_array()
    
    
    cProfile.run('bench.benchmark()')
    

