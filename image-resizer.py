#!/usr/bin/env python3

from PIL import Image
import sys

class picture():
    def __init__(self,name):
        self.file = Image.open(name)
        self.h = self.file.size[1]
        self.w = self.file.size[0]
        self.d = self.file.info['dpi'][0]

    def resizeto(self,value):
        if self.h>1.5*self.w:
            sys.exit("%s est trop grand : refaire une capture"%current_height)
        ratio = value/2.54*self.d
        self.file.resize((int(self.w/ratio), int(self.h/ratio)), Image.ANTIALIAS)
        self.file.save(sys.argv[1], dpi=(self.d,self.d))

if __name__=="__main__":
    file = picture(sys.argv[1])
    file.resizeto(8)
        
