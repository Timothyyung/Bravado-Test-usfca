# -*- coding: utf-8 -*-

import cProfile
import yaml
import _thread
import threading
import time
import json
import timeit
import csv
from unmarshal import benchmark


class testingThread(threading.Thread):
    
    def __init__(self,path1,path2,testid,bravado_version):
        threading.Thread.__init__(self)
        self.path1 = path1
        self.path2 = path2
        self.testid = testid
        self.bench = benchmark(self.path1,self.path2)
        self.bravado_version = bravado_version
        self.testsdata = []

    def run(self):
        for i in range(0,10):
            self.test_benchmark()
        self.create_csv()


    def test_benchmark(self):
        self.times = timeit.timeit(self.bench.unmarshal, number = 10)
        res = {'spec'  : self.path1,
                'times': self.times,
                'json_size' : self.bench.json_size(),
                'bravado_version': self.bravado_version}
        self.testsdata.append(res)
        print('benchmark:' + self.path1 +':{}'.format(self.times))        
    
    def create_csv(self):
        myFields = ['spec','times','json_size','bravado_version']

        myFile = open('test'+str(self.testid)+'.csv', 'w')
        with myFile:
            writer = csv.DictWriter(myFile, fieldnames=myFields)
            writer.writeheader()
            for tdata in self.testsdata:
                writer.writerow(tdata)



if __name__ == "__main__":
    threadpool = []
    paths = []
    with open('paths.txt', 'r') as f:
        paths = f.read().splitlines()
    
    
    for i in range(0,len(paths),2):
        thread = testingThread(paths[i], paths[i+1],i,"master")
        threadpool.append(thread)

    for thread in threadpool:
        thread.start()
    
    for thread in threadpool:
        thread.join()

"""
    for i in range(0,len(paths),2):
        bench = benchmark(paths[i],paths[i+1])
        #bench.unmarshal()
        print(paths[i], paths[i+1])
        times = timeit.timeit(bench.unmarshal,number=10)
        print('benchmark {}'.format(times))
"""

