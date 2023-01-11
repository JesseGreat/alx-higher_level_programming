#!/usr/bin/python3
"""
Module that contains a an empty function
"""


class BaseGeometry(object):
    """ Empty class """
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
