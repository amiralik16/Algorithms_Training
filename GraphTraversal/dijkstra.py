from heapq import *
from collections import defaultdict
inf = float('inf')
# Edge = namedtuple('Edge', 'start, end, cost')

# def make_edge(start,end,cost=1):
#     return Edge(start,end,cost)
# class Qelement:
#     def element
class Graph:
    def __init__(self,vertices,edges):
        #Assuming edges will be an adjacency list implemented as a dictionay(Start: (end,weight)), edge name is string
        #Vertices is just a simple list of vertices
        self.edges = edges
        self.vertices = vertices
    
    def dijkstra(self,start,stop):
        q = []
        heappush(q,(0,start,''))
        done = defaultdict(str)
        while(len(done)<len(self.vertices)):
            # print(q)
            w,current,prev = heappop(q)
            print(f'currently looking at {current}, prev node was {prev}')
            if current == stop:
                #stopping logic
                path = []
                path.append(prev)
                node = prev
                while node != start:
                    node = done[node]
                    path.append(node)
                print(f'Smallest path was {path[::-1]}')
                print(f'Path length was {w}')
                return 1
            neighbors = self.edges[current]
            for neighbor in neighbors:
                #push it to the priority queue if its not the previous one
                if neighbor[0] != prev:
                    #find it if its already in the queue, if it is update it. if not, add it
                    found = False
                    for i,el in enumerate(q):
                        if q[i][1] == neighbor[0]:
                            if w+neighbor[1]<q[i][0]:
                                # q[i][0] = w+neighbor[1]
                                # q[i][2] = current
                                q.append((w+neighbor[1],neighbor[0],current))
                                q.pop(i)
                                heapify(q)
                                found = True
                                break
                    if not found and not done[neighbor[0]]:
                        heappush(q,(w+neighbor[1],neighbor[0],current))
            done[current] = prev
        return None
                
def simplify(s):
    s = s.split(',')
    out = [None] * len(s)
    for i in range(len(s)):
        out[i] = (s[i][0].upper(),int(s[i][1]))
    return out

if __name__ == "__main__":
    vertices = list('ABCDEFGHIJKLS')
    edges = defaultdict(list)
    edges['S'] = simplify('b2,a7,c3')
    edges['B'] = simplify('h1,d4,a3,s2')
    edges['A'] = simplify('s7,b3,d4')
    edges['C'] = simplify('s3,l2')
    edges['D'] = simplify('f5,b4')
    edges['E'] = []
    edges['F'] = simplify('d5,h3')
    edges['G'] = simplify('h2,e2')
    edges['H'] = simplify('b1,f3,g2')
    edges['I'] = simplify('l4,j6,k4')
    edges['J'] = simplify('l4,k4,i6')
    edges['K'] = simplify('l4,j4,e5')
    edges['L'] = simplify('c2,j4,i4')
    g = Graph(vertices,edges)
    g.dijkstra('S','E')