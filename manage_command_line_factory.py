from manage_command_factory import ManageCommandFactory


class ManageCommandLineFactory(ManageCommandFactory):
    def __init__(self, list_command):
        """Constructor method of this class
        """
        self.list_command = list_command
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def find_points(self):
        """Select width and height of command for creating Drawingtool
        """
        self.x1 = int(self.list_command[1])
        self.y1 = int(self.list_command[2])
        self.x2 = int(self.list_command[3])
        self.y2 = int(self.list_command[4])

    def create(self, drawing_tool):
        """Create and return an multidimensional array Canvas with lines
        """
        x = 'x'
        max_row = len(drawing_tool) - 1
        max_col = len(drawing_tool[0]) - 1
        if ((self.x1 > 0 and self.x2 > 0 and self.y1 > 0 and self.y2 > 0)
                and (self.x1 < max_col and self.x2 < max_col
                     and self.y1 < max_row and self.y2 < max_row)
                and (self.x1 == self.x2 or self.y1 == self.y2)):  
            if self.x1 == self.x2:
                if self.y1 <= self.y2:
                    for i in range(self.y1, self.y2+1):
                        drawing_tool[i][self.x1] = x
                else:
                    for i in range(self.y2, self.y1+1):
                        drawing_tool[i][self.x1] = x
            elif self.y1 == self.y2:
                if self.x1 <= self.x2:
                    for i in range(self.x1, self.x2+1):
                        drawing_tool[self.y1][i] = x
                else:
                    for i in range(self.x2, self.x1+1):
                        drawing_tool[self.y1][i] = x
        else:
            print('no se puede escribir linea')
        return drawing_tool

    def print_canvas(self, drawing_tool):
        """Print Canvas created
        """
        for i in range(len(drawing_tool)):
            for j in range(len(drawing_tool[i])):
                print(drawing_tool[i][j], end='')
            print()
