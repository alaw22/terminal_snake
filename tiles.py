from enum import Enum
from constants import ESC

class TileType(Enum):
    EMPTY  = "empty"
    APPLE  = "apple"
    HEAD   = "head"
    BODY   = "body"
    CORNER = "corner"

class Tile:

    def __init__(self,x,y,tile_type,text,bg_color=None,fg_color=None,direction=None):
        self.__x = x
        self.__y = y
        self.__tile_type = tile_type
        self.__bg_color = bg_color if bg_color is not None else ""
        self.__fg_color = fg_color if fg_color is not None else ""
        self.__text = self._color_tile(text)
        self.direction = direction

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.tile_type == other.tile_type and self.text == other.text
        

    def _color_tile(self,text):
        return f"{ESC}48;2;{self.bg_color}m{ESC}38;2;{self.fg_color}m{text}{ESC}m"


    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,newval: int):
        if not isinstance(newval,int):
            print("Can only set self.x to type int")
            return
        self.__x = newval

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,newval: int):
        if not isinstance(newval,int):
            print("Can only set self.y to type int")
            return
        self.__y = newval

    @property
    def tile_type(self):
        return self.__tile_type
    
    @tile_type.setter
    def tile_type(self,newval: TileType):
        if not isinstance(newval,TileType):
            print("Can only set self.tile_type to instance of TileType")
            return
        
        self.__tile_type = newval

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self,newval: str):
        if not isinstance(newval,str) or len(newval) < 2:
            print("text attribute must be of length 2 or more and a string")
            return
        
        self.__text = self._color_tile(newval)

    @property
    def bg_color(self):
        return self.__bg_color
    
    @bg_color.setter
    def bg_color(self,newval: str):
        self.__bg_color = newval

    @property
    def fg_color(self):
        return self.__fg_color
    
    @fg_color.setter
    def fg_color(self,newval: str):
        self.__fg_color = newval

    def __str__(self):
        return self.__text
    
    # def __init__(self,tile_type,prev_tile=None,orientation=None,direction=None):
    #     if orientation is not None and tile_type != TileType.CORNER:
    #         raise Exception("Only TileType.CORNER tiles have an orientation")

    #     self.tile_type = tile_type
    #     self.prev_tile = prev_tile
    #     self.direction = direction
    #     self.orientation = orientation
    #     self._set_tile_ascii()

    # def _set_direction(self,direction):
    #     if self.tile_type == TileType.APPLE or self.tile_type == TileType.EMPTY:
    #         return
    
    #     if self.tile_type == TileType.HEAD:
    #         self.direction = direction
    #         self._set_tile_ascii()
    #         return
        
                

    #     self._set_tile_type(TileType.BODY)
    #     self._set_tile_type(TileType.CORNER)
        

    # def _set_tile_type(self,tile_type):
    #     if isinstance(tile_type,TileType):
    #         self.tile_type = tile_type
    #         self._set_tile_ascii()

    # def _set_tile_ascii(self):
    #     match self.tile_type:
    #         case TileType.EMPTY:
    #             self.ascii = color_tile("  ",BACKGROUND_C,BACKGROUND_C)
    #         case TileType.APPLE:
    #             self.ascii = color_tile("  ",APPLE_C,APPLE_C)
    #         case TileType.HEAD:
    #             if self.direction == "right":
    #                 self.ascii = HEAD_RIGHT
    #             elif self.direction == "down":
    #                 self.ascii = HEAD_DOWN
    #             elif self.direction == "left":
    #                 self.ascii = HEAD_LEFT
    #             elif self.direction == "up":
    #                 self.ascii = HEAD_UP
    #             else:
    #                 raise Exception("Direction type is not recognized")

    #             self.ascii = color_tile(self.ascii,SNAKE_C,EYES_C)
    #         case TileType.BODY:
    #             if self.direction == "right" or self.direction == "left":
    #                 self.ascii = "=="
    #             elif self.direction == "down" or self.direction == "up":
    #                 self.ascii = chr(166)*2 
    #             else:
    #                 raise Exception("Direction type is not recognized")

    #             self.ascii = color_tile(self.ascii,SNAKE_C,PATTERN_C)              
    #         case TileType.CORNER:
    #             if self.orientation == "top_left":
    #                 self.ascii = TOP_LEFT
    #             elif self.orientation == "top_right":
    #                 self.ascii = TOP_RIGHT
    #             elif self.orientation == "bottom_left":
    #                 self.ascii = BOTTOM_LEFT
    #             elif self.orientation == "bottom_right":
    #                 self.ascii = BOTTOM_RIGHT
    #             else:
    #                 raise Exception("Orientation not recognized")
                
    #             self.ascii = color_tile(self.ascii,SNAKE_C,PATTERN_C)
            
    #         case _:
    #             raise Exception("TileType not recognized")

