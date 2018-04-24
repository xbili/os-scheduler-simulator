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

or

`python -m simulator < filename`

Given an input from either `stdin` or a file with each line in the format:

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
