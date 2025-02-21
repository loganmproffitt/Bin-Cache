# Bin-Cache

Basic simulator of an automated warehouse system. Includes:
- Graph data structure to represent the top xy plane
- Stack objects stored at each node in the graph
  - Stack types include BinStack, EntryStack, and ExitStack
  - BinStacks contain a stack data structure while Entry and ExitStack contain queue data structure to mimic the real life behavior
- Bin objects contain a list of items, could add subcontainers/divisions in the future
- For prototyping purposes, I created an ItemType object and Item subtype, then a few sample Items (Basketball, Baseball, etc.).
  - This allows for randomly generating actual instances of those sample items. In the future, I would likely add support for csv files with orders to feed into the simulator.
- I also created a Robot object which can move around the grid, drop bins, and place bins

I also created unit tests for all of the features above.
Future features could include:
- A* or Dijkstra's for robot navigation
- Automated bin retrieval from entry port, stack selection, navigation, then placement
- Automated bin retrieval and placement in the exit port
- Time step simulation and real time order feeding
  - Different actions could be assigned different durations, and each completed order could have a time summary, allowing for machine learning optimization
