def to_roman(integer_input):
    int_string = str(integer_input)
    int_list = list(int_string)
    # print(construct_roman_array(int_list))
    construct_roman_array(int_list)

def construct_roman_array(int_list):
    result = []
    places_dict = {
        "ones_place": [int_list[-1], "1"],
        "tens_place": [int_list[-2], "10"],
        "hundreds_place": [int_list[-3], "100"],
        "thousands_place": [int_list[-4], "1000"]
    }

    roman_conversion = {
        "5000": 'MMMMM',
        "1000": 'M',
        "500": 'D',
        "100": 'C',
        "50": 'L',
        "10": 'X',
        "5":  'V',
        "1": 'I'
    }

    for k,v in places_dict.items():
        unit_key = str(places_dict[k][1])
        five_key = (str(int(places_dict[k][1])*5))
        roman_unit = roman_conversion[unit_key]
        roman_five = roman_conversion[five_key]
        value = int(v[0])
        if k == "thousands_place":
            for x in range(value):
                result.append(roman_unit)
        elif value < 4:
            for x in range(value):
                result.append(roman_unit)
        elif value == 4:
            result.append(roman_five)
            result.append(roman_unit)
        elif value == 5:
            result.append(roman_five)
        elif value > 5:
            result.append(roman_five)
            for x in range((value - 5)):
                result.append(roman_unit)

    print(''.join(result))

to_roman(4587)
