import unittest

from simulator.tests.test_utils import create_processes


class SchedulerTest(object):
    def get_assignment_input(self):
        """Returns the input provided by the assignment."""
        return create_processes(
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

    def assert_process_schedule(self, processes, expected):
        schedule = self.scheduler.schedule(processes)
        avg_waiting_time = self.scheduler.avg_waiting_time

        self.assertEqual(schedule, expected['schedule'])
        self.assertEqual(avg_waiting_time, expected['avg_waiting_time'])

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
