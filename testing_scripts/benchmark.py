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

    setup_dict.append("""
from unmarshal_nested import benchmark_nested
bench = benchmark_nested()""")
    
    setup_dict.append("""
from unmarshal_array import benchmark_array
bench = benchmark_array()""")

    setup_dict.append("""
from unmarshal_benchmark import benchmark
bench = benchmark()""")

    setup_dict.append("""
from unmarshal_inherited import benchmark
bench = benchmark_inherited()""")

    func = 'bench.benchmark()'
    
    for set_up in setup_dict:
        times = timeit.timeit(stmt=func, setup=set_up, number=10)
        print('benchmark {}'.format(times))
