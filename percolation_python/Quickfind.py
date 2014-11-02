__author__ = 'osamahal-ghammari'



class QuickFindUF(object):
    id = []

    def __init__(self, n=None, arr = None):
        if arr == None:
            self.id=self._construct_array(n)
        else:
            self.id = arr

    def _construct_array(self, n):
        temp_arr =[]
        for e in range(n):
            temp_arr.append(e)
        return temp_arr

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self,p,q):
        pid= self.id[p]
        qid= self.id[q]

        for e in range(len(self.id)):
            if self.id[e] == pid:
                self.id[e]=qid

