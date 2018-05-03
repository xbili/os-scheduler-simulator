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
