import sys
import numpy
import random
import PyPluMA

class TSV2CSVPlugin:
   def input(self, filename):
      self.tsvfile = open(filename, 'r')

   def run(self):
      pass

   def output(self, filename):
      csvfile = open(filename, 'w')
      
      for tsvline in self.tsvfile:
         csvfile.write(tsvline.replace('\t',','))



