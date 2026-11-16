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

#! Bubble Sort: Sorts a list by repeatedly comparing and swapping adjacent elements.

def bubble_sort(delivery_times: list[int]) -> list[int]:
    if not delivery_times:
        return []

    end = len(delivery_times)

    while end > 1:
        swapped = False

        for i in range(1, end):
            # Compare adjacent values and swap them if they are out of order.
            if delivery_times[i - 1] > delivery_times[i]:
                delivery_times[i - 1], delivery_times[i] = (
                    delivery_times[i],
                    delivery_times[i - 1]
                )
                swapped = True

        if not swapped:
            break

        end -= 1

    return delivery_times


times = [45, 20, 60, 15, 35]
print(bubble_sort(times))