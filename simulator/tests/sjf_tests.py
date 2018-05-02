import unittest

from simulator.schedulers import SJF
from simulator.tests.base import SchedulerTest
from simulator.tests.test_utils import create_processes


class SJFTest(unittest.TestCase, SchedulerTest):
    def setUp(self):
        self.scheduler = SJF()

    def tearDown(self):
        self.scheduler.reset()

    def test_simple_example(self):
        processes = create_processes(
            (1, 0, 2),
            (2, 1, 10),
            (3, 2, 1))

        expected_schedule = [
            (0, 1),
            (2, 2),
            (12, 3)]
        expected_avg_waiting_time = 3.67

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
            (9, 1),
            (17, 2),
            (19, 3),
            (30, 3),
            (35, 2),
            (41, 1),
            (43, 0),
            (60, 2),
            (67, 1),
            (70, 3),
            (78, 0),
            (90, 1),
            (100, 0),
            (110, 2),
            (119, 3)]
        expected['avg_waiting_time'] = 7.12

        self.assert_process_schedule(processes, expected)
