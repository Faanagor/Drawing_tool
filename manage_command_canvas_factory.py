from manage_command_factory import ManageCommandFactory


class ManageCommandCanvasFactory(ManageCommandFactory):
    def __init__(self, list_command, width, height):
        """Constructor method of this class
        """
        #super().__init__()
        self.list_command = list_command
        self.width = width
        self.height = height
        self.canvas = [
            x[:] for x in [['  '] * (self.width + 2)] * (self.height + 2)
        ]

    def find_points(self):
        """Select width and height of command for creating Drawingtool
        """
        self.width = int(self.list_command[1])
        self.height = int(self.list_command[2])

    def create(self):
        """Create and return an multidimensional array Canvas
        """
        horizontal_wall = '-'
        vertical_wall = '|'
        empty_space = ' '
        for i in range(self.height + 2):
            for j in range(self.width + 2):
                if i == 0 or i == self.height + 1:
                    self.canvas[i][j] = horizontal_wall
                elif j == 0 or j == self.width + 1:
                    self.canvas[i][j] = vertical_wall
                else:
                    self.canvas[i][j] = empty_space
        return self.canvas

    def print_canvas(self):
        """Print Canvas created
        """
        for i in range(len(self.canvas)):
            for j in range(len(self.canvas[i])):
                print(self.canvas[i][j], end='')
            print()
        
