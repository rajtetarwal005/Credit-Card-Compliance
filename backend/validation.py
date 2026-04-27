from fastapi import HTTPException

def validate_input(data):
    errors = []

    if not (1 <= data.interest_rate <= 60):
        errors.append("Interest rate must be between 1 and 60")

    if not (0 <= data.late_fee <= 2000):
        errors.append("Late fee must be between 0 and 2000")

    if not (0 <= data.annual_fee <= 10000):
        errors.append("Annual fee must be between 0 and 10000")

    if not (15 <= data.billing_cycle <= 45):
        errors.append("Billing cycle must be between 15 and 45")

    if not (1 <= data.min_payment <= 100):
        errors.append("Minimum payment must be between 1 and 100")

    if data.disclosure not in [0, 1]:
        errors.append("Disclosure must be 0 or 1")

    if errors:
        raise HTTPException(status_code=400, detail=errors)