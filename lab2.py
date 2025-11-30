def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")
          
def get_user_input():
    print("user_input")
    x = input()
    split_list = x.split(",")
    float_list = [float(i) for i in split_list]
    return float_list

def cal_average_temperature(temp_list):
    print("cal_average")
    avg = sum(temp_list) / len(temp_list)
    return avg

def find_min_max_temperature(temp_list):
    print("find_min_max")
    return min(temp_list), max(temp_list)

def main():
    # 1. Display menu
    display_main_menu()

    # 2. Get the user input list (floats)
    temp_list = get_user_input()

    # 3. Calculate average
    avg = cal_average_temperature(temp_list)
    print("Average temperature:", avg)

    # 4. Find min and max
    minimum, maximum = find_min_max_temperature(temp_list)
    print("Minimum temperature:", minimum)
    print("Maximum temperature:", maximum)
    

# Run main if file is executed directly
if __name__ == "__main__":
    main()





