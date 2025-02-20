from grid import Grid

grid = Grid()
grid.init_grid(x_size=3, y_size=3, depth=6, entry_nodes=((1,1)), exit_nodes=((2,2)))
grid.print_grid()