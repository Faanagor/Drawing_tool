import unittest

from manage_command_line_factory import ManageCommandLineFactory
import function_create_canvas_for_testing


class TestManageCommandLineFactory(unittest.TestCase):
    def test_create(self):
        list_command = ['L', '5', '4', '15', '4']
        width = 20
        height = 15
        x1 = int(list_command[1])
        x2 = int(list_command[3])
        y = int(list_command[2])
        test_canvas = function_create_canvas_for_testing(width, height)
        for i in range(x1, x2 + 1):
            test_canvas[y][i] = 'x'

        drawing_tool = function_create_canvas_for_testing(width, height)
        CanvasTest = ManageCommandLineFactory(test_canvas)
        CanvasTest.find_points(list_command)
        result = CanvasTest.create(drawing_tool)

        assert result == test_canvas
