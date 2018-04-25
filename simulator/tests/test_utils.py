from simulator.core.process import Process

def create_processes(*processes):
    """Takes in 3-element tuples and convert them into a list of processes."""
    return [Process(id, arrive_time, burst_time)
            for id, arrive_time, burst_time in processes]
