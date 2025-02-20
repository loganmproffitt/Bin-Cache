from setup.warehouse_setup import WarehouseSetup
import random


if __name__ == "__main__":
    warehouse = WarehouseSetup(x_size=3, y_size=3, depth=6, entry_nodes=[(1,1)], exit_nodes=[(2,2)])
    warehouse.populate_grid_with_bins(num_bins=5, items_per_bin=4)
    warehouse.print_setup()