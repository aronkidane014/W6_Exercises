
def conv_f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius)  

fahrenheit_values = [212, 90, 72, 32, 0, -40]

for current_temp_F in fahrenheit_values:
    current_temp_C = conv_f_to_c(current_temp_F)
    print(f"{current_temp_F}°F is approximately {current_temp_C}°C")
