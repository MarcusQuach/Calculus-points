Distance Between Two Points
===========================

This simple Python script calculates the distance between two points in a 2D plane using the distance formula.

Description
-----------

The formula used is:

distance = √[(x₂ - x₁)² + (y₂ - y₁)²]

This script takes in four arguments:

- x1: x-coordinate of the first point  
- x2: x-coordinate of the second point  
- y1: y-coordinate of the first point  
- y2: y-coordinate of the second point  

And then calculates and prints the distance between those two points.

Example
-------

In this example:

    find_points(0, 2, 4, 6)

The points are (0, 4) and (2, 6), and the calculated distance is:

    2.8284271247461903

How to Run
----------

1. Make sure you have Python installed.
2. Clone this repository or copy the script into a file (e.g., distance.py).
3. Open a terminal and run:

    python distance.py

Requirements
------------

- Python 3.x
- No external libraries needed (only uses Python's built-in math module)

File Structure
--------------

    distance_project/
    │
    ├── distance.py     # Main script
    └── README.txt      # Project overview (this file)