#!/bin/bash
#git clone https://github.com/Timothyyung/bravado-opt-usfca.git
python get_branches.py

while read branch
do
	./benchmark.py
done < branches.txt



#rm -rf bravado-opt-usfca
