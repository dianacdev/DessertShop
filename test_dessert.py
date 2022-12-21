"""Used to test the dessert.py classes, how to run pytest: python -m pytest test_dessert.py"""
import pytest
import dessert as d
from packaging import Packaging
from dessert import Order as o


@pytest.fixture
def test_cookie():
    """Tests that the Cookie Name is correct"""
    cookie = d.Cookie("Chocolate Chip M&M")
    assert cookie.name == "Chocolate Chip M&M"
    assert cookie.cookie_quantity == 12
    assert cookie.price_per_dozen == 5.00
    assert cookie.packaging == "Box"
    return cookie


@pytest.fixture
def test_candy():
    """Tests that the Sundae is created correctly"""
    candy = d.Candy("Chocolate Beans")
    assert candy.name == "Chocolate Beans"
    assert candy.candy_weight == 1
    assert candy.price_per_pound == 1.0
    assert candy.packaging == "Bag"
    return candy


@pytest.fixture
def test_ice_cream():
    """Tests that the Sundae is created correctly"""
    ice_cream = d.IceCream("Vanilla Bean")
    assert ice_cream.name == "Vanilla Bean"
    assert ice_cream.scoop_count == 1
    assert ice_cream.price_per_scoop == 1.5
    assert ice_cream.packaging == "Bowl"
    return ice_cream


@pytest.fixture
def test_sundae():
    """Tests that the Sundae is created correctly"""
    sundae = d.Sundae("Sprinkles")
    assert sundae.name == "Sprinkles"
    assert sundae.topping_name == "Sprinkles"
    assert sundae.topping_price == 0.50
    assert sundae.scoop_count == 2
    assert sundae.price_per_scoop == 0.50
    assert sundae.packaging == "Boat"
    return sundae


def test_cookie_modified():
    """Tests that the Cookie is created correctly once modified"""
    cookie = d.Cookie("Chocolate Chip", 5, 10.00)
    cookie.packaging = "Bag"
    assert cookie.name == "Chocolate Chip"
    assert cookie.cookie_quantity == 5
    assert cookie.price_per_dozen == 10.00
    assert cookie.packaging == "Bag"


def test_candy_modified():
    """Tests that the Candy is created correctly once modified"""
    candy = d.Candy("Jelly Beans", 1.5, 1.0)
    candy.packaging = "Box"
    assert candy.name == "Jelly Beans"
    assert candy.candy_weight == 1.5
    assert candy.price_per_pound == 1.0
    assert candy.packaging == "Box"



def test_ice_cream_modified():
    """Tests that the IceCream is created correctly once modified"""
    ice_cream = d.IceCream("Vanilla", 2, 0.5)
    ice_cream.packaging = "Boat"
    assert ice_cream.name == "Vanilla"
    assert ice_cream.scoop_count == 2
    assert ice_cream.price_per_scoop == 0.5
    assert ice_cream.packaging == "Boat"

def test_sundae_modified():
    """Tests that the Sundae is created correctly once modified"""
    sundae = d.Sundae("Vanilla", 3, 0.5, "Hot Fudge", 0.5)
    sundae.packaging ="Bowl"
    assert sundae.name == "Hot Fudge Vanilla Sundae"
    assert sundae.topping_name == "Hot Fudge"
    assert sundae.topping_price == 0.5
    assert sundae.scoop_count == 3
    assert sundae.price_per_scoop == 0.5
    assert sundae.packaging == "Bowl"

def test_candy_cost_calculate():
    """Test candy calculate_cost() and calculate_tax()"""
    candy_calc = d.Candy("Candy Corn", 1.5, .25)
    assert candy_calc.calculate_cost() == 0.375
    assert candy_calc.calculate_tax() == 0.027187499999999996

def test_cookie_calculate():
    """Test cookie calculate_cost() and calculate_tax()"""
    cookie_calc = d.Cookie("Double Fudge", 48,10)
    assert cookie_calc.calculate_cost() == 40
    assert cookie_calc.calculate_tax() == 2.9

def test_ice_cream_calculate():
    """Test ice cream calculate_cost() and calculate_tax()"""
    ice_cream_calc = d.IceCream("Amaretto", 5, 2.05)
    assert ice_cream_calc.calculate_cost() == 10.25
    assert ice_cream_calc.calculate_tax() == 0.7431249999999999

def test_sundae_calculate():
    """Test sundae calculate_cost() and calculate_tax()"""
    sundae_calc = d.Sundae("Bubble Gum", 3, 1.25)
    assert sundae_calc.calculate_cost() == 4.25
    assert sundae_calc.calculate_tax() == 0.308125

def test_tax_percent_modified():
    """Test modified tax"""
    dessert = d.Candy("Candy Corn", 1.5, .25)
    dessert.tax_percent = 15.25
    assert dessert.calculate_cost() == 0.375
    assert dessert.calculate_tax() == 0.0571875

def test_packaging_subclass():
    """Used to test if a class is a subclass of Packaging all should equal false because Packaging is an interface"""
    assert issubclass(d.Candy, Packaging) is False
    assert issubclass(d.Cookie, Packaging) is False
    assert issubclass(d.IceCream, Packaging) is False
    assert issubclass(d.Sundae, Packaging) is False
    assert issubclass(d.DessertItem, Packaging) is False

def test_order_default():
    """Tests Payment"""
    assert o.pay_method.name == "CASH"

def test_order_modified():
    """Tests Payment"""
    o.pay_method =  o.PayType.CARD
    assert o.pay_method.name == "CARD"

def test_cookie_is_same():
    """Testing Combining of Like Terms for Cookie"""
    cookie_01= d.Cookie("Candy Corn Cookie",12,2.25)
    cookie_02 = d.Cookie("Candy Corn Cookie",12,2.25)
    assert d.Cookie.is_same_as(cookie_01, cookie_02) is True

def test_cookie_is_not_same():
    """Testing Combining of Like Terms for Cookie"""
    cookie_01 = d.Cookie("Candy Corn Cookie",12,2.25)
    cookie_02 = d.Cookie("Candy Corn Cookie",6,.25)
    assert d.Cookie.is_same_as(cookie_01, cookie_02) is not True

def test_candy_is_same():
    """Testing Combining of Like Terms for Candy"""
    candy_01 = d.Candy("Candy Corn",1.5,.25)
    candy_02 = d.Candy("Candy Corn",1.5,.25)
    assert d.Candy.is_same_as(candy_01, candy_02) is True

def test_candy_is_not_same():
    """Testing Combining of Like Terms for Candy"""
    candy_01 = d.Candy("Candy Corn",5.5,.225)
    candy_02 = d.Candy("Candy Corn",1.5,.25)
    assert d.Candy.is_same_as(candy_01, candy_02) is not True
