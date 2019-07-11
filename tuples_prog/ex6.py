# Python | Print unique rows in a given boolean matrix using Set with tuples


def unique_rows(input):
    # convert each row (list) into tuple
    # we are mapping tuple function on each row of
    # input matrix
    input = map(tuple, input)

    # put all rows in set
    result = set(input)

    # print all unique rows
    for row in list(result):
        print (row)

    # Driver program


if __name__ == "__main__":
    input = [[0, 1, 0, 0, 1],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0]]
    unique_rows(input)
