# import pandas as pd
# import random

# def generate_data(n=300):
#     data = []

#     for _ in range(n):
#         interest = random.randint(10, 60)
#         late_fee = random.randint(100, 2000)
#         annual_fee = random.randint(0, 10000)
#         billing_cycle = random.randint(15, 45)
#         min_payment = random.randint(1, 20)
#         disclosure = random.choice([0, 1])  # 1 = Yes, 0 = No

#         # Compliance rules
#         if (
#             interest > 40 or
#             late_fee > 1000 or
#             annual_fee > 5000 or
#             billing_cycle < 25 or
#             min_payment < 5 or
#             disclosure == 0
#         ):
#             label = 0  # Non-Compliant
#         else:
#             label = 1  # Compliant

#         data.append([
#             interest,
#             late_fee,
#             annual_fee,
#             billing_cycle,
#             min_payment,
#             disclosure,
#             label
#         ])

#     df = pd.DataFrame(data, columns=[
#         "interest_rate",
#         "late_fee",
#         "annual_fee",
#         "billing_cycle",
#         "min_payment",
#         "disclosure",
#         "label"
#     ])

#     return df


# if __name__ == "__main__":
#     df = generate_data(300)
#     df.to_csv("backend/data/data.csv", index=False)
#     print("Dataset created at backend/data/data.csv")

import pandas as pd
import random

def generate_compliant():
    return [
        random.randint(10, 40),   # interest (safe)
        random.randint(100, 1000),
        random.randint(0, 5000),
        random.randint(25, 45),
        random.randint(5, 20),
        1,  # disclosure = yes
        1   # label
    ]

def generate_non_compliant():
    interest = random.randint(10, 60)
    late_fee = random.randint(100, 2000)
    annual_fee = random.randint(0, 10000)
    billing_cycle = random.randint(15, 45)
    min_payment = random.randint(1, 20)
    disclosure = random.choice([0, 1])

    # Force at least 2 violations
    violations = 0

    if interest > 40:
        violations += 1
    if late_fee > 1000:
        violations += 1
    if annual_fee > 5000:
        violations += 1
    if billing_cycle < 25:
        violations += 1
    if min_payment < 5:
        violations += 1
    if disclosure == 0:
        violations += 1

    if violations < 2:
        # force one violation
        interest = random.randint(41, 60)

    return [
        interest,
        late_fee,
        annual_fee,
        billing_cycle,
        min_payment,
        disclosure,
        0
    ]


def generate_data(n=300):
    data = []

    for _ in range(n // 2):
        data.append(generate_compliant())

    for _ in range(n // 2):
        data.append(generate_non_compliant())

    random.shuffle(data)

    df = pd.DataFrame(data, columns=[
        "interest_rate",
        "late_fee",
        "annual_fee",
        "billing_cycle",
        "min_payment",
        "disclosure",
        "label"
    ])

    return df


if __name__ == "__main__":
    df = generate_data(300)
    df.to_csv("backend/data/data.csv", index=False)
    print("✅ Balanced dataset created")