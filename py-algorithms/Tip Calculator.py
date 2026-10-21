def calculate_tips(meal_price, custom_tip):
    price =meal_price.strip("$")
    price = float(price)
    custom_decimal = float(custom_tip.strip("%")) / 100
    first_tip = price * 0.15
    second_tip  = price * 0.20
    third_tip = price * custom_decimal
    return [f"${first_tip:.2f}", f"${second_tip:.2f}", f"${third_tip:.2f}"]