'''
What is this design pattern about?
-> This design pattern says that there should be a single inteface which should ideally kick off
set of processes. An example can be thought of as Switching on your computer systsem, where we press one 
button which internally kicks off multiple processes. 

'''

from __future__ import print_function
import time

SLEEP = 0.1

# complex functions. 
class TC1:
    
    def run(self):
        print(u"###### In Test 1 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")
        
class TC2:
    
    def run(self):
        print(u"###### In Test 2 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")
        
        
class TC3:
    
    def run(self):
        print(u"###### In Test 3 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")
        
        
#facade.
class TestRunner:
    
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]
        
    def runAll(self):
        [i.run() for i in self.tests]
        
#client

if __name__ == '__main__':
    testRunner = TestRunner()
    testRunner.runAll()