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


dad = Parent()
son = Child()

print "\nimplicit()"
dad.altered()
son.implicit()
print "\noverride"
dad.override()
son.override()
print "\naltered()"
dad.altered()
son.altered()
