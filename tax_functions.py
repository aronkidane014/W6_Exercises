def get_soc_sec_tax(gross_pay):
    tax_rate = 0.062  # 6.2%
    return round(gross_pay * tax_rate, 2)

def get_medicare_tax(gross_pay):
    tax_rate = 0.0145  
    return round(gross_pay * tax_rate, 2)

def get_federal_tax(gross_pay, withholding_code):
    if withholding_code == 0:
        tax_rate = 0.23  
    elif withholding_code == 1:
        tax_rate = 0.21  
    elif withholding_code == 2:
        tax_rate = 0.195  
    elif withholding_code == 3:
        tax_rate = 0.185  
    elif withholding_code >= 4:
        
        extra_withholdings = withholding_code - 4
        tax_rate = 0.18 - (0.005 * extra_withholdings)  
    else:
        return 0  

    return round(gross_pay * tax_rate, 2)


def display_results():

    person1_gross_pay = 750
    person1_withholding_code = 0
    print(f"Person 1: Gross Pay: ${person1_gross_pay}")
    print(f"Social Security Tax: ${get_soc_sec_tax(person1_gross_pay)}")
    print(f"Medicare Tax: ${get_medicare_tax(person1_gross_pay)}")
    print(f"Federal Tax Withholding: ${get_federal_tax(person1_gross_pay, person1_withholding_code)}")
    print()

    person2_gross_pay = 1550
    person2_withholding_code = 2
    print(f"Person 2: Gross Pay: ${person2_gross_pay}")
    print(f"Social Security Tax: ${get_soc_sec_tax(person2_gross_pay)}")
    print(f"Medicare Tax: ${get_medicare_tax(person2_gross_pay)}")
    print(f"Federal Tax Withholding: ${get_federal_tax(person2_gross_pay, person2_withholding_code)}")
    print()
    person3_gross_pay = 1100
    person3_withholding_code = 5
    print(f"Person 3: Gross Pay: ${person3_gross_pay}")
    print(f"Social Security Tax: ${get_soc_sec_tax(person3_gross_pay)}")
    print(f"Medicare Tax: ${get_medicare_tax(person3_gross_pay)}")
    print(f"Federal Tax Withholding: ${get_federal_tax(person3_gross_pay, person3_withholding_code)}")
    print()
display_results()
