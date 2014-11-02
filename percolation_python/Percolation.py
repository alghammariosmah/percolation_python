from percolation_python import WieghtedQuickUnion

__author__ = 'osamahal-ghammari'

#FALSE == It should return False as it doesn't percolates
#TRUE == It should retrun True as it percolates

class Percolation(object):
    def __init__(self,N):
        self.N= N
        self.new_list=[0]*(N**2+2) # we create a list with 0s for the block.
        self.new_list[-1]=1
        self.new_list[-2]=1
        self.WQU = WieghtedQuickUnion.WQU((N ** 2) + 2) # to check the connection and the id.


    def open(self,i,j):
        '''the following function should open the blocked places for us in order to make the system percolates'''
        node = ((i - 1) * self.N) + j - 1 #it should locate the ith row and jth column.
        if self.new_list[node]== 0: #if the node is blocked
            self.new_list[node] = 1 # we open it
            if (node +1) < self.N**2 and (node +1) > 0: #now we check the neighboring nodes if they are opened. node +1 checks it from the right side.
                if self.new_list[node +1] == 1:
                    self.WQU.union(node +1, node) # we call the Wieghted Quick Union if they have the same root.
            if (node -1) < self.N**2 and (node -1)> 0: #we check the other neighboring node. node - 1 check it from the left.
                if self.new_list[node-1]==1:
                    self.WQU.union(node-1, node)
            if self.N**2 > (node - self.N) > 0: # we check it from up.
                if self.new_list[node - self.N] == 1:
                    self.WQU.union(node-self.N, node)
            if self.N**2 > (node+self.N) > 0: # we check it from down.
                if self.new_list[node+self.N] == 1:
                    self.WQU.union((node + self.N),node)

            if 0 <= node < self.N: # we need to know whether the node is on the top or in the bottom line.
                self.WQU.union(node,self.N**2)
            elif self.N**2 -self.N <= node < self.N**2:
                self.WQU.union(node,self.N**2+1)


    def is_Open(self,node): # is site (row i, column j) open?
        return self.new_list[node] #it will return with a boolean answer. True if it is opened, False otherwise

    def is_Full(self,node): #is site (row i, column j) full?
        return not self.new_list[node] # it will return either True that the row i and column j is Full.

    def percolates(self): # does the system percolates?
        return self.WQU.connected(self.N ** 2, self.N ** 2 + 1) #True percolates, False it doesn't percolates


''''
a = Percolation(5)
a.open(1,3)
print a.new_list
a.open(2,4)
print a.new_list
a.open(3,3)
print a.new_list
a.open(4,3)
print a.new_list
a.open(5,3)
print a.new_list
a.open(2,5)
print a.new_list
a.open(2,3)
print a.new_list
print a.percolates()
'''''

