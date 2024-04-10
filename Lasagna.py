def expected_bake_time():
    return 40

def bake_time_remaining(time_in_oven):
    return 40 - time_in_oven

def prepartion_time_in_minutes(number_of_layers):
    return number_of_layers*2

def total_time_passed(number_of_layers, time_in_oven):
    return number_of_layers*2 + time_in_oven


