def GainOuCoupon(Class):
    if (Class.Typologie == "coupon autocall"):
        Class.GainOuCoupon = "gain"

    else:
        Class.GainOuCoupon = "coupon fixe"