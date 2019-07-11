# All Three Combined


class Parent(object):

    def implicit(self):
        print "Parent implicit()"

    def override(self):
        print "Parent override()"

    def altered(self):
        print "Parent altered()"


class Child(Parent):

    def override(self):
        print "Child override()"

    def altered(self):
        print "Child, Before Parent altered()"
        super(Child, self).altered()
        print "Child, After Parent altered()"


class BadStuff(Parent):

    def altered(self):
        print "BadStuff, Before Parent altered()"
        super(BadStuff, self).altered()
        print "BadStuff, After Parent altered()"

    def override(self):
        print "BadStuff override()"


class SuperFun(Child, BadStuff):
    pass


s = SuperFun()

print "\n"
s.altered()
print "\n"
s.override()
print "\n"
s.implicit()
