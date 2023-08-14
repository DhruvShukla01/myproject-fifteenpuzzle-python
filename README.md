# Fifteen Puzzle Game

**Author**: Dhruv Shukla  
**Date**: May 29, 2023

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Gameplay Instructions](#gameplay-instructions)
- [In-Depth File Breakdown](#in-depth-file-breakdown)
  * [`fifteen.py`](#fifteenpy)
  * [`game.py`](#gamepy)
  * [`graph.py`](#graphpy)
- [License](#license)

## Overview
This project implements the classic Fifteen Puzzle game. Utilizing Python's `tkinter` for its GUI and `numpy` for matrix operations, players can interact with the game in a graphical window to shuffle tiles and aim to solve the puzzle.

<img width="479" alt="Screenshot 2023-08-14 at 5 56 46 AM" src="https://github.com/DhruvShukla01/myproject-fifteenpuzzle-python/assets/135282874/58f01c10-a59d-4ab5-9c6c-d169388b5971">
<img width="375" alt="Screenshot 2023-08-14 at 5 58 02 AM" src="https://github.com/DhruvShukla01/myproject-fifteenpuzzle-python/assets/135282874/bfcea316-dba5-4394-aabd-a07e2ce46d03">

## Installation
1. Ensure Python is installed on your machine.
2. Install the required libraries:
   ```bash
   pip install numpy tkinter
   ```
3. Clone the repository or download the game files.
4. Navigate to the directory and run:
For Terminal File
    ```bash
   python fifteen.py
    ```
5. For GUI File:
   ```bash
   python game.py
   ```
## Gameplay Instructions

1. **Starting the Game**: Launch the game by running the `graph.py` script. A window with numbered tiles will appear.
2. **Shuffling Tiles**: Use the `shuffle` button to randomize the tile positions. This provides a new puzzle configuration for you to solve.
3. **Moving Tiles**: Click on any tile adjacent to the empty space. The tile will move into the empty space, effectively swapping their positions.
4. **Objective**: Aim to arrange the tiles in ascending order, starting from the top-left and ending with the empty space at the bottom-right corner.

## In-Depth File Breakdown

### `fifteen.py`

This file forms the backbone of the Fifteen Puzzle game, providing the essential logic:

- **Class `Fifteen`**: 
    * **Initialization**: Sets up the puzzle with a default size or a specified one.
    * **Methods**: 
        - `update()`: Updates tile positions.
        - `transpose()`: Helps in transposing two tiles.
        - `shuffle()`: Randomizes tile positions.
        - `is_valid_move()`: Checks if a given move is valid.
        - `is_solved()`: Determines if the puzzle is solved.
        - `draw()`: Provides a console-based visual representation of the puzzle.
    * **Console Play**: If executed directly, players can play a console version of the game.

### `game.py`

This file is responsible for the graphical user interface using `tkinter`:

- **Tile Representation**: Tiles are visualized as `Button` widgets in a `Tkinter` window.
- **Shuffle Button**: Apart from numbered tiles, there's a shuffle button allowing players to randomize tile positions.
- **Tile Movement**: Defines the logic to move tiles within the GUI when clicked.
- **Visual Updates**: Ensures the GUI updates correctly based on user interactions and the current state of the puzzle.

### `graph.py`
This file implements a graph class for the Fifteen Puzzle game:

- **Class `Vertex`**: Defines a vertex in the graph, used to represent puzzle configurations.
    * **Methods**:
        - `addNeighbor()`: Adds a neighbouring vertex.
        - `getConnections()`: Returns connected vertices.
        - `getId()`: Returns the vertex ID.
        - `getWeight()`: Returns the weight between vertices.
- **Class `Graph`**: Implements the graph structure for puzzle configurations.
    * **Methods**:
        - `addVertex()`: Adds a vertex to the graph.
        - `getVertex()`: Retrieves a vertex from the graph.
        - `addEdge()`: Adds an edge between vertices.
        - `getVertices()`: Returns all vertices in the graph.
        - `breadth_first_search()`: Performs breadth-first search traversal.
        - `depth_first_search()`: Performs depth-first search traversal.
      
## License

Theis project is licensed under the [BSD 2-Clause License](LICENSE)
