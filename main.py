import time
import sys
import tiles as tiles
from board import Board
from constants import *

def main():
    body = tiles.Tile(10,10,tiles.TileType.HEAD,HEAD_UP,SNAKE_C,PATTERN_C,direction="up")
    apple = tiles.Tile(10,10,tiles.TileType.APPLE,"  ",APPLE_C)
    directions = [HEAD_RIGHT,HEAD_DOWN,HEAD_LEFT,HEAD_UP]
    for i in range(12):
        if i > 0:
            # print(f"{i-1+5}{2*(i-1)+5}")
            sys.stdout.write(f"{ESC}{i-1+5};{2*(i-1)+5}H")
            sys.stdout.write("  ")
            sys.stdout.flush()

        sys.stdout.write(f"{ESC}{i+5};{2*i+5}H")
        sys.stdout.write(body.text)
        sys.stdout.flush()

        body.text = directions[i % 4]
        time.sleep(0.5)


    # board = Board()
    # board.blit_grid()
    # nframes = 0
    # while not board.game_over:
    #     board.blit_grid()
    #     board.update()
    #     time.sleep(0.1)
    #     nframes += 1


if __name__ == "__main__":
    main()
# apple = tiles.Tile(tiles.TileType.APPLE)
# snake_head_right = tiles.Tile(tiles.TileType.HEAD,direction="right")
# snake_head_down = tiles.Tile(tiles.TileType.HEAD,direction="down")
# snake_head_left = tiles.Tile(tiles.TileType.HEAD,direction="left")
# snake_head_up = tiles.Tile(tiles.TileType.HEAD,direction="up")
# snake_corner_top_right = tiles.Tile(tiles.TileType.CORNER,orientation="top_right")
# snake_corner_bottom_right = tiles.Tile(tiles.TileType.CORNER,orientation="bottom_right")
# snake_corner_top_left = tiles.Tile(tiles.TileType.CORNER,orientation="top_left")
# snake_corner_bottom_left = tiles.Tile(tiles.TileType.CORNER,orientation="bottom_left")


# h_back = tiles.Tile(tiles.TileType.BODY,direction="right")
# v_back = tiles.Tile(tiles.TileType.BODY,direction="up")
# empty = tiles.Tile(tiles.TileType.EMPTY)
