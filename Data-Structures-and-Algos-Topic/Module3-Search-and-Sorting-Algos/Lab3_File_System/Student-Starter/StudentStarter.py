import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

#TODO for part 2
#create your own graph object
class Graph():
    def __init__(self):
        #define graph attributes

            

#provided method
#will help in displaying with networkx
#Param: G = networkx graph
#Param: root = "top" of the data structure
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike
    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.
    G: the graph (must be a tree)
    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.
    width: horizontal space allocated for this branch - avoids overlap with other branches
    vert_gap: gap between levels of hierarchy
    vert_loc: vertical location of root
    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')
    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))
    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments
        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed
        '''
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children)!=0:
            dx = width/len(children)
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap,
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
        
def main():
    #TODO for part 1
    #read the input file: "input.txt"
    #will contain structural numbers and names
    #format: ###.some name
    #parse the file for the structural numbers
    #and the names that you will use to make
    #your own graph
    #note: you don't have to do this in the
    #main method


    #TODO for part 3
    #print the file structure in order
    #beware that the input file may not
    #be in numerical order.
    #reminder: the format is ###.some name
    #hint: use DFS
    #note: you don't have to do this in the
    #main method

    #TODO for part 4
    #display the graph using networkx and matplotlib
    #HINT: the activity on directed graphs
    #may be helpful ;)
    #note: you don't have to do this in the
    #main method
    # NOTE: for part 4, make sure to use G2 as your graph
    # and NOT the graph you construct from your custom class
    # you will still need to add aspects of your original 
    # graph to G2, but for all the networkx and matplotlib functions
    # use G2 as the graph you pass into the function
    G2 = nx.Graph()
    
main()
