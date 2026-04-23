#default parameters

def greet(name="Sam", greeting="Hello!"):
    return f"{greeting}, {name}!"

def calculate_shipping(price, discount_rate=0.0, shipping_fee=3000):
    total = price * (1 - (discount_rate/100)) + shipping_fee
    return f"{discount_rate} 할인, 배송비 {shipping_fee}"

def format_leaderboard_entry(rank, name, score, label):
    
