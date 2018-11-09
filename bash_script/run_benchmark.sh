#!/bin/bash
git clone https://github.com/Timothyyung/bravado-opt-usfca.git
#python get_branches.py

while read branch
do
  echo "Switching branch to $branch."
  cd bravado-opt-usfca; git checkout $branch; cd ..; pip3 install -e bravado-opt-usfca >/dev/null ; cd ..
	cd testing_scripts; python3 benchmark.py $branch; cd ../bash_script
done < branches.txt

rm -rf bravado-opt-usfca
rm -rf ../testing_scripts/old_benchmark/__pycache__
rm -rf ../testing_scripts/__pycache__