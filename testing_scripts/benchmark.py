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

if __name__ == "__main__":
    set_up = """
from unmarshal_array import benchmark_array
bench = benchmark_array()"""

    func = 'bench.benchmark()'
    times = timeit.timeit(stmt=func, setup=set_up, number=10)
    print('benchmark_array(): {}'.format(times))
    #bench = benchmark()
    #bench.unmarshal__10k()
    #bench = benchmark_nested()
    #bench.benchmark()
