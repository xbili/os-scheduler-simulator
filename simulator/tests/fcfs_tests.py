import unittest

from simulator.schedulers import FCFS
from simulator.tests.base import SchedulerTest
from simulator.tests.test_utils import create_processes


class FCFSTest(unittest.TestCase, SchedulerTest):
    def setUp(self):
        self.scheduler = FCFS()

    def tearDown(self):
        self.scheduler.reset()

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

    def test_advanced_scheduling(self):
        """
        Longer test case for scheduling as given together with sample code.
        """
        processes = create_processes(
            (0, 0, 9),
            (1, 1, 8),
            (2, 2, 2),
            (3, 5, 2),
            (3, 30, 5),
            (1, 31, 2),
            (2, 32, 6),
            (0, 38, 8),
            (2, 60, 7),
            (0, 62, 2),
            (1, 65, 3),
            (3, 66, 8),
            (1, 90, 10),
            (0, 95, 10),
            (2, 98, 9),
            (3, 99, 8))

        expected_schedule = [
            (0, 0),
            (9, 1),
            (17, 2),
            (19, 3),
            (30, 3),
            (35, 1),
            (37, 2),
            (43, 0),
            (60, 2),
            (67, 0),
            (69, 1),
            (72, 3),
            (90, 1),
            (100, 0),
            (110, 2),
            (119, 3)]

        expected_avg_waiting_time = 6.44

        expected = {
            'schedule': expected_schedule,
            'avg_waiting_time': expected_avg_waiting_time,
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
            (35, 1),
            (37, 2),
            (43, 0),
            (60, 2),
            (67, 0),
            (69, 1),
            (72, 3),
            (90, 1),
            (100, 0),
            (110, 2),
            (119, 3)]
        expected['avg_waiting_time'] = 6.44

        self.assert_process_schedule(processes, expected)
