"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}

    for item in notes:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1

    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ru = dict(recipe_updates)
    
    return ideas | ru


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sort = dict(sorted(cart.items()))
    return sort

def send_to_store(cart, aisle_mapping):
    """Combine users order with aisle and refrigeration information."""

    fulfillment = {}

    for item, qty in cart.items():
        aisle, refrigerated = aisle_mapping[item]
        fulfillment[item] = [qty, aisle, refrigerated]

    # Test expects REVERSE alphabetical order
    return dict(sorted(fulfillment.items(), reverse=True))

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""

    for item, data in fulfillment_cart.items():
        ordered_qty = data[0]   # quantity ordered

        if item in store_inventory:
            # inventory format: [stock, aisle, refrigerated]
            stock = store_inventory[item][0]

            new_stock = stock - ordered_qty

            if new_stock <= 0:
                store_inventory[item][0] = 'Out of Stock'
            else:
                store_inventory[item][0] = new_stock

    return store_inventory

