#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring"""
from unittest import TestCase
from numpy.testing import assert_almost_equal, assert_equal

from python_geometry.polygon_utilities import area_of_polygon_2D


class TestArea_of_polygon2D(TestCase):
    def test_quads(self):
        quad1 = ([0, 0], [1, 0], [1, 1], [0, 1])
        quad2 = ([0, 0], [0, 1], [1, 1], [1, 0])
        assert_equal(area_of_polygon_2D(quad1), 1)
        assert_equal(area_of_polygon_2D(quad2), -1)

    def test_triangles(self):
        tria1 = ([0, 0], [1, 0], [1, 1])
        tria2 = ([0, 0], [1, 1], [1, 0])
        assert_equal(area_of_polygon_2D(tria1), 0.5)
        assert_equal(area_of_polygon_2D(tria2), -0.5)
