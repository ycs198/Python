import random

class Coin(object):

    def __init__(self,rare=False,clean = True,heads = True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

        self.colour = "Gold"
        self.num_edges = 1
        self.diameter = 22.5
        self.thickness = 3.15
        self.heads = True


    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def filp(self):
        head_options= [True,False]
        choice = random.choice(head_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "${} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))

class Onepound(Coin):
    def __init__(self):
        data = {
            "original_value" : 1.00,
            "clean_colour": "gold",
            "rusty_colour": "Greenish",
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5,
        }
        super(Onepound,self).__init__(**data)



class Onepence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges":1,
            "diameter":20.3,
            "thickness":1.52,
            "mass":3.56,
        }
        super(Onepence,self).__init__(**data)



class Twopence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges":1,
            "diameter":25.9,
            "thickness":1.85,
            "mass":7.12,
        }
        super(Twopence,self).__init__(**data)



class Fivepence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges":1,
            "diameter":18.0,
            "thickness":1.77,
            "mass":3.25,
        }
        super(Fivepence,self).__init__(**data)

    def rust(self):
        self.colour = self.clean_colour


class Tenpence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges":1,
            "diameter":24.5,
            "thickness":1.85,
            "mass":6.50,
        }
        super(Tenpence,self).__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

class Twentypence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges":7,
            "diameter":21.4,
            "thickness":1.7,
            "mass":5.00,
        }
        super(Twentypence,self).__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

class Fiftypence(Coin):
    def __init__(self):
        data = {
            "original_value" : 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges":7,
            "diameter":27.3,
            "thickness":1.78,
            "mass":8.00,
        }
        super(Fiftypence,self).__init__(**data)

    def rust(self):
        self.colour = self.clean_colour


class Twopound(Coin):
    def __init__(self):
        data = {
            "original_value" : 2.00,
            "clean_colour": "gold & silver",
            "rusty_colour": "Greenish",
            "num_edges":1,
            "diameter":28.4,
            "thickness":2.50,
            "mass":12.00,
        }
        super(Twopound,self).__init__(**data)

coins = [Onepence(),Twopence(),Fivepence(),Tenpence(),Twentypence(),Fiftypence(),Onepound(),Twopound()]

for coin in coins:
    arguments = [coin,coin.colour,coin.value,coin.diameter,coin.thickness,coin.num_edges,coin.mass]

    string = "{} -colour:{},value:{},diameter:{},thickness:{},num_edges:{},mass:{}".format(*arguments)
    print string
