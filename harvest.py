############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        


def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon = MelonType('musk', 1998, 'green', True, True )
    muskmelon.add_pairing(['mint'])


    casaba = MelonType('cas', 2003, 'orange', False, None )
    casaba.add_pairing(["strawberries", "mint"])

    crenshaw = MelonType('cren', 1996, 'green', False, None)
    crenshaw.add_pairing(['proscuitoo'])

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True)
    yellow_watermelon.add_pairing(['ice cream'])



    all_melon_types = [muskmelon, casa, crenshaw, yellow_watermelon]

    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in melon_types:
        print('{} pairs with '.format(melon_type))
        for pairing in melon_type.pairings:
            print('- {}'.format(pairing))

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}
    for melon_type in melon_types:
        melon_dict[melon_type.code] = melon_type

    return melon_dict

############
# Part 2   #
############

class Melon(object):

    def __init__(self, melon_type, shape_rating, color_rating, field_num, name):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_num = field_num
        self.name = name

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5:
            return True
        return False


    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons():
    
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



