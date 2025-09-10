def _student_discount(price):
    return price * 0.9 if price > 1000 else price * 0.95
def _regular_discount(price):
    return price * 0.85 if price > 2000 else price
DISCOUNT_STRATEGIES = {
    "student": _student_discount,
    "regular": _regular_discount,
}
def discount(price, category):
    strategy = DISCOUNT_STRATEGIES.get(category, _regular_discount)
    return strategy(price)
print(discount(1500, "student"))
print(discount(2500,"regular"))
print(discount(800,"student"))
print(discount(1500,"regular"))