import unittest

from input_file import InputFile
import is_int

class TestInputFile(unittest.TestCase):
    def test_read_file(self):
        path = 'input.txt'
        file = open(path, "r")
        InputFileTest = InputFile(path)
        result = InputFileTest.read_file()
        assert result == file

    def test_validate_commands(self):
        path = 'input.txt'
        CREATE_CANVAS = 'C'
        CREATE_LINE = 'L'
        CREATE_RECTANGLE = 'R'
        BUCKET_FILL = 'B'
        list_command = [['C', '20', '4'], 
                        ['L', '1', '2', '6', '2'], 
                        ['L', '6', '3', '6', '4'], 
                        ['R', '16', '1', '20', '3'], 
                        ['B', '10', '3', 'o']]
        cont_line = 0
        error = False
        for i in list_command:
            number_letter = len(i)
            if i[0] == BUCKET_FILL:
                validate_int = is_int(i[1:3])
            else:
                validate_int = is_int(i[1:])
            if cont_line == 0:
                if i[0] == CREATE_CANVAS and number_letter == 3 and validate_int:
                    error = False
                else:
                    error = True
                    break
            else:
                if i[0] == CREATE_LINE and number_letter == 5 and validate_int:
                    error = False
                elif i[0] == CREATE_RECTANGLE and number_letter == 5 and validate_int:
                    error = False
                elif i[0] == BUCKET_FILL and number_letter == 4 and validate_int:
                    error = False
                else:
                    error = True
                    break
            cont_line += 1

        InputFileTest = InputFile(path)
        result = InputFileTest.validate_commands()
        assert result == error
            
                    
                    
                




    # def test_if_integer(self, string):
    #     string_to_int = False
    #     try:
    #         int(string)
    #         string_to_int = True
    #         return string_to_int
    #     except ValueError:
    #         print('Entra en valueerror')
    #         return string_to_int

    # def test_selector(self, list_line, list_result):
    #     canvas_created = list_result[0]
        
    #     if canvas_created == False:
            
    #         if list_line[0] == CREATE_CANVAS:
    #             width = int(list_line[1])
    #             height = int(list_line[2])
    #             DrawingTool = ManageCommandCanvasFactory(list_line, width, height)
    #             DrawingTool.find_points()
    #             drawing_tool = DrawingTool.create()
    #             DrawingTool.print_canvas()
    #             canvas_created = True
    #             list_result[0] = canvas_created
    #             list_result.append(drawing_tool)
                
    #         else:
    #             print("Canvas hasn't been created")
    #     else:
    #         canvas = list_result[1]
    #         if list_line[0] == CREATE_LINE:
    #             Line1 = ManageCommandLineFactory(list_line)
    #             Line1.find_points()
    #             drawing_tool = Line1.create(canvas)
    #             Line1.print_canvas(drawing_tool)
    #             list_result[1] = drawing_tool
    #         elif list_line[0] == CREATE_RECTANGLE:
    #             Rectangle1 = ManageCommandRectangleFactory(list_line)
    #             coordinates = Rectangle1.find_points()
    #             history_rectangle.append(coordinates)
    #             print('History rectangle = ', history_rectangle)
    #             drawing_tool = Rectangle1.create(canvas)
    #             Rectangle1.print_canvas(drawing_tool)
    #             list_result[1] = drawing_tool
    #         elif list_line[0] == BUCKET_FILL:
    #             BucketFill1 = ManageCommandBucketFillFactory(list_line)
    #             BucketFill1.find_points()
    #             drawing_tool = BucketFill1.create(canvas, history_rectangle)
    #             BucketFill1.print_canvas(drawing_tool)
    #             list_result[1] = drawing_tool
    #         elif list_line[0] == CREATE_CANVAS:
    #             print("Canvas has been already created")
    #         else:
    #             print("Option no available")
    #     return list_result
