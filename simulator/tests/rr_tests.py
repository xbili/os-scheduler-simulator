import unittest

from simulator.schedulers import RoundRobin
from simulator.tests.base import SchedulerTest
from simulator.tests.test_utils import create_processes


class RRTest(unittest.TestCase, SchedulerTest):
    def setUp(self):
        self.scheduler = RoundRobin()

    def tearDown(self):
        self.scheduler.reset()

    def test_one_task(self):
        """Tests round robin execution for a single task."""
        processes = create_processes((1, 0, 20))
        expected = {}
        expected['schedule'] = [
            (0, 1)]
        expected['avg_waiting_time'] = 0.0
        self.assert_process_schedule(processes, expected)

    def test_lecture_example(self):
        """Tests the example went through during lecture."""
        processes = create_processes(
            (1, 0, 24),
            (2, 0, 3),
            (3, 0, 3))
        expected_schedule = [
            (0, 1),
            (4, 2),
            (7, 3),
            (10, 1)]
        expected_avg_waiting_time = 5.67

        expected = {
            'schedule': expected_schedule,
            'avg_waiting_time': expected_avg_waiting_time,
        }

        self.assert_process_schedule(processes, expected)

    def test_techtud_example(self):
        """http://www.techtud.com/example/solved-example-rr-round-robin"""

        # Time quantum is 3 for this example
        self.scheduler = RoundRobin(time_quantum=3)
        processes = create_processes(
            (4, 0, 9),
            (5, 1, 2),
            (3, 2, 7),
            (2, 3, 6),
            (1, 4, 5),
            (6, 5, 3))
        expected_schedule = [
            (0, 4),
            (3, 5),
            (5, 3),
            (8, 2),
            (11, 4),
            (14, 1),
            (17, 6),
            (20, 3),
            (23, 2),
            (26, 4),
            (29, 1),
            (31, 3)]
        expected_avg_waiting_time = 16.00

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
            (4, 1),
            (8, 2),
            (10, 0),
            (14, 3),
            (16, 1),
            (20, 0),
            (30, 3),
            (34, 1),
            (36, 2),
            (40, 3),
            (41, 0),
            (45, 2),
            (47, 0),
            (60, 2),
            (64, 0),
            (66, 2),
            (69, 1),
            (72, 3),
            (90, 1),
            (98, 0),
            (102, 2),
            (106, 1),
            (108, 3),
            (112, 0),
            (116, 2),
            (120, 3),
            (124, 0),
            (126, 2)]
        expected['avg_waiting_time'] = 8.81

        self.assert_process_schedule(processes, expected)
