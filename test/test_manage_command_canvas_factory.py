import unittest

from manage_command_canvas_factory import ManageCommandCanvasFactory
import function_create_canvas_for_testing


class TestManageCommandCanvasFactory(unittest.TestCase):
    def test_create(self):
        list_command = ['C', '20', '15']
        width = int(list_command[1])
        height = int(list_command[2])
        test_canvas = function_create_canvas_for_testing(width, height)
        CanvasTest = ManageCommandCanvasFactory(list_command, width, height)
        result = CanvasTest.create(list_command)
        assert result == test_canvas
