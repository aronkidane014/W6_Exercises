
def get_supplier_code(part_code):
    """Returns the supplier code from the part code."""
    return part_code.split(':')[0]


def get_product_num(part_code):
    """Returns the product number from the part code."""
    return part_code.split(':')[1].split('-')[0]


def get_size(part_code):
    """Returns the size from the part code."""
    size_code = part_code.split('-')[1]
    
    size_map = {'L': 'large', 'M': 'medium', 'S': 'small'}
    return size_map.get(size_code, size_code)  


part_code1 = "ACME:123-L"
part_code2 = "DI:12345-M"
part_code3 = "ACE:1-12"


part_codes = [part_code1, part_code2, part_code3]


for part_code in part_codes:
    supplier = get_supplier_code(part_code).capitalize()
    product_num = get_product_num(part_code)
    size = get_size(part_code)

    print(f"Part #{product_num}, size {size}, supplied by {supplier}")
