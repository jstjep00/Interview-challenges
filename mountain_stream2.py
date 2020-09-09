def main():
    closest_n_points = []               # instead of checking all points in array we will just keep the closest n       
    input_numbers_array = []            # one array for all number inputs

    # first input of C points that we will query later, raise exception if not [1, 10^6] or integer
    try:
        number_of_points = int(input())
    except ValueError:
        print("You didn't enter a number of points in cartesian system")

    if not (number_of_points <= 10**6) or not (number_of_points >= 1):
        raise Exception("Number of points you want to print out need to be between 1 and 10^6")

    # simple while loop we break out of in case a 3 is invoked, everything else is ignored through continue
    while(True):
        input_string = input()

        # ignore if empty input
        if input_string == "":
            continue
        # input string has to start with 1, be a list of 3 elements to be added to be a point command
        elif (input_string[0] == "1") and (len(input_string.split(" ")) == 3):
            input_string = input_string.split(" ")
            for i in input_string:
                # if an element in split up string is a digit, add it if its not just remove all from input array and continue
                if i.isdigit():
                    input_numbers_array.append(int(i))
                else:
                    input_numbers_array = []
                    continue
        # if single digit is entered with no spaces and that digit isn't a 1 then append to array
        elif input_string.isdigit():
            if int(input_string) != 1:
                input_numbers_array.append(int(input_string))
        # if anything else is entered like a word or character then ignore it
        else:
            continue
        
        # if input array is empty (mostly because of wrong point input or empty string input)
        if input_numbers_array == []:
            continue
        # if first number in input array is 1 then check if subsequent numbers are in [-1000, 1000]
        elif input_numbers_array[0] == 1:
            if input_numbers_array[1] in range(-1000, 1000) and input_numbers_array[2] in range(-1000, 1000):
                # if number C we selected in beginning is fulfilled criteria then we add point to array of n closest
                # sort by distance to origin and remove the farthest point from the closest_n_points array so we don't have to lookup
                # all the points entered and compare their lengths at request of printing command
                closest_n_points.append([input_numbers_array[1], input_numbers_array[2]])
                if len(closest_n_points) > number_of_points:
                    closest_n_points.sort(key= lambda x: x[0]**2 + x[1]**2)
                    closest_n_points.pop(-1)
        # simple for loop to go through all points and format their output
        elif input_numbers_array[0] == 2:
            for point in closest_n_points:
                print("{} {}".format(point[0], point[1]))
        # end the while loop with 3
        elif input_numbers_array[0] == 3:
            break
        # reset number array 
        input_numbers_array = []

if __name__ == '__main__':
    main()

