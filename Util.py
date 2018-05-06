from math import sqrt

def dist(ob1, ob2):
    return sqrt( (ob1.center_x-ob2.center_x)**2 + (ob1.center_y-ob2.center_y)**2 )
