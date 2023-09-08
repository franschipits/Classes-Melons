"""Classes for melon orders."""


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    # order_type = None
    # tax = 0
    def __init__ (self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        # self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas melons":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total +=  3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    def __init__ (self,species,qty,passed_inspection = False):
        self.passed_inspection = passed_inspection
        super().__init__(species,qty)

    def mark_inspection(self, passed):
        self.passed_inspection = passed # order0 = GovernmentMelonOrder('Christmas', 10)
                                        # order0.mark_inspection(True)

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    #     # self.order_type = "domestic"
    #     # self.tax = 0.08
    #     # super().__init__(species,qty)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        # self.order_type = "international"
        # self.tax = 0.17
        self.country_code = country_code
        super().__init__(species, qty)



    def get_country_code(self):
        """Return the country code."""

        return self.country_code

