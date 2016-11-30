#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring"""
from unittest import TestCase
from numpy.testing import assert_almost_equal, assert_equal

from python_geometry.polygon_utilities import area_of_polygon_2D


class TestArea_of_polygon2D(TestCase):
    def test_rectangles(self):
        ## square
        quad1 = ([0, 0], [1, 0], [1, 1], [0, 1])
        quad2 = ([0, 0], [0, 1], [1, 1], [1, 0])
        assert_equal(area_of_polygon_2D(quad1), 1)
        assert_equal(area_of_polygon_2D(quad2), -1)

        # rectangles
        quad3 = ([0, 0], [5, 0], [5, 1], [0, 1])
        assert_equal(area_of_polygon_2D(quad3), 5)

    def test_triangles(self):
        tria1 = ([0, 0], [1, 0], [1, 1])
        tria2 = ([0, 0], [1, 1], [1, 0])
        tria3 = ([0, 0], [5, 10], [2, 5])
        assert_equal(area_of_polygon_2D(tria1), 0.5)
        assert_equal(area_of_polygon_2D(tria2), -0.5)
        assert_equal(area_of_polygon_2D(tria3), 2.5)
