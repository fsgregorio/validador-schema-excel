import pytest
from datetime import datetime
from src.contract import Sales


def test_sales_with_validate_data():
    validate_data = {
        "email": "person1@example.com",
        "date": datetime.now(),
        "valor": 100.50,
        "product": "Product 1",
        "quantity": 1,
        "category": "category1"
    }
    
    sales = Sales(**validate_data)
    assert sales.email == validate_data["email"]
    assert sales.date == validate_data["date"]
    assert sales.valor == validate_data["valor"]
    assert sales.product == validate_data["product"]
    assert sales.quantity == validate_data["quantity"]
    assert sales.category == validate_data["category"]
    
def test_sales_with_invalid_data():
    invalid_data = {
        "email": "person1",
        "date": "is not a date",
        "valor": -100,
        "product": "",
        "quantity": -1,
        "category": "categor2"
    }
    
    with pytest.raises(ValueError):
        Sales(**invalid_data)
        

# Catogory validate test
def test_sales_category_validate():
    validate_data = {
        "email": "person2@example.com",
        "date": datetime.now(),
        "valor": 100.50,
        "product": "Product 2",
        "quantity": 1,
        "category": "category not exist"
    }