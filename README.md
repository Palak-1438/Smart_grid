# Smart Grid Power Flow Analysis

## Project Overview

This project simulates **power flow in a smart grid network** using **maximum flow algorithms** on weighted directed graphs. It models generators, substations, and loads as nodes, with transmission lines represented as edges with capacities.  

**Objective:** Determine the **maximum electricity flow** from generators (sources) to loads (sinks) while respecting the capacity limits of all transmission lines. Additionally, the project provides a **graphical visualization** of the smart grid to analyze the network structure and power flow paths.

---

## Why This Project?

- Smart grids require **efficient distribution of electricity**.  
- Knowing the **maximum flow** ensures **optimal power transmission** without overloading any lines.  
- Useful for **grid planning, fault analysis, and capacity optimization**.  
- Educational tool to understand **graph algorithms applied to real-world networks**.

---

## Project Structure

smart_grid/
│
├── smart_grid_flow.py # Main program to compute maximum flow
├── grid_data.py # Grid network data: nodes, edges, capacities
├── visualization.py # Functions to visualize the smart grid
└── README.md # Project documentation

# Installation Guide - Smart Grid Power Flow Analysis

This guide explains how to set up and run the Smart Grid Power Flow Analysis project on your local machine.

---

## Prerequisites

- **Python 3.6 or higher**  
- **pip** (Python package manager)  

Check Python version:

```bash
python --version
Step 1: Clone the Repository
git clone <your-repo-url>
cd smart_grid

Step 2: Install Required Packages

The project requires the following Python packages:

networkx – for graph representation

matplotlib – for visualization

Install them using pip:

pip install networkx matplotlib

Step 3: Open the Project in VS Code

Launch Visual Studio Code.

Open the smart_grid folder.

Ensure the following files are present:

smart_grid_flow.py

grid_data.py

visualization.py

Step 4: Run the Project

Open a terminal in VS Code and run:

python smart_grid_flow.py


The terminal will display the maximum power flow.

A graphical window will pop up showing the network visualization
