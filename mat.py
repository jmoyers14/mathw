
def get_pixel_at(pixel_grid, i, j):
    '''
    Returns the pixel in pixel_grid at row i and column j (zero-indexed).
    Returns 0 if i or j is out of bounds for the given pixel_grid.
    '''
    height  = len(pixel_grid)
    width   = len(pixel_grid[0])
    
    if (j >= width or i >= height or j < 0 or i < 0):
        return 0
    else:
        return pixel_grid[i][j]

    # REMOVE THIS COMMENT AND REPLACE IT WITH YOUR CODE ...

    

def test_get_pixel_at():
    ''' Basic, brief sanity checks for get_pixel_at. '''

    # If all of these tests return true, then your solution to
    # get_pixel_at is probably mostly correct. However, passing
    # these tests does not mean your solution is completely 
    # correct. There are many ways to implement get_pixel_at 
    # that pass these tests and are still wrong. 

    test_grid = [
        [1, 2, 3, 4, 5, 6],
        [0, 2, 4, 6, 8, 10],
        [3, 4, 5, 6, 7, 8]
    ]

    try:
        assert get_pixel_at(test_grid, 0, 0) == 1,   "Call to get_pixel_at(0, 0) should have returned 1."
        assert get_pixel_at(test_grid, -1, 0) == 0,  "Call to get_pixel_at(-1, 0) should have returned 0."
        assert get_pixel_at(test_grid, 0, -1) == 0,  "Call to get_pixel_at(0, -1) should have returned 0."
        assert get_pixel_at(test_grid, -1, -1) == 0, "Call to get_pixel_at(-1, -1) should have returned 0."

        assert get_pixel_at(test_grid, 2, 5) == 8,   "Call to get_pixel_at(2, 5) should have returned 8."
        assert get_pixel_at(test_grid, 3, 5) == 0,   "Call to get_pixel_at(3, 5) should have returned 0."
        assert get_pixel_at(test_grid, 2, 6) == 0,   "Call to get_pixel_at(2, 6) should have returned 0."
        assert get_pixel_at(test_grid, 3, 6) == 0,   "Call to get_pixel_at(3, 6) should have returned 0."

        assert get_pixel_at(test_grid, 1, 3) == 6,   "Call to get_pixel_at(1, 3) should have returned 6."
    except AssertionError as e:
        # Print out a user-friendly error message
        print e

# Run the tests. This method prints nothing if the tests
# pass. This method prints an error message for the first 
# error it encounters.
#test_get_pixel_at()


def average_of_surrounding(pixel_grid, i, j):
    '''
    Returns the unweighted average of the values of the pixel at row i 
    and column j and the eight pixels surrounding it.
    '''

    x = j - 1
    y = i - 1
    width = j + 1
    height = i + 1

    '''
    print "x = %d" % x
    print "y = %d" % y
    print "width  = %d" % width
    print "height = %d" % height
    '''

    pixel_sum = 0
    for col in range(x, width+1):
        for row in range(y, height+1):
            pixel_sum += get_pixel_at(pixel_grid, row, col)

    #print "pixel_sum = %d " % pixel_sum
    # REMOVE THIS COMMENT AND REPLACE IT WITH YOUR CODE ...

    # pixel_sum should be an integer. We intend for this to be 
    # truncating integer division.  
    return pixel_sum / 9


def print_grid(pixel_grid):

    width  = len(pixel_grid[0])
    height = len(pixel_grid)

    for y in range(0, height):
        for x in range(0, width):
            print(pixel_grid[y][x]),
        print "\n"

def test_average_of_surrounding():
    ''' Basic, brief sanity checks for average_of_surrounding. '''
    # Similarly to test_get_pixel_at, passing all of these tests
    # does not guarantee that your implementation of 
    # average_of_surrounding is correct.

    test_grid = [
        [1, 2, 3, 4, 5, 6],
        [0, 2, 4, 6, 8, 10],
        [3, 4, 5, 6, 7, 8]
    ]

    #print get_pixel_at(test_grid, 1, 2)
    #print average_of_surrounding(test_grid, 1, 2)
    try:
        assert average_of_surrounding(test_grid, 1, 4) == 6, "Call to average_of_surrounding(test_grid, 1, 1) should have returned 6"
        assert average_of_surrounding(test_grid, 1, 1) == 2, "Call to average_of_surrounding(test_grid, 1, 1) should have returned 2"
        assert average_of_surrounding(test_grid, 1, 5) == 4, "Call to average_of_surrounding(test_grid, 1, 5) should have returned 4"
        assert average_of_surrounding(test_grid, 0, 5) == 3, "Call to average_of_surrounding(test_grid, 0, 5) should have returned 3"
        assert average_of_surrounding(test_grid, 1, 2) == 4, "Call to average_of_surrounding(test_grid, 1, 2) should have returned 4."
        assert average_of_surrounding(test_grid, 0, 0) == 0, "Call to average_of_surrounding(test_grid, 0, 0) should have returned 0."
        assert average_of_surrounding(test_grid, 2, 5) == 3, "Call to average_of_surrounding(test_grid, 2, 5) should have returned 3."
    except AssertionError as e:
        print e

#test_average_of_surrounding()


def blur(pixel_grid):
    '''
    Given pixel_grid (a grid of pixels), returns a new grid of pixels
    that is the result of blurring pixel_grid. In the output grid, 
    each pixel is the average of that pixel and its eight neighbors in
    the input grid. 
    '''

    # REMOVE THIS COMMENT AND REPLACE IT WITH YOUR CODE ...





#no main functions in python I guess
test_get_pixel_at()
test_average_of_surrounding()

