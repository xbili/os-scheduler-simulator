import unittest

from simulator.schedulers import SRTF
from simulator.tests.base import SchedulerTest
from simulator.tests.test_utils import create_processes


class SRTFTest(unittest.TestCase, SchedulerTest):
    def setUp(self):
        self.scheduler = SRTF()

    def tearDown(self):
        self.scheduler.reset()

    def test_simple_example(self):
        processes = create_processes(
            (1, 0, 10),
            (2, 1, 2),
            (3, 2, 5))
        expected_schedule = [
            (0, 1),
            (1, 2),
            (3, 3),
            (8, 1)]
        expected_avg_waiting_time = 2.67

        expected = {
            'schedule': expected_schedule,
            'avg_waiting_time': expected_avg_waiting_time
        }

        self.assert_process_schedule(processes, expected)

    def test_assignment_input(self):
        """Runs the test using the given input for the assignment."""
        processes = self.get_assignment_input()
        expected = {}
        expected['schedule'] = [
            (0, 0),
            (2, 2),
            (4, 0),
            (5, 3),
            (7, 0),
            (13, 1),
            (30, 3),
            (31, 1),
            (33, 3),
            (37, 2),
            (43, 0),
            (60, 2),
            (62, 0),
            (64, 2),
            (65, 1),
            (68, 2),
            (72, 3),
            (90, 1),
            (100, 3),
            (108, 2),
            (117, 0)]
        expected['avg_waiting_time'] = 4.50

        self.assert_process_schedule(processes, expected)
