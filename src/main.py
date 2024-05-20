from db_operations import (
    add_category, update_category, delete_category, find_categories,
    add_product, update_product, delete_product, find_products
)

def print_categories(categories):
    for category in categories:
        print(f"ID: {category[0]}, Name: {category[1]}")

def print_products(products):
    for product in products:
        print(f"ID: {product[0]}, Name: {product[2]}, Category ID: {product[1]}, Price: {product[3]}, Quantity: {product[4]}")

if __name__ == "__main__":
    add_category('Fruits')
    add_category('Vegetables')

    add_product('Apple', 1, 0.5, 100)
    add_product('Carrot', 2, 0.2, 200)

    categories = find_categories('Fruit')
    print("Categories found:")
    print_categories(categories)

    products = find_products('Apple')
    print("Products found:")
    print_products(products)

    update_category(1, 'Fresh Fruits')

    update_product(1, price=0.6)

    delete_product(2)

    delete_category(2)

    categories = find_categories('Fresh')
    print("Categories found after update:")
    print_categories(categories)

    products = find_products('Apple')
    print("Products found after update:")
    print_products(products)
