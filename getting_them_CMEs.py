

def max_cme(maximum_hours, webinars_hours, webinars_profits, number_of_webinars):
    matrix = [[0 for _ in range(maximum_hours+1)] for _ in range(number_of_webinars+1)]     # 2D array full of zeroes

    '''
       Solving the subproblems we build the matrix from bottom up, adding up all possible combinations that add up to maximum hours
       Each row represents a recursive webinar selection and each collumn represents amount of hours left (from 0 to maximum_hours)
    '''
    for i in range(number_of_webinars + 1):
        for j in range(maximum_hours + 1):
            if j == 0:                                          # first collumn is always zero since there is no hours to use
                matrix[i][j] = 0
            elif webinars_hours[i-1] <= j and i != 0:
                matrix[i][j] = max(webinars_profits[i-1]        # check if current highest profit is bigger than previous row 
+ matrix[i-1][j-webinars_hours[i-1]],  matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]                   # if it is not bigger use last highest profit
    matrix.pop(0)                                               # remove empty array
    print( matrix[number_of_webinars-1][maximum_hours])
    return matrix

def find_minimum(matrix, webinars_hours, webinars_profits):
    i = len(matrix)
    j = len(matrix[0])
    '''
        Go through matrix checking if highest profit is bigger than previous
        if it is then the current "row" of webinar isn't the one we used in highest profit combination
        if it is then we subtract webinars hours of current row and check the row above to see if we selected that webinar
            from the hours left
    '''
    while i > 0:
        if matrix[i-1][j-1] > matrix[i-2][j-1] and i != 0:
            print("{} {}".format(webinars_hours[i-1], webinars_profits[i-1]))
            i -= 1
            j -= webinars_profits[i-1]
        else:
            i -= 1


def main():
    maximum_hours = int(input())
    number_of_webinars = int(input())
    webinars_hours = input().split(" ")
    webinars_profits = input().split(" ")

    for i in range(number_of_webinars):
        webinars_hours[i] = int(webinars_hours[i])
        webinars_profits[i] = int(webinars_profits[i])


    matrix = max_cme(maximum_hours, webinars_hours, webinars_profits, number_of_webinars)
    find_minimum(matrix, webinars_hours, webinars_profits)


if __name__ == '__main__':
    main()