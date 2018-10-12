# -*- coding: utf-8 -*-

import cProfile
import yaml
import _thread
import threading
import time
import json
import timeit
from unmarshal import benchmark


class testingThread(threading.Thread):
    
    def __init__(self,path1,path2):
        threading.Thread.__init__(self)
        self.path1 = path1
        self.path2 = path2

    def run(self):
        print("starting testing thread")
        self.test_benchmark()


    def test_benchmark(self):
        bench = benchmark(self.path1,self.path2)
        times = timeit.timeit(bench.unmarshal, number = 10)
        with open('./test.txt', 'a') as outfile:
            outfile.write('benchmark:' + self.path1 +':{}'.format(times))

        print('benchmark:' + self.path1 +':{}'.format(times))        



if __name__ == "__main__":
    threadpool = []
    paths = []
    with open('paths.txt', 'r') as f:
        paths = f.read().splitlines()
    
    
    for i in range(0,len(paths),2):
        thread = testingThread(paths[i], paths[i+1])
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

