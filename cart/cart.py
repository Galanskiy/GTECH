from store.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        # Get request assign to variable
        self.request = request
        # Get current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, create new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all website pages
        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Cart persistence
        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get current user profile and field
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convertaition of cart order dict to json str
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save converted str to profile model
            current_user.update(old_cart=carty)

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Cart persistence
        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get current user profile and field
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convertaition of cart order dict to json str
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save converted str to profile model
            current_user.update(old_cart=carty)


    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids    to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)
        # Return those looked up products
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id =str(product)
        product_qty = int(quantity)

        # Get cart
        ourcart =self.cart
        #Update dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get current user profile and field
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convertaition of cart order dict to json str
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save converted str to profile model
            current_user.update(old_cart=carty)

        return thing

    def delete(self, product):
        product_id = str(product)
        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get current user profile and field
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convertaition of cart order dict to json str
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save converted str to profile model
            current_user.update(old_cart=carty)

    def cart_total(self):
        # Get products ids
        product_ids = self.cart.keys()
        # Lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        # Counter
        total = 0
        for key, value in quantities.items():
            # Convert key string
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total