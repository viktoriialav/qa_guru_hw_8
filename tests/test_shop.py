"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests.models import Product


@pytest.fixture
def products():
    products = [
        Product("book", 100, "This is a book", 1000),
        Product("backpack", 1000, "This is a backpack", 200),
        Product("pen", 20, "This is a pen", 2000),
        Product("pencil", 10, "This is a pencil", 4000),
        Product("pencil case", 200, "This is a pencil case", 500)
    ]
    return products


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, products):
        # TODO напишите проверки на метод check_quantity
        for product in products:
            assert product.check_quantity(product.quantity * 0.5) is True

        for product in products:
            assert product.check_quantity(product.quantity) is True

        for product in products:
            assert product.check_quantity(product.quantity * 2) is False

    def test_product_buy(self, products):
        # TODO напишите проверки на метод buy
        for product in products:
            product.buy(product.quantity * 0.5)

    def test_product_buy_more_than_available(self, products):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        for product in products:
            try:
                product.buy(product.quantity + 1)
            except ValueError:
                pass



class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

