#!/usr/bin/env python
#*********WARNING:********* Do not edit this directly, instead copy the file elsewhere and edit or find and edit the ipython file/Users/pmzrsg/source/hypothesis-examples/ Tests.ipynb
#!/usr/bin/env python
# coding: utf-8
 
#import numpy as np
import unittest
import importlib
import MyFunctions
#importlib.reload(MyFunctions) #ipython_only
 
#importlib.reload(MyFunctions) #ipython_only
class BasicTests(unittest.TestCase):
        
    def testMySqrt(self):
        root4 = MyFunctions.mySqrt( 4.0 )
        self.assertEqual(root4 , 2.0, "root 4 should be two")
#unittest.main(argv=['first-arg-is-ignored'], exit=False) #ipython_only
 
 
#importlib.reload(MyFunctions) #ipython_only
class TestBlank(unittest.TestCase):
    def testBlank(self):
        pass
        
#unittest.main(argv=['first-arg-is-ignored'], exit=False) #ipython_only 
 
unittest.main(argv=['first-arg-is-ignored'], exit=False)
 
 
