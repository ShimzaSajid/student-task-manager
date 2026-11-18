import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Study Git")
        self.assertEqual(task["title"], "Study Git")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_add_empty_task_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        self.manager.add_task("Study Git")
        self.manager.complete_task(1)
        self.assertTrue(self.manager.get_tasks()[0]["completed"])

    def test_delete_task(self):
        self.manager.add_task("Study Git")
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.get_tasks()), 0)


if __name__ == "__main__":
    unittest.main()