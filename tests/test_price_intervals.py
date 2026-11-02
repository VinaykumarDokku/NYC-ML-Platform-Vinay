import pytest

from src.serving.price_intervals import calculate_price_interval


def test_default_price_interval():
    result = calculate_price_interval(200)
    assert result["predicted_price"] == 200
    assert result["lower_price"] == 170
    assert result["upper_price"] == 230


def test_custom_error_margin():
    result = calculate_price_interval(100, 0.10)
    assert result["lower_price"] == 90
    assert result["upper_price"] == 110


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_price_interval(-100)


def test_invalid_error_margin():
    with pytest.raises(ValueError):
        calculate_price_interval(200, 1.5)
