from .cart import Cart

# Create context processor so cart work on all website pages
def cart(reqest):
    # Return the default data from our cart
    return {'cart': Cart(reqest)}