import unittest

from simulator.fcfs import FCFS
from simulator.test_utils import create_processes

class FCFSTest(unittest.TestCase):
    def setUp(self):
        self.scheduler = FCFS()

    def test_basic_scheduling(self):
        """
        Test case for the basic example provided in the assignment
        specification.
        """
        processes = create_processes(
            (0, 0, 4),
            (1, 2, 3))
        expected_schedule = [
            (0, 0),
            (4, 1)]
        expected_avg_waiting_time = 1.0
        expected = {
            'schedule': expected_schedule,
            'avg_waiting_time': expected_avg_waiting_time,
        }

        self.assert_process_schedule(processes, expected)

    def assert_process_schedule(self, processes, expected):
        schedule = self.scheduler.schedule(processes)
        avg_waiting_time = self.scheduler.avg_waiting_time

        self.assertEqual(schedule, expected['schedule'])
        self.assertEqual(avg_waiting_time, expected['avg_waiting_time'])

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
