# Building a cash register

This app enables you to add products to a cart and computes the total price.

Functions to calculate prices with various discount types, including:
- Buy X, get Y free
- Fixed price after X
- Fractional price after X
(the discount dictionary together with price dictionary are both stored in the data folder)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zemgabriela/amenitiz.git```

2. Navigate to the directory
3. ```pip install -r requirements.txt```
4. ```python main.py``` and select the products in your cart

## Assumptions: 
1. Data folder gets frequently updated -> if the discount changes or becomes inactive, the files get rewritten.
2. All products of a company are stored in price_dict in data folder.
3. Each product has a unique identifier in price_dict, e.g. "GR1" is the unique code for green tea.
4. Each product can have a single discount.
5. I am not including products that are "out-of-stock", assuming it's a cash register and products that are scanned must be available.
