#!/bin/bash
git clone https://github.com/Timothyyung/bravado-opt-usfca.git
#python get_branches.py

while read branch
do
  echo "Switching branch to $branch."
  cd bravado-opt-usfca; git checkout $branch; cd ..;  pip install -e bravado-opt-usfca >/dev/null ; cd ..
	cd testing_scripts; python benchmark.py; cd ../bash_script
done < branches.txt

sudo rm -rf bravado-opt-usfca
