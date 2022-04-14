import unittest

from manage_command_rectangle_factory import ManageCommandRectangleFactory
import function_create_canvas_for_testing


class TestManageCommandRectangleFactory(unittest.TestCase):
    def test_create(self):
        list_command = ['R', '5', '4', '15', '8']
        width = 20
        height = 15
        x1 = int(list_command[1])
        y1 = int(list_command[2])
        x2 = int(list_command[3])
        y2 = int(list_command[4])
        test_canvas = function_create_canvas_for_testing(width, height)
        for i in range(y1, y2 + 1):
            test_canvas[i][x1] = 'x'
            test_canvas[i][x2] = 'x'
        for i in range(x1, x2 + 1):
            test_canvas[y1][i] = 'x'
            test_canvas[y2][i] = 'x'

        drawing_tool = function_create_canvas_for_testing(width, height)
        CanvasTest = ManageCommandRectangleFactory(test_canvas)
        CanvasTest.find_points(list_command)
        result = CanvasTest.create(drawing_tool)
        assert result == test_canvas
