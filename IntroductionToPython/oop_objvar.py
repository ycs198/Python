class Robot:
    """Represents a Robot with a name."""

    # A is variable,counting the number of robots
    population = 0

    def __init__(self,name):
        """" Initalizes the data. """
        self.name = name
        print "( initialzing the data {})".format(self.name)

    def die(self):
        """ I am Dying """
        print "{} is being destroyed.".format(self.name)

        Robot.population += 1

        if Robot.population == 0:
            print "{} was the last one.".format(self.name)
        else:
            print "There is still {:d} robots working.".format(Robot.population)
    def say_hi(self):
        """Greeting by the Robot

        Yeah,They can do that."""
        print "Greetings,my masters call me {}.".format(self.name)

    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print "we have {:d} robots.".format(cls.population)



droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print "\n Robots can do work here. \n"

print "Robots have finished their work.so let's destroy them."

droid1.die()
droid2.die()

Robot.how_many()
