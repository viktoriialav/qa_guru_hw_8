"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity * 0.5) is True
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity * 2) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(product.quantity * 0.5)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        pytest.raises(ValueError, product.buy, product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product):
        buy_count = product.quantity // 10

        cart.add_product(product)
        assert cart.products[product] == 1

        cart.add_product(product, buy_count)
        assert cart.products[product] == buy_count + 1

    def test_cart_remove_product_from_empty_cart(self, cart, product):
        remove_count = product.quantity // 10

        # remove_count = None
        cart.remove_product(product)
        assert product not in cart.products

        # remove_count is defined
        cart.remove_product(product, remove_count=remove_count)
        assert product not in cart.products

    def test_cart_remove_product_from_non_empty_cart(self, cart, product):
        buy_count = remove_count = product.quantity // 10

        # remove_count = None
        cart.add_product(product, buy_count)
        cart.remove_product(product)
        assert product not in cart.products

        # remove_count is more than current count (cart.products[product])
        cart.add_product(product, buy_count)
        cart.remove_product(product, remove_count=remove_count * 2)
        assert product not in cart.products

        # remove_count is less than current count (cart.products[product])
        cart.add_product(product, buy_count)
        cart.remove_product(product, remove_count=remove_count // 2)
        assert cart.products[product] == buy_count - remove_count // 2

    def test_cart_clear(self, cart):
        cart.clear_cart()
        assert cart.products == {}

    def test_cart_get_total_price(self, cart, product):
        buy_count = product.quantity // 10

        # the cart is empty
        assert cart.get_total_price() == 0

        # the cart isn't empty
        cart.add_product(product, buy_count)
        assert cart.get_total_price() == product.price * buy_count

    def test_cart_buy(self, cart, product):
        initial_product_quantity = product.quantity
        buy_count = initial_product_quantity // 10

        cart.add_product(product, buy_count)
        cart.buy()
        assert cart.products == {} and product.quantity == initial_product_quantity - buy_count

    def test_cart_buy_more_than_available(self, cart, product):
        buy_count = product.quantity * 2

        cart.add_product(product, buy_count)
        pytest.raises(ValueError, cart.buy)
