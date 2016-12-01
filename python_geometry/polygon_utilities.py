#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring"""
import numpy as np


def area_of_polygon_2D(polygon, *args):
    """
    Computes the signed area of an arbitrary convex polygon as described in
    http://paulbourke.net/geometry/polygonmesh/.
    The signed area is positive for counter clockwise ordering otherwise
    negative.

    Parameters
    ----------
     polygon:
        np.ndarray, list
            The polygon as a list of consecutive 2D points.

    Returns
    -------
    float
        Area of the polygon. The area is negativ for clockwise point ordering
    """

    if args:
        poly = [polygon]

        for pt in args:
            if pt.shape != (2,):
                for sp in pt:
                    poly.append(sp)
            else:
                poly.append(pt)
        polygon = np.array(poly)

    area = 0.
    for i in range(len(polygon) - 1):
        area += (polygon[i][0] * polygon[i + 1][1]
                 - polygon[i + 1][0] * polygon[i][1])

    # close the loop with the last crossproduct
    area += (polygon[-1][0] * polygon[0][1] - polygon[-1][1] * polygon[0][0])

    area /= 2.
    if area == 0:
        raise ValueError('Calculated Area is 0!')
    return area
