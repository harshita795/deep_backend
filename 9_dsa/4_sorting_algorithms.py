# Sorting Algorithms

class Product:
    def __init__(self, name: str, rating: float):
        self.name = name
        self.rating = rating

    def __repr__(self) -> str:
        return f"{self.name}: {self.rating}"


def get_rating(product: Product) -> float:
    return product.rating


def sort_products(products: list[Product]) -> list[Product]:
    return sorted(products, key=get_rating)


products = [
    Product("Laptop", 4.5),
    Product("Keyboard", 3.8),
    Product("Mouse", 4.2)
]

print(sort_products(products))
