import os
import sys
from copy import deepcopy

from simulator.core.process import Process
from simulator.schedulers import FCFS, RoundRobin, SRTF, SJF

RESULT_DIR = 'schedules'
RESULT_FCFS = 'FCFS.txt'
RESULT_RR = 'RR.txt'
RESULT_SRTF = 'SRTF.txt'
RESULT_SJF = 'SJF.txt'


def read_input(input_file):
    res = []
    with open(input_file) as f:
        for line in f:
            array = line.split()
            if len(array) != 3:
                print ("wrong input format")
                exit()
            res += [Process(int(array[0]), int(array[1]), int(array[2]))]

    return res


def write_output(output_file, schedule, avg_waiting_time):
    with open(output_file, 'w') as f:
        for item in schedule:
            f.write(str(item) + '\n')
        f.write('average waiting time %.2f\n' % avg_waiting_time)


if __name__ == '__main__':
    input_file = str(sys.argv[1])
    processes = read_input(input_file)

    # Schedulers
    schedulers = [FCFS(), RoundRobin(), SRTF(), SJF()]
    result_names = [RESULT_FCFS, RESULT_RR, RESULT_SRTF, RESULT_SJF]

    for idx, scheduler in enumerate(schedulers):
        schedule = scheduler.schedule(deepcopy(processes))
        avg_waiting_time = scheduler.avg_waiting_time
        write_output(os.path.join(RESULT_DIR, result_names[idx]), schedule, avg_waiting_time)
