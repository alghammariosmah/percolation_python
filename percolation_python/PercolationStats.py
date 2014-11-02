__author__ = 'osamahal-ghammari'

import math
import percolation
import random

class PercolationStats:
    def __init__(self, N,T):
        self.N=N # grid NxN
        self.T=T #trails number

        def Percolation_test(): # we need to test whether the function percolates or not
            empty_list=[]
            Does_It_Percolate= percolation.Percolation(self.N) #testing percolation
            while not Does_It_Percolate.percolates(): #if it does not percolates, we check the rows and the columns and checks of the node is used or not.
                row=random.randint(1,self.N)
                column= random.randint(1,self.N)
                if [row] not in empty_list and [column] not in empty_list:
                    Does_It_Percolate.open(row)
                    Does_It_Percolate.open(column)
                    empty_list.append([row,column])
            return (Does_It_Percolate.new_list.count(True)-2)
        self.counter=[]
        for i in range(self.T):
            self.counter.append(Percolation_test())

        print "with", N, "*", N, "grid and", T, "tries", "\n"
        print "mean\t\t\t\t\t\t=\t", self.mean(self.counter)
        print "standard deviation\t\t\t=\t", self.stddev(self.counter)
        print "%95 confidence interval\t\t=\t", self.confidenceLo(self.counter), ",", self.confidenceHi(self.counter)
        print "---------------------------------------------------------------------------------------"

    def mean(self,numbers):
        return float(sum(numbers))/float(len(numbers))

    def stddev(self, numbers):
        number= len(numbers)
        num= sum(n**2 for n in numbers)-(sum(numbers)**2)/number
        variance= num/(number-1)
        return math.sqrt(variance)

    def confidencelo(self,numbers):
        upNumber=1.96*self.stddev(numbers)
        downNumber=math.sqrt(self.T)
        result= self.mean(numbers)-(upNumber/downNumber)
        return result

    def confidencehi(self, numbers):
        upNumber=1.96*self.stddev(numbers)
        downNumbers=math.sqrt(self.T)
        result= self.mean(numbers)+(upNumber/downNumbers)
        return result


