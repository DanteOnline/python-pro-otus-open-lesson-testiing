def validate_order(user, cart, payment, delivery):
    if not user.is_authenticated:
        raise ValueError("User not authenticated")

    if not cart:
        raise ValueError("Cart is empty")

    if not payment:
        if user.balance >= cart.total:
            payment = "balance"
        else:
            raise ValueError("No payment method provided")

    if delivery == "pickup":
        if not user.has_pickup_option:
            raise ValueError("Pickup not available for user")
    elif delivery == "courier":
        if user.address is None:
            raise ValueError("No delivery address provided")
        if user.address.city not in ["Moscow", "SPb"]:
            raise ValueError("Delivery not available to this city")
    else:
        raise ValueError("Invalid delivery method")

    return True
