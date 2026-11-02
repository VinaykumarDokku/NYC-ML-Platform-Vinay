

import math


def calculate_price_interval(predicted_price, error_margin=0.15):
    if not math.isfinite(predicted_price) or predicted_price < 0:
        raise ValueError("Invalid predicted price")

    if not math.isfinite(error_margin) or not 0 <= error_margin < 1:
        raise ValueError("Invalid error margin")

    return {
        "predicted_price": round(predicted_price, 2),
        "lower_price": round(predicted_price * (1 - error_margin), 2),
        "upper_price": round(predicted_price * (1 + error_margin), 2),
        "error_margin": error_margin,
    }


if __name__ == "__main__":
    print(calculate_price_interval(200))


