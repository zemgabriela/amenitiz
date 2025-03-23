from collections import Counter

################## CASES ##################
# case 1: Buy X, get Y free
def free_product_included(discount_dict, count_occurances, price_dict):
    """
    Case 1: After purchasing 'promo_amount', you get 'promo_free' items for free.
    Returns the final price after applying the discount, only for discounted products.
    """
    must_pay_quantities = count_occurances.copy()
    total_price = 0

    for product, details in discount_dict.items():
        if details['discount_type'] == "free_product_included":
            promo_amount = details['promo_amount']
            promo_free = details['promo_free']
            if product in count_occurances:
                quantity = count_occurances[product]
                free_items = (quantity // (promo_amount + promo_free)) * promo_free
                must_pay_quantities[product] = quantity - free_items
                total_price += round(must_pay_quantities[product] * price_dict[product],2)

    return total_price

# case 2: After X, each additional unit has a fixed price
def fixed_price_after_x(discount_dict, count_occurances, price_dict):
    """
    Case 2: After x amount, each additional unit costs a given price y.
    """
    total_price = 0

    for product, details in discount_dict.items():
        if details['discount_type'] == "fixed_price_after_x":
            promo_amount = details['promo_amount']
            new_price = details['new_price']
            if product in count_occurances and count_occurances[product] >= promo_amount:
                total_price += round(count_occurances[product] * new_price,2)  # Price for first promo_amount units
            elif product in count_occurances:
                total_price += round(count_occurances[product] * price_dict[product],2)
    
    return total_price

# case 3: After purchasing X, all units are a fraction of the original price
def fraction_price_after_x(discount_dict, count_occurances, price_dict):
    """
    Case 3: After purchasing 'promo_amount', units will cost a fraction of the original price.
    """
    total_price = 0

    for product, details in discount_dict.items():
        if (details['discount_type'] == "fraction_price_after_x") & (product in count_occurances):
            promo_amount = details['promo_amount']
            fraction = details['fraction']
            if product in count_occurances and count_occurances[product] >= promo_amount:
                total_price += round(count_occurances[product] * price_dict[product] * fraction, 2)
            elif product in count_occurances:
                total_price += round(count_occurances[product] * price_dict[product],2)

    return total_price

# case: No discount for non-discounted products
def full_price_for_non_discounted(discount_dict, count_occurances, price_dict):
    """
    Case: For products that are not on sale, calculate the total price at their full price.
    Returns the total price for the non-discounted products.
    """
    total_price = 0
    for product in count_occurances:
        if product not in discount_dict:
            total_price += round(count_occurances[product] * price_dict[product],2)

    return total_price

################## CART FUNCTION ##################
# calculating_price function
def calculating_price(cart, discount_dict, price_dict):
    count_occurances = {product: cart.count(product) for product in set(cart)}

    # Apply all functions
    free_product_price = free_product_included(discount_dict, count_occurances, price_dict)
    fixed_price_price = fixed_price_after_x(discount_dict, count_occurances, price_dict)
    fraction_price = fraction_price_after_x(discount_dict, count_occurances, price_dict)
    full_price = full_price_for_non_discounted(discount_dict, count_occurances, price_dict)

    # Final total price
    return free_product_price + fixed_price_price + fraction_price + full_price

    