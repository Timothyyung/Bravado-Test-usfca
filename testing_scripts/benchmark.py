# -*- coding: utf-8 -*-

import cProfile
import yaml
import json
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object
from unmarshal_array import benchmark_array
from unmarshal_benchmark import benchmark


if __name__ == "__main__":
    bench = benchmark_array()
    bench.benchmark()
    bench = benchmark()
    bench.unmarshal__10k()
