Characteristics:
- 3d grid
    - Grid can be created with x, y, z sizes, can be expanded non-uniformly (in x and y direction, z likely uniform)
    - Maybe it starts at an origin point on the x and y planes, they go positive and negative. So we just add (x, y) points, they get a z size automatically
    - Representation:
        - We want to mainly traverse the x and y plane, which sits atop the z plane. We’re not really navigating all 3 dimensions, instead we traverse to (x, y), then perform actions
        - How should we represent x and y?
            - A graph would likely be most flexible
                - Could expand freely and non-uniformly, and use A* and Dijkstra's
                - Can assign values to nodes and edges - time cost, stack type (bin stack, exit point, taken by another robot)
        - Bins
            - We have a graph of nodes (stacks), so we traverse to a stack and perform bin actions
            - Each stack contains bins
                - Bin object - can be subdivided into x sub containers, each subcontainer can contain items
                - Each bin can have an id, and when an item is added to the system, it is assigned the container id and subcontainer number
                -  
        
