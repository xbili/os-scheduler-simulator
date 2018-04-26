# CS5250 Assignment 4

OS scheduling simulator in Python.

Experiment with the following schedulers:

1. First Come First Serve (FCFS)
2. Round Robin
3. Shortest Remaining Time First (SRTF)
4. Shortest Job First (SJF)

## Getting Started

To run:

`python -m simulator <filename>`

Input file should have the format for each line:

`<process id> <arriving time> <burst time>`

The program will write a line in the following format every time the CPU
performs a context switch:

`(<timestamp>, <process id>)`

And lastly output the average waiting time:

`Average waiting time <waiting time>`

The outputs will be written in a file with the name of the scheduler and stored
in the folder called `schedules`.

## Test Cases

To run the unit tests for each scheduler, run:

`python -m unittest simulator.tests`

## Notebooks

The experimentation for the parameter values were done using Jupyter notebook.
You can view it on GitHub directly, but to run locally:

`pip install -r requirements.txt`

`jupyter notebook`

A new browser should open based on your local Jupyter settings.
