class Gelateria:

    food_type = 'ice cream'

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self._flavours = list()
        self._price = 1.00
        self._order_number = 1


    def add_flavours(self, flavours):
        if type(flavours) == str:
            if flavours in self._flavours:
                print(f'Flavour "{flavours}" is already in the system.')
            else:
                self._flavours.append(flavours)
        elif type(flavours) == list:
            for flavour in flavours:
                if flavour in self._flavours:
                    print(f'Flavour "{flavour}" is already in the system.')
                else:
                    self._flavours.append(flavour)


    def _calculate_price(self, number_of_scoops: int):
        return number_of_scoops * self._price


    def take_order(self):
        order = dict()
        count_ice = 0
        price = 0
        print()
        print('-'*15)
        print(f'Order {self._order_number}')
        print('-'*15)
        print('Your order:')
        add_more = None

        while add_more != 'q':
            count_ice += 1
            flavours = input('Flavours separated by commas: * ').split(",")
            # print(flavours)
            for flav in flavours:
                flav_clean = flav.strip()
                if flav_clean not in self._flavours:
                    print(f'Sadly, flavour \'{flav}\' is not available.')
                    del flavours[flavours.index(flav)]
                    continue
            amounts = input('Amounts separated by commas: * ').split(",")
            order[count_ice] = {i: j for i, j in zip(flavours, amounts)}
            add_more = input('To add more, press enter. If you\'re finished, press \'q\'. ')

        for order_no, it in order.items():
            for k, v in it.items():
                price += self._calculate_price(float(v))

        print(f'Price: {price}0 €')
        print('Thank you for your order!')

        self._order_number += 1


    def __repr__(self):
        string = '\n'
        string += f'Welcome to the gelateria {self.name} from {self.location}!\n'
        string += f'We are happy to serve you. Our hand-made ice cream is made from an original family recipe.\n'
        string += 'We offer the following flavours of ice cream for you to enjoy: \n'
        if self._flavours:
            for flav in self._flavours:
                string += f'\t* {flav.capitalize()}\n'
        else:
            string += '\tUnfortunately, we have no flavours available.\n'
        string += 'We are happy to serve you!\n'
        return string

if __name__ == "__main__":
    i = Gelateria('hello', 'steienstreet')
    i.add_flavours(['sweet', 'sour', 'salt', 'plain'])
    print(i.__repr__())
    i.take_order()
