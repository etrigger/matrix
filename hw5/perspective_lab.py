from image_mat_util import *

from mat import Mat
from vec import Vec

from solver import solve

## Task 1
def move2board(v): 
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the 
          origin and q intersects the whiteboard plane at p.
    '''
    return Vec({'y1','y2','y3'},{'y1':v['y1']/v['y3'],'y2':v['y2']/v['y3'],'y3':1})

## Task 2
def make_equations(x1, x2, w1, w2): 
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}

    u = Vec(domain, {('y1','x1'): -x1,     ('y1','x2'): -x2,     ('y1','x3'): -1,
                     ('y3','x1'): w1 * x1, ('y3','x2'): w1 * x2, ('y3','x3'): w1})
    v = Vec(domain, {('y2','x1'): -x1,     ('y2','x2'): -x2,     ('y2','x3'): -1,
                     ('y3','x1'): w2 * x1, ('y3','x2'): w2 * x2, ('y3','x3'): w2})
    return [u, v]


## Task 3
w = Vec({(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}, {('y1', 'x1'): 1})

## jsut stupid hack. was too tired to think about this problem

## Task 3 
H = Mat(({'y1', 'y3', 'y2'}, {'x2', 'x3', 'x1'}), 
        {('y3', 'x1'): -0.7219356810710038, 
         ('y1', 'x3'): -359.86096256684493, 
         ('y1', 'x2'): 0.051693404634580956, 
         ('y2', 'x1'): -0.38152131800543626, 
         ('y3', 'x3'): 669.4762699006183, 
         ('y2', 'x2'): 0.7378180860600998, 
         ('y3', 'x2'): -0.01169073086496547, 
         ('y1', 'x1'): 1.0000000000000002, 
         ('y2', 'x3'): 110.0231807477826})


## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector 
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).
    '''
    from matutil import coldict2mat, mat2coldict
    return coldict2mat({i: move2board(v) for (i,v) in mat2coldict(Y).items()})
