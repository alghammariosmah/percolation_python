__author__ = 'osamahal-ghammari'


class WQU(object):
    def __init__(self,N):
        ''''we have to define the size of the array and each number index'''
        self.size= []
        self.ID= []
        for i in range(N): # We append each number to the ID of the size N
            self.ID.append(i)
            self.size.append(1)

    def find(self,p): #we find the main root of the element p
        while p != self.ID[p]:p=self.ID[p]
        return p

    def connected(self,p,q): # this function makes sure that both of p and q IDs are connected by calling the function find()
        if self.find(p) == self.find(q):return True
        else:return False

    def union(self, p, q):
        ''''this funtion unit both of p and q and change their IDs according to the root of p'''
        i = self.find(p)
        j= self.find(q)
        if i==j: return
        if self.size[i] >= self.size[j]: #if the tree of i is bigger than j;
            self.ID[j]=i #change the ID of j into i
            self.size[i]+= self.size[i] #then append to the size of index i
        else: # if the size of the tree of i is not bigger than j
            self.ID[i] = j  # the ID of i changes to j
            self.size[j]= self.size[i] #and the size of j equals i

'''
wqu = WQU(10)
print wqu.size
wqu.union(2,4)
wqu.union(2,5)
print wqu.connected(4,5)
print wqu.ID
print wqu.connected(2,4)
'''
