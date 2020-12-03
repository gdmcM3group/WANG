from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
from roofBuilder import *

class shop:
    
    def __init__(self,level,start_x,start_y,start_z,end_x,,end_z,direction):
        self.level=level
        self.s_x=start_x
        self.s_y=start_y
        self.s_z=start_z
        self.e_x=end_x
        self.e_z=end_z
        self.direction=direction
        if(self.e_x-self.s_x<self.e_z-self.s_z):
            self.s_x=start_z
            self.e_x=end_z
            self.s_z=start_x
            self.e_z=end_x

    def build_shop(self):
        area=(self.e_x-self.s_x+1)*(self.e_z-self.s_z+1)
        if(area>=72 and area<120):
        elif(area>=120 and area<20*15):
        else:


    def small_shop(self):
        