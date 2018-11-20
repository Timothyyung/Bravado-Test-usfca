# -*- coding: utf-8 -*-

import csv
import sys
import yaml
import timeit

def write_csv(result):
    with open('result/' + sys.argv[1] + '.csv', mode='w') as csv_file:
        fieldnames = ['array', 'array_primitives', 'nested', 'inherited']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(result)

def calculate_avg(result):
    total = 0.0
    result.sort()

    for i in range(3):
        total += result[i];
    return total / 3

if __name__ == "__main__":
    setup_dict = {}

    setup_dict['array'] = """
from unmarshal_array import benchmark_array
bench = benchmark_array()"""

    setup_dict['array_primitives'] = """
from unmarshal_array_primitives import benchmark_array_primitives
bench = benchmark_array_primitives()"""

    setup_dict['nested'] = """
from unmarshal_nested import benchmark_nested
bench = benchmark_nested()"""

    setup_dict['inherited'] = """
from unmarshal_inherited import benchmark_inherited
bench = benchmark_inherited()"""


    result = {}
    func = 'bench.benchmark()'

    if len(sys.argv) == 2:
        for key in setup_dict:
            times = timeit.repeat(stmt=func, setup=setup_dict[key], number=1, repeat=3)
            #print(times)
            result[key] = calculate_avg(times)
            print('benchmark {} spec {}'.format(key, result[key]))
        write_csv(result)
    elif len(sys.argv) == 3:
        #print(sys.argv[1])
        times = timeit.repeat(stmt=func, setup=setup_dict[sys.argv[2]], number=1, repeat=10)
        result[sys.argv[2]] = calculate_avg(times)
        print('benchmark {} spec {}'.format(sys.argv[2], result[sys.argv[2]]))
    else:
        print("<branch><type>")
