#!/bin/bash
git clone https://github.com/Timothyyung/bravado-opt-usfca.git
#python get_branches.py

while read branch
do
  echo "$branch"
  cd bravado-opt-usfca; git checkout $branch; cd ..; pip3 install -e bravado-opt-usfca; cd ..
	cd testing_scripts; python benchmark.py; cd ../bash_script
done < branches.txt



#rm -rf bravado-opt-usfca
