class Process(object):

    last_scheduled_time = 0

    def __init__(self, id, arrive_time, burst_time):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time

    def __repr__(self):
        return ('[id %d : arrive_time %d,  burst_time %d]' %
                (self.id, self.arrive_time, self.burst_time))
