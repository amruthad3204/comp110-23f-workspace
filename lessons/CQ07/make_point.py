"""Importing the Point class and creating a new point."""

from lessons.CQ07.point import Point

my_point: Point = Point(3.0, 5.0)

my_point.scale_by(4)

your_point = my_point.scale(2)