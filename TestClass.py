# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 21:02:12 2014

@author: magnus

"""


class StuffPicker:

    def __init__(self,filename):        
        self.name = filename
        self.Goya = "hee"
    def getFileName(self):
        print self.name
        
   
   



a = StuffPicker('ola')
a.getFileName()