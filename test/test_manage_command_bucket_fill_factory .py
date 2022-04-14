import unittest

from manage_command_bucket_fill_factory import ManageCommandBucketFillFactory
import function_create_canvas_for_testing


class TestManageCommandBucketFillFactory(unittest.TestCase):
    def test_create(self):
        list_command = ['B', '1', '1', 'O']
        width = 20
        height = 15
        empty_space = ' '
        x1 = int(list_command[1])
        y1 = int(list_command[2])
        colour_fill = list_command[3]
        test_canvas = function_create_canvas_for_testing(width, height)
        test_canvas[x1][y1] = colour_fill
        for i in range(1, len(test_canvas) - 1):
            for j in range(1, len(test_canvas[i]) - 1):
                if test_canvas[i][j] == colour_fill:
                    if test_canvas[i + 1][j] == empty_space:
                        test_canvas[i + 1][j] = colour_fill
                    if test_canvas[i][j + 1] == empty_space:
                        test_canvas[i][j + 1] = colour_fill
                    if test_canvas[i - 1][j] == empty_space:
                        test_canvas[i - 1][j] = colour_fill
                    if test_canvas[i][j - 1] == empty_space:
                        test_canvas[i][j - 1] = colour_fill

        drawing_tool = function_create_canvas_for_testing(width, height)
        CanvasTest = ManageCommandBucketFillFactory(test_canvas)
        CanvasTest.find_points(list_command)
        result = CanvasTest.create(drawing_tool)

        assert result == test_canvas
