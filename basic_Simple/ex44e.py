# Composition


class Parent(object):

    def implicit(self):
        print "Parent implicit()"

    def override(self):
        print "Parent override()"

    def altered(self):
        print "Parent altered()"


class Child(object):
    def __init__(self):
        self.parent = Parent()

    def implicit(self):
        self.parent.implicit()

    def override(self):
        print "Child override()"

    def altered(self):
        print "Child, Before Parent altered()"
        self.parent.altered()
        print "Child, After Parent altered()"


son = Child()
son.implicit()

print "\n"
son.override()

print "\n"
son.altered()
