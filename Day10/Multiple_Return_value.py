def get_sum_and_product(a, b):
    """
    This function takes two numbers and returns their sum and product.
    """
    sum = a + b
    product = a * b
    return sum, product

s, p = get_sum_and_product(10, 5)
print("Sum:", s)
print("Product:", p)