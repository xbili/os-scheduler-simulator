import unittest

from simulator.fcfs import FCFS
from simulator.test_utils import create_processes

class FCFSTest(unittest.TestCase):
    def setUp(self):
        self.scheduler = FCFS()

    def test_basic_scheduling(self):
        processes = create_processes(
            (0, 0, 4),
            (1, 2, 3))
        schedule = self.scheduler.schedule(processes)
        avg_waiting_time = self.scheduler.avg_waiting_time

        expected = [
            (0, 0),
            (4, 1)]

        self.assertEqual(schedule, expected)
        self.assertEqual(avg_waiting_time, 1.0)

    def tearDown(self):
        self.scheduler.reset()

class RRTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

class SRTFTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

class SJFTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
