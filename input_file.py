from manage_command_canvas_factory import ManageCommandCanvasFactory
from manage_command_line_factory import ManageCommandLineFactory
from manage_command_rectangle_factory import ManageCommandRectangleFactory
from manage_command_bucket_fill_factory import ManageCommandBucketFillFactory


class InputFile:
    def __init__(self, path):
        self.path = path
        self.list_command = []
        self.CREATE_CANVAS = 'C'
        self.CREATE_LINE = 'L'
        self.CREATE_RECTANGLE = 'R'
        self.BUCKET_FILL = 'B'
        self.history_rectangle = []

    def read_file(self):
        """Read input.txt file, where are the commands for drqawingtool
        """
        self.path = 'input.txt'
        file = open(self.path, "r")
        cont_line = 0
        line = file.readlines()
        while (cont_line < len(line)):
            cont_line += 1
        file.close()
        return line

    def validate_commands(self, line, number_line):
        """validates if the values of input file  are valid for the drawingtool to work  
        """
        self.list_command = line.split(" ")
        error = False
        
        number_letter = len(self.list_command)
        if self.list_command[0] == self.BUCKET_FILL:
            validate_int = self.is_int(self.list_command[1:3])
        else:
            validate_int = self.is_int(self.list_command[1:])
        
        if number_line == 0:
            if self.list_command[0] == self.CREATE_CANVAS and number_letter == 3 and validate_int:
                error = False
            else:
                error = True
        else:
            if self.list_command[0] == self.CREATE_LINE and number_letter == 5 and validate_int:
                error = False
            elif self.list_command[0] == self.CREATE_RECTANGLE and number_letter == 5 and validate_int:
                error = False
            elif self.list_command[0] == self.BUCKET_FILL and number_letter == 4 and validate_int:
                error = False
            else:
                error = True
        return error

    def is_int(self, list_with_number):
        """validates if the values must be integers, really can be changed to integer  
        """
        string_to_int = True
        for i in list_with_number:
            i = i.replace('\n', '')
            string_to_int = i.isnumeric()
            if string_to_int == False:
                return string_to_int
        return string_to_int

    def selector(self, list_line, list_result):
        canvas_created = list_result[0]
        
        if canvas_created == False:
            
            if list_line[0] == self.CREATE_CANVAS:
                width = int(list_line[1])
                height = int(list_line[2])
                DrawingTool = ManageCommandCanvasFactory(list_line, width, height)
                DrawingTool.find_points()
                drawing_tool = DrawingTool.create()
                DrawingTool.print_canvas()
                canvas_created = True
                list_result[0] = canvas_created
                list_result.append(drawing_tool)
                
            else:
                print("Canvas hasn't been created")
        else:
            canvas = list_result[1]
            if list_line[0] == self.CREATE_LINE:
                Line1 = ManageCommandLineFactory(list_line)
                Line1.find_points()
                drawing_tool = Line1.create(canvas)
                Line1.print_canvas(drawing_tool)
                list_result[1] = drawing_tool
            elif list_line[0] == self.CREATE_RECTANGLE:
                Rectangle1 = ManageCommandRectangleFactory(list_line)
                coordinates = Rectangle1.find_points()
                self.history_rectangle.append(coordinates)
                drawing_tool = Rectangle1.create(canvas)
                Rectangle1.print_canvas(drawing_tool)
                list_result[1] = drawing_tool
            elif list_line[0] == self.BUCKET_FILL:
                BucketFill1 = ManageCommandBucketFillFactory(list_line)
                BucketFill1.find_points()
                drawing_tool = BucketFill1.create(canvas, self.history_rectangle)
                BucketFill1.print_canvas(drawing_tool)
                list_result[1] = drawing_tool
            elif list_line[0] == self.CREATE_CANVAS:
                print("Canvas has been already created")
            else:
                print("Option no available")
        return list_result