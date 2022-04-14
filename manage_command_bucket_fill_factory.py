from manage_command_factory import ManageCommandFactory

class ManageCommandBucketFillFactory(ManageCommandFactory):
    def __init__(self, list_command):
        """Constructor method of this class
        """
        self.list_command = list_command
        self.x1 = 0
        self.y1 = 0
        self.colour_fill = ''

    def find_points(self):
        """Coordinatis with x axis (self.x1) and y axis (self.y1) for filling the             canvas with symbol (self.o1)
        """
        self.x1 = int(self.list_command[1])
        self.y1 = int(self.list_command[2])
        self.colour_fill = self.list_command[3]
        
    def create(self, drawing_tool, history_rectangle):
        """Create and return an multidimensional array Canvas with filling 
        """
        empty_space = ' '
        max_row = len(drawing_tool) - 1
        max_col = len(drawing_tool[0]) - 1
        if ((self.x1 > 0 and self.y1 > 0)
        and (self.x1 < max_col and self.y1 < max_row)):
            cont_rows = 0
            while drawing_tool[self.y1 + cont_rows] [self.x1] == empty_space:
                drawing_tool = self.fill_line(drawing_tool, cont_rows)
                cont_rows += 1
            cont_rows = -1
            while drawing_tool[self.y1 + cont_rows] [self.x1] == empty_space:
                drawing_tool = self.fill_line(drawing_tool, cont_rows)
                cont_rows -= 1
            
            for i in range(1, len(drawing_tool)-1):
                for j in range(1, len(drawing_tool[i])-1):
                    if drawing_tool[i][j] == self.colour_fill:
                        if drawing_tool[i+1][j] == empty_space:
                            drawing_tool[i+1][j] = self.colour_fill
                        if drawing_tool[i][j+1] == empty_space:
                            drawing_tool[i][j+1] = self.colour_fill
                        if drawing_tool[i-1][j] == empty_space:
                            drawing_tool[i-1][j] = self.colour_fill
                        if drawing_tool[i][j-1] == empty_space:
                            drawing_tool[i][j-1] = self.colour_fill
        else:
            print('no se puede rellenar')

        return drawing_tool

    def fill_line(self, drawing_tool, cont_rows):
        empty_space = ' '
        continue_fill_colour = True
        cont_position = 0
        while continue_fill_colour:
            if drawing_tool[self.y1 + cont_rows][self.x1 + cont_position] == empty_space:
                drawing_tool[self.y1 + cont_rows][self.x1 + cont_position] = self.colour_fill
            else:
                continue_fill_colour = False
            cont_position += 1
        continue_fill_colour = True
        cont_position = -1
        while continue_fill_colour:
            if drawing_tool[self.y1 + cont_rows][self.x1 + cont_position] == empty_space:
                drawing_tool[self.y1 + cont_rows][self.x1 + cont_position] = self.colour_fill
            else:
                continue_fill_colour = False
            cont_position -= 1
        return drawing_tool

    def print_canvas(self, drawing_tool):
        """Print Canvas updated 
        """
        for i in range(len(drawing_tool)):
            for j in range(len(drawing_tool[i])):
                print(drawing_tool[i][j], end='')
            print()
        