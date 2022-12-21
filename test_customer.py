"""Used to test the dessert.py classes, how to run pytest: python -m pytest test_customer.py"""
import pytest
import dessert as d

def test_customer_create():
    """Tests creating a customer and changing the default inputs"""
    customer = d.Customer("Dr.Evil", 1313, 3131)
    assert customer.customer_name == "Dr.Evil"
    assert customer.customer_id == 1313
    assert customer.next_customer_id == 3131
    return customer
