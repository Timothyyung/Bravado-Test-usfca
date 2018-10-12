#!/bin/bash

cd ../jsondata/json_generators
python3 animal.py $1
python3 make_array.py $1
python3 nested.py $1

