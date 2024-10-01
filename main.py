from typing import List
from disp import Display
import threading

class Cell:
    def __init__(
        self,
        x: int = 0,
        y: int = 0
    ):
        self.x = x
        self.y = y


dirs = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
class State:
    def __init__(
        self,
        alive_cells: List[Cell]
    ):
        self.grid = set()
        for cell in alive_cells:
            self.grid.add((cell.x, cell.y))
        self.display = Display()

    def __str__(
        self
    ) -> str:
        return f'{self.grid}  {len(self.grid)}'

    def alive_neighboors(
        self,
        x: int,
        y: int
    ) -> int:
        alive = 0
        for d in dirs:
            p = (x + d[0], y + d[1])
            if p in self.grid: alive += 1
        return alive

    def update(
        self
    ):
        next_living = []
        possible = set()
        for p in self.grid:
            possible.add(p)
            for d in dirs:
                possible.add((p[0] + d[0], p[1] + d[1]))
        for p in possible:
            living_nearby = self.alive_neighboors(p[0], p[1]) 
            if living_nearby == 3 or (living_nearby == 2 and p in self.grid):
                next_living.append(p)
        self.grid = set(next_living)

    def get_state(
        self,
        x: int,
        y: int
    ) -> bool:
        return (x, y) in self.grid

    def draw_grid(
        self,
        offset_x: int = 0,
        offset_y: int = 0
    ):
        self.display.clear_bitmap()
        for i in range(32):
            for j in range(128):
                if not self.get_state(j + offset_y, i + offset_x): continue
                self.display.set_bitmap(i, j, 1)
        self.display.draw()


from rle import parse_rle

import sys
v = parse_rle(sys.argv[1])
print(v)
#initial_state = [Cell(0,0), Cell(0,-1), Cell(-1,0), Cell(0,1), Cell(1,1)]
initial_state = [Cell(y, x) for x,y in v]
state = State(initial_state)
x, y = -10, -40

import time
while True:
    state.update()
    state.draw_grid(x,y)
