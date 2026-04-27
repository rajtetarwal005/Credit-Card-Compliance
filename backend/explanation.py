def get_explanation(data):
    reasons = []

    if data.interest_rate > 40:
        reasons.append("High interest rate")

    if data.late_fee > 1000:
        reasons.append("High late payment fee")

    if data.annual_fee > 5000:
        reasons.append("High annual fee")

    if data.billing_cycle < 25:
        reasons.append("Short billing cycle")

    if data.min_payment < 5:
        reasons.append("Minimum payment too low")

    if data.disclosure == 0:
        reasons.append("Disclosure not provided")

    return reasons