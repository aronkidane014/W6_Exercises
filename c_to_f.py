
def conv_c_to_f(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit) 


celsius_values = [100, 45, 19, 0, -7, -40]

for current_temp_C in celsius_values:
    current_temp_F = conv_c_to_f(current_temp_C)
    print(f"{current_temp_C}°C is approximately {current_temp_F}°F")
