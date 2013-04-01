'''
Created on Mar 30, 2013

@author: neymellosampaio
'''
import unittest


class TestUtil(unittest.TestCase):


        def readFile(self):
            from core.util import fileHandler
            
            fh = fileHandler()
            
            fh.readFile("../examples/TEST.DAT")
            
            self.