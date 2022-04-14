def create_canvas_for_test(width, height):
    test_canvas = [x[:] for x in [['  '] * (width + 2)] * (height + 2)]
    horizontal_wall = '-'
    vertical_wall = '|'
    empty_space = ' '
    for i in range(height + 2):
        for j in range(width + 2):
            if i == 0 or i == height + 1:
                test_canvas[i][j] = horizontal_wall
            elif j == 0 or j == width + 1:
                test_canvas[i][j] = vertical_wall
            else:
                test_canvas[i][j] = empty_space
    return test_canvas