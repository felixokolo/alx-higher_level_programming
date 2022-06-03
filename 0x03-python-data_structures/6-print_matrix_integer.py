#!/usr/bin/python3

if __name__ == "__main__":
    def print_matrix_integer(matrix=[[]]):
        for row in matrix:
            for elem, idx in zip(row, range(len(row))):
                print("{}".format(elem), end='')
                if idx < len(row)-1:
                    print('', end=' ')
            print('')
