from collections import Counter

def free_product_included(discount_dict, count_occurances, promo_amount = 1, promo_free = 1):
    
    discount_product_list = [product for product, discount in discount_dict.items() if discount == "free_product_included"]
    must_pay_quantities = count_occurances.copy()

    for discount_product in discount_product_list:
        if discount_product in count_occurances:
            free_items = (count_occurances[discount_product] // (promo_amount + promo_free)) * promo_free
            must_pay_quantities[discount_product] = count_occurances[discount_product] - free_items

    return must_pay_quantities