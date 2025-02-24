class Product:
    """
    Класс с товаром
    """
    def __init__(self, id: int, name: str, price: float, quantity: int) -> None:
        """
        функция для инициализации класса товара
        :param id: идентификатор товара
        :param name: название товара
        :param price: цена товара
        :param quantity: количество товара
        :return: None
        """
        self.__id = id
        self.name = name
        self.__price = price
        self.__quantity = quantity

    def get_id(self) -> int:
        """
        возвращает идентификатор товара(геттер)
        :return: int
        """
        return self.__id

    def set_id(self, id: int) -> None:
        """
        добавляет id товару (сеттер)
        :return: None
        """
        self.__id = id

    def get_price(self) -> float:
        """
        возвращает price (геттер)
        :return: float
        """
        return self.__price

    def set_price(self, price: float) -> None:
        """
        устанавливает прайс (сеттер)
        :return: None
        """
        self.__price = price

    def get_quantity(self) -> int:
        """
        возвращает количество товара (геттер)
        :return: int
        """
        return self.__quantity

    def set_quantity(self, quantity: int) -> None:
        """
        устанавливает количество товара (сеттер)
        :return: None
        """
        self.__quantity = quantity

    def update_quantity(self, amount: int) -> None:
        """
        обновляет количество товара
        :param amount: новое количество
        :return: None
        """
        self.__quantity += amount

    def info(self) -> None:
        """
        выводит информацию о товаре
        :return: None
        """
        print(f"""
        ID продукта: {self.__id}
        Название продукта: {self.name}
        Цена продукта: {self.__price}
        Количество продукта: {self.__quantity}
        """)


class Store:
    """
    Класс для создания магазина
    """
    def __init__(self, name: str, products: list[Product], director: str) -> None:
        """
        инициализация магазина
        :param name: название магазина
        :param products: список товара
        :param director: имя директора
        :return: None
        """
        self.name = name
        self.products = products
        self.director = director

    def add_product(self, product: Product) -> None:
        """
        добавляет товар в магазин
        :param product: новый товар
        :return: None
        """
        self.products.append(product)

    def remove_product(self, product_id: int) -> None:
        """
        удаляет товар по идентификатору
        :param product_id: идентификатор товара
        :return: None
        """
        new_products = []
        for prod in self.products:
            if prod.__id != product_id:
                new_products.append(prod)
        self.products = new_products

    def get_product_by_id(self, id: int) -> Product | None:
        """
        поиск товара по идентификатору
        :param id: идентификатор товара
        :return: Product | None (если товар не найден)
        """
        for product in self.products:
            if product.__id == id:
                return product
        return None
    
    def show_products(self) -> None:
        """
        выводит информацию о товарах
        :return: None
        """
        if not self.products:
            print("Ничего нет")
            return
        for product in self.products:
            product.info()


class Customer:
    """
    Класс для создания покупателя
    """
    def __init__(self, name: str, balance: float) -> None:
        """
        инициализация покупателя
        :param name: имя покупателя
        :param balance: баланс покупателя
        :return: None
        """
        self.name = name
        self.cart = {}
        self.__balance = balance

    def get_balance(self) -> float:
        """
        возвращает бэленс покупателя(геттер)
        :return: float
        """
        return self.__balance

    def set_balance(self, balance: float) -> None:
        """
        устанавливает бэленс покупателю(сеттер)
        :return: None
        """
        self.__balance = balance

    def add_to_cart(self, product : Product, quantity: int) -> None:
        """
        добавляет товар в корзину
        :param product: товар который нужно добавить
        :param quantity: количество товара
        :return: None
        """
        if product.__quantity < quantity:
            print(f"Недостаточно товара: {product.name}")
            return -1
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    def remove_product_cart(self, product: Product) -> True | False:
        """
        удаляет товар из корзины
        :param product: товар который нужно удалить
        :return: True если успешно удалило | False если есть ошибки
        """
        if product in self.cart:
            del self.cart[product]
            print("Товар успешно удален")
            return True
        else:
            print("Ошибка")
            return False

    def view_cart(self) -> None:
        """
        выводит информацию о товарах в корзине, а также общую стоимость товара
        :return: None
        """
        if not self.cart:
            print("Ваша корзина пуста")
            return
        total = 0
        for product, quantity in self.cart.items():
            print(f"{product.name} - {quantity} шт. ({product.__price} за штуку)")
            total += product.__price * quantity 
        print(f"Общая стоимость: {total}")

    def checkout(self, store: Store) -> None:
        """
        функция для оплаты товара из корзины
        :param store: товары количество которых будет уменьшено после покупки
        :return: None
        """
        total = 0
        flag = False
        for product, quantity in self.cart.items():
            total += product.__price * quantity
            if store.get_product_by_id(product) < quantity:
                flag = True
        if self.__balance < total:
            print("Недостаточно средств")
            return -1
        if flag:
            print("Недостаточно товаров для совершения покупок")
            return -1
        for product, quantity in self.cart.items():
            product.update_quantity(-quantity)
        self.__balance -= total
        self.cart.clear()
        print("Вы оплатили покупки")


class DiscountedProduct(Product):
    """
    Класс для установления скидок на товары, наследуется от класса Product
    """
    def __init__(self, id: int, name: str, price: float, quantity: int, discount: float) -> None:
        """
        инициализация товаров со скидкой
        :param id: идентификатор товара
        :param name: название товара
        :param price: цена товара
        :param quantity: количество товара
        :param discount: скидка на товар в процентах
        :return: None
        """
        super().__init__(id, name, price, quantity)
        self.discount = discount

    def info(self) -> None:
        """
        выводит информацию о товаре по скидке
        :return: None
        """
        print(f"""
        ID продукта: {self.__id}
        Название продукта: {self.name}
        Цена продукта со скидкой: {self.__price * (1 - self.discount / 100)}
        Количество продукта: {self.__quantity}
        """)

product1 = Product(1, "Tesla", 60000, 5)
product2 = Product(2, "RTX 5090", 2000, 50)
product3 = Product(3, "iphone 16", 800, 76)
new_product = Product(4, "finalmouse ulx", 180, 1000)
store = Store("Барахолка", [product1, product2, product3], "Ryan Gosling")
store.add_product(new_product)
store.remove_product(1)
product = store.get_product_by_id(3)
product.info()
store.show_products()
customer = Customer("Keanu", 3000)
customer.add_to_cart(product3, 1)
customer.view_cart()
discounted_product = DiscountedProduct(5, "Восстановленный Iphone", 700, 1, 30)
discounted_product.info()