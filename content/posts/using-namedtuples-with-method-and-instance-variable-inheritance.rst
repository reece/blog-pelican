Using namedtuples with method and instance variable inheritance
###############################################################
:date: 2013-06-02 16:23
:author: reece
:slug: using-namedtuples-with-method-and-instance-variable-inheritance
:status: published

Python's namedtuple class provides a simple, lightweight way to make
simple immutable classes. If you're using dictionaries to pass objects
around, consider using namedtuples instead: they're easier to read and
provide the benefits of classes such as methods and properties. With
namedtuples, you'll have cleaner code with essentially no additional
work.

The `Python namedtuple
docs <http://docs.python.org/2/library/collections.html#collections.namedtuple>`__ include
examples for Point and Point3D. Point3D inherits the instance variables
("fields" in namedtuples), but not the methods of the Point class.
What's not discussed in the documentation is how to inherit methods
**and** fields when using namedtuples, and that's the subject of this
post.

| Let's start with the examples from the docs. The first example is:
| [python]
| Point = collections.namedtuple('Point', ['x', 'y'])
| p = Point(5,6)
| [/python]

This is quite useful in itself because it allows us to access p.x and
p.y as properties, which many find to be preferable to p['x'] or p['y']
with a dict-based structure.

But Points often need to be manipulated, and object-oriented programmers
often prefer to put the code for such manipulations with the class than
as standalone functions. With namedtuples, that might look like this
(again, from the docs):

| [python]
| class Point(namedtuple('Point', 'x y')):
| \_\_slots\_\_ = ()
| @property
| def hypot(self):
| return (self.x \*\* 2 + self.y \*\* 2) \*\* 0.5
| def \_\_str\_\_(self):
| return 'Point: x=%6.3f y=%6.3f hypot=%6.3f' % (self.x, self.y,
  self.hypot)
| [/python]

Great, we now have methods associated with the class.

The docs go on to define Point3D with an additional dimension:

| [python]
| Point3D = namedtuple('Point3D', Point.\_fields + ('z',))
| [/python]

Although Point3D "inherits" fields from Point, it doesn't inherit any
methods. In fact, Point3D isn't a subclass of Point at all. In the
example above, we merely copied one aspect of the definition of Point to
make Point3D. So, if there were methods in Point, they would not be
available to Point3D. In the real world, method inheritance is useful
for abstraction and code maintenance.

Like all classes, classes derived from namedtuples may be subclassed and
their methods overridden. Consider an imaginary number class like this
that formats imaginary numbers in typical a + bi notation.

| [python]
| class Point\_img(Point):
| def \_\_str\_\_(self):
| return 'Point: %6.3f+%6.3fi' % (self.x, self.y)
| [/python]

So, it's now time to combine class inheritance and extending a
namedtuple's fields. Let's define a new Point2D and Point3D classes like
this:

| [python]
| from collections import namedtuple
| class Point2D(namedtuple('Point', ['x', 'y'])):
| @property
| def length(self):
| return sum([ d\*\*2 for d in self ]) \*\* 0.5
| def \_\_add\_\_(self,other):
| assert self.\_\_class\_\_ == other.\_\_class\_\_, "may only add
  instances of same class"
| return self.\_\_class\_\_.\_\_new\_\_(self.\_\_class\_\_,\*[ d1+d2 for
  d1,d2 in zip(self,other) ])
| def \_\_str\_\_(self):
| return '%s: <%s>; length=%6.3f' % (
| self.\_\_class\_\_.\_\_name\_\_,
| ','.join([ '%s=%6.3f' % (d,v)
| for d,v in zip(self.\_fields,self) ]),
| self.length)
| class Point3D(namedtuple('Point3D', Point2D.\_fields + ('z',)),
  Point2D):
| pass
| [/python]

Notice that Point3D is derived from two classes: a namedtuple-based
class defined by adding to \_fields, and the Point2D class which defined
methods (and was itself derived from a namedtuple). This isn't rocket
science, but it's a obscure and potentially very useful to others.

With these definitions, we may now define 2D and 3D points. Notice that
Point3D inherits the addition and string representation methods of
Point2D.

| [python]
| In [21]: print Point2D(3,4)
| Point2D: <x= 3.000,y= 4.000>; length= 5.000

| In [22]: print Point2D(3,4) + Point2D(5,6)
| Point2D: <x= 8.000,y=10.000>; length=12.806

| In [23]: print Point3D(3,4,5)
| Point3D: <x= 3.000,y= 4.000,z= 5.000>; length= 7.071

| In [24]: print Point3D(3,4,5) + Point3D(1,2,3)
| Point3D: <x= 4.000,y= 6.000,z= 8.000>; length=10.770
| [/python]

Finally, it's worth noting that designing the notion that Point3D is-a
Point2D is dubious. If I were going to implement this, I'd probably
start with a generic n-dimensional point that had the methods described
above, and then subclass special cases like Point2D and Point3D as
needed.
