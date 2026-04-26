from pydantic import BaseModel

class CardInput(BaseModel):
    interest_rate: float
    late_fee: float
    annual_fee: float
    billing_cycle: int
    min_payment: float
    disclosure: int  # 1 = Yes, 0 = No