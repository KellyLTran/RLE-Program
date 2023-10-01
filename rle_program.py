
# Translates data (RLE or raw) a hexadecimal string without delimiters
# Ex: to_hex_string([3, 15, 6, 4]) yields string "3f64"
def to_hex_string(data):
    hex_data = ''

    # for loop evaluates data from the index 0 to the end of the list
    for item in data[0:]:

        # Gets the hex value of item
        hex_value = hex(item)

        # Gets rid of delimiters in hex string and adds it to the list
        hex_data += hex_value[2:]
    return hex_data

# Returns number of runs of data in an image data set
# Ex: count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields integer 2
def count_runs(flat_data):

    # Variable current is assigned to the value in the first item of the list
    current = flat_data[0]

    # count is defined as 1 to account for the first item
    count = 1
    total_count = 0

    # for loop evaluates data from index 1 to the end of the list
    for item in flat_data[1:]:

        # We only increment output integer by 1 when the next item is a new item
        if current != item:
            current = item
            count += 1

        # Otherwise, the total_count is incremented by 1 to keep track of total number of runs
        else:
            total_count += 1

        # If run is greater than 15 items, then leftover values are broken into a new run to keep track of its count
        if total_count > 15:
            count += 1

            # total_count is reset
            total_count = 0
    return count

# Returns encoding (in RLE) of the raw data passed in to generate RLE representation of a data
# Ex: encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields list [3, 15, 6, 4]
def encode_rle(flat_data):
    current = flat_data[0]
    count = 1

    # Creates an empty list for the necessary values to be added to
    encoded_list = []

    for item in flat_data[1:]:

        # Increments count variable by 1 if the first item in the list equals the next item
        if current == item:
            count += 1

            # If the count is greater than 15 items or pixels, then leftover values are broken into a new run
            if count > 15:

                # count is decremented by 1 to reset it because count was incremented by 1 before this if statement
                encoded_list.append(count - 1)
                encoded_list.append(current)
                current = item
                count = 1

        # When previous item does not equal next item, the count and current item appends to the encoded list
        else:
            encoded_list.append(count)
            encoded_list.append(current)
            current = item
            count = 1

    # Accounts for the last item of the last run of the data list
    encoded_list.append(count)
    encoded_list.append(item)
    return encoded_list

# Returns decompressed size RLE data; used to generate flat data from RLE encoding
# Ex: get_decoded_length([3, 15, 6, 4]) yields integer 9
def get_decoded_length(rle_data):
    sum = 0

    # for loop evaluates even index positions and enumerates data for iteration counter
    for index, item in enumerate(rle_data):

        # Checks for even numbered index positions
        if index % 2 == 0:

            # Increments sum by the item in that even index position
            sum += item
    return sum

# Returns the decoded data set from RLE encoded data
# Ex: decode_rle([3, 15, 6, 4]) yields list [15, 15, 15, 4, 4, 4, 4, 4, 4]
def decode_rle(rle_data):
    decoded_list = []

    # for loop evaluates even index positions and enumerates data to iterate over the list
    for index, item in enumerate(rle_data):
        if index % 2 == 0:

            # Assigns item in that index position to count
            count = item
        else:
            # Range in for loop accounts for how many times the item must be added to the decoded list
            for i in range(count):

                # Appends the item in odd index position to the decoded list
                decoded_list.append(item)
    return decoded_list

# Translates a string in hexadecimal format into byte data
# Ex: string_to_data ("3f64") yields list [3, 15, 6, 4]
def string_to_data(data_string):
    count = 0
    int_list = []
    for item in data_string:

        # Gets the integer value of the hexadecimal string
        decimal = int(item, 16)

        # Appends the decimal to the list of int_list
        int_list.append(decimal)
    return int_list

'''
Title: Python – Convert Hexadecimal String to Integer
Author: Data Science Parichay
Date: n.d.
Code Version: Python
Availability: https://datascienceparichay.com/article/python-convert-hexadecimal-string-to-integer/
'''

'''
Title: COP3502C - Prog Fundamentals 1 - Fall 2022
Author: Lisha Zhou
Date: Oct. 11, 2022
Code Version: Python
Availability: https://ufl.zoom.us/rec/play/3ZTpfYQCTGazO0ILzrC63C_hf2tGdtNpFe0ve4UYdvcMivJUCoVwWG9fN-qauti3Z43gjmSUBbWI8iAS.elX8bVLpPzIRPoc3
'''

# Translates RLE data into a human-readable representation
# Ex: to_rle_string([15, 15, 6, 4]) yields string "15f:64"
def to_rle_string(rle_data):
    result = ''

    # Gets the length of RLE data
    data_len = len(rle_data)

    # for loop evaluates even index positions and enumerates data for iteration counter
    for index, item in enumerate(rle_data):

        # Checks for even index positions and adds to the string
        if index % 2 == 0:
            result += str(item)

        # For odd index positions, the item is converted to hex format first than added to the string
        else:
            hex_value = hex(item)
            result += str(hex_value[2:])

            # If the odd index position does not equal the last item of the list, then add a colon to the string
            # This prevents a colon at the end of the returned result
            if index != data_len - 1:
                result += ':'
    return result


# Translates a string in human-readable RLE format (with delimiters) into RLE byte data
# Ex: string_to_rle("15f:64") yields list [15, 15, 6, 4]
def string_to_rle(rle_string):

    # Splits the string by each colon present in the string and assigns it to variable strings
    # Ex: 15f:64 splits to ['15f', '64']
    strings = rle_string.split(':')
    result = []

    # for loop iterates through strings and evaluates even index positions
    for index, item in enumerate(strings):

        # Gets length of each item in the list
        element_len = len(item)

        # If the length is 3, then the first two characters are decimal numbers
        if element_len == 3:

            # Converts first two characters to integers and appends them to the list
            result.append(int(item[0:2]))

            # Assigns last character to variable hex_value
            hex_value = item[2]

            # Gets the integer value of the hexadecimal string and appends to the list
            decimal_value = int(hex_value, 16)
            result.append(decimal_value)

        # Otherwise, the length is treated as 2
        else:

            # Converts the first decimal value to an integer and appends it to the list
            result.append(int(item[0:1]))
            hex_value = item[1]

            # Gets the integer value of the hexadecimal string and appends to the list
            decimal_value = int(hex_value, 16)
            result.append(decimal_value)
    return result


if __name__ == '__main__':
    # Imports the console module provided
    from console_gfx import ConsoleGfx

    # Displays the welcome message
    print("Welcome to the RLE image encoder!")

    # Displays the color test
    print("\nDisplaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    # Defines image_data for use in loop
    image_data = None

    # Creates an empty list to store the user input from options 3, 4, and 5 for use in option 7, 8, and 9
    rle_encode = []

    # Keeps track of user's selection of option 5 or not
    option_5 = False

    # Adds a new line for the initial print of the menu before the loop
    print()

    # Creates a loop to allow the user to generate files until they choose to exit
    while True:

        # Displays the RLE Menu
        print("\nRLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data")

        # Assigns user's input of a menu choice to variable option and expects user's input to be an integer
        option = int(input("\nSelect a Menu Option: "))

        # Exits the program when user inputs 0 as a menu option
        if option == 0:
            exit()

        # Displays prompt for user to input a file name from testfiles when user inputs 1 as menu option
        elif option == 1:
            filename = input("Enter name of file to load: ")

            # Loads file based on the filename user inputs and assigns this to variable image_data
            image_data = ConsoleGfx.load_file(filename)

        # Loads image data from test_image when user inputs 2 as menu option
        elif option == 2:

            # Assigns ConsoleGfx.test_image to variable image_data
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.")

        # Reads RLE data from user input in decimal notation with delimiters
        elif option == 3:

            # Assigns user input to variable rle_string
            rle_string = input("Enter an RLE string to be decoded: ")

            # Passes variable rle_string with function string_to_rle to translate rle string to RLE byte data
            rle_data = string_to_rle(rle_string)

            # Decodes RLE byte data to decompress it for use
            rle_decode = decode_rle(rle_data)

            # Encodes decompressed data to generate RLE representation of data
            rle_encode = encode_rle(rle_decode)

        # Reads RLE data from user input in hexadecimal notation without delimiters
        elif option == 4:
            rle_hex_string = input("Enter the hex string holding RLE data: ")

            # Passes variable assigned to user input with function string_to_data to translate hex string into RLE byte data
            rle_data = string_to_data(rle_hex_string)
            rle_decode = decode_rle(rle_data)
            rle_encode = encode_rle(rle_decode)

        # Reads raw (flat) data from user input in hexadecimal notation
        elif option == 5:

            # Variable option_5 becomes true when user selects option 5
            option_5 = True
            flat_string = input("Enter the hex string holding flat data: ")
            rle_data = string_to_data(flat_string)

        # Displays the image chosen by calling image_data when user inputs 6
        elif option == 6:
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)

        # Converts the current data into a human-readable RLE representation with delimiters
        elif option == 7:

            # If option 5 is not chosen, the encoded data becomes decoded with the decode_rle function
            # Ex: the encoded data of [3, 15, 6, 4] is decoded to [15, 15, 15, 4, 4, 4, 4, 4, 4]
            if option_5 == False:
                flat_data = decode_rle(rle_encode)
                rle_encode = encode_rle(flat_data)

                # Passes rle_data as parameter for function to_rle_string to translate RLE data into human-readable representation
                rle_string = to_rle_string(rle_data)
                print("RLE representation: " + str(rle_string))

            # Otherwise, the decoding step is skipped since option 5 does not need to be converted to RLE Byte Data
            else:
                rle_encode = encode_rle(rle_data)
                rle_string = to_rle_string(rle_encode)
                print("RLE representation: " + str(rle_string))

        # Converts the current data into RLE hexadecimal representation without delimiters
        elif option == 8:

            if option_5 == False:
                flat_data = decode_rle(rle_encode)
                rle_encode = encode_rle(flat_data)
                rle_hex = to_hex_string(rle_encode)
                print("RLE hex values: " + str(rle_hex))
            else:
                rle_encode = encode_rle(rle_data)
                rle_hex = to_hex_string(rle_encode)
                print("RLE hex values: " + str(rle_hex))

        # Displays the current flat data in hexadecimal representation without delimiters
        elif option == 9:
            if option_5 == False:
                # Option 9 skips the encoding step because it does not need to be converted to RLE Byte Data
                flat_data = decode_rle(rle_encode)
                flat_hex_string = to_hex_string(flat_data)
                print("Flat hex values: " + str((flat_hex_string)))
            else:
                # Option 5 skips the decoding step as it does in option 7 and 8 too
                flat_hex_string = to_hex_string(rle_data)
                print("Flat hex values: " + str((flat_hex_string)))