"""Definitions of some standard shapes and helper routines."""

def cube_rotated(length=1.4142135623730951, origin=(0, 0, 0), h=0.1):
    """
    Return a cube rotated by -pi/2 mesh.

    Parameters
    ----------
    length : float
        Side length of the cube_rotated.
    origin : tuple
        Coordinates of the origin (bottom left corner)
    h : float
        Element size.

    """
    cube_rotated_stub = """
    Point(1) = {orig0,orig1,orig2,cl};
    Point(2) = {orig0+l/1.4142135623730951,orig1+l/1.4142135623730951,orig2,cl};
    Point(3) = {orig0,orig1+l*1.4142135623730951,orig2,cl};
    Point(4) = {orig0-l/1.4142135623730951,orig1+l/1.4142135623730951,orig2,cl};
    Point(5) = {orig0,orig1,orig2+l,cl};
    Point(6) = {orig0+l/1.4142135623730951,orig1+l/1.4142135623730951,orig2+l,cl};
    Point(7) = {orig0,orig1+l*1.4142135623730951,orig2+l,cl};
    Point(8) = {orig0-l/1.4142135623730951,orig1+l/1.4142135623730951,orig2+l,cl};

    Line(1) = {1,2};
    Line(2) = {2,3};
    Line(3) = {3,4};
    Line(4) = {4,1};
    Line(5) = {1,5};
    Line(6) = {2,6};
    Line(7) = {3,7};
    Line(8) = {4,8};
    Line(9) = {5,6};
    Line(10) = {6,7};
    Line(11) = {7,8};
    Line(12) = {8,5};

    Line Loop(1) = {-1,-4,-3,-2};
    Line Loop(2) = {1,6,-9,-5};
    Line Loop(3) = {2,7,-10,-6};
    Line Loop(4) = {3,8,-11,-7};
    Line Loop(5) = {4,5,-12,-8};
    Line Loop(6) = {9,10,11,12};

    Plane Surface(1) = {1};
    Plane Surface(2) = {2};
    Plane Surface(3) = {3};
    Plane Surface(4) = {4};
    Plane Surface(5) = {5};
    Plane Surface(6) = {6};

    Physical Surface(1) = {1};
    Physical Surface(2) = {2};
    Physical Surface(3) = {3};
    Physical Surface(4) = {4};
    Physical Surface(5) = {5};
    Physical Surface(6) = {6};

    Surface Loop (1) = {1,2,3,4,5,6};

    Volume (1) = {1};

    Mesh.Algorithm = 6;
    """

    cube_rotated_geometry = (
        "l = " + str(length) + ";\n" +
        "orig0 = " + str(origin[0]) + ";\n" +
        "orig1 = " + str(origin[1]) + ";\n" +
        "orig2 = " + str(origin[2]) + ";\n" +
        "cl = " + str(h) + ";\n" + cube_rotated_stub)

    return __generate_grid_from_geo_string(cube_rotated_geometry)

def cube_shifted(length=1, origin=(0, 0, 0), h=0.1):
    """
    Return a cube_shifted by 15 degrees  mesh.

    Parameters
    ----------
    length : float
        Side length of the cube.
    origin : tuple
        Coordinates of the origin (bottom left corner)
    h : float
        Element size.

    """
    cube_shifted_stub = """
    Point(1) = {orig0,orig1,orig2,cl};
    Point(2) = {orig0+0.96592582628907*l,orig1-0.25881904510252*l,orig2,cl};
    Point(3) = {orig0+1.22474487139159*l,orig1+0.7071068118655*l,orig2,cl};
    Point(4) = {orig0+0.25881904510252*l,orig1+0.96592582628907*l,orig2,cl};
    Point(5) = {orig0,orig1,orig2+l,cl};
    Point(6) = {orig0+0.96592582628907*l,orig1-0.25881904510252*l,orig2+l,cl};
    Point(7) = {orig0+1.22474487139159*l,orig1+0.7071068118655*l,orig2+l,cl};
    Point(8) = {orig0+0.25881904510252*l,orig1+0.96592582628907*l,orig2+l,cl};

    Line(1) = {1,2};
    Line(2) = {2,3};
    Line(3) = {3,4};
    Line(4) = {4,1};
    Line(5) = {1,5};
    Line(6) = {2,6};
    Line(7) = {3,7};
    Line(8) = {4,8};
    Line(9) = {5,6};
    Line(10) = {6,7};
    Line(11) = {7,8};
    Line(12) = {8,5};

    Line Loop(1) = {-1,-4,-3,-2};
    Line Loop(2) = {1,6,-9,-5};
    Line Loop(3) = {2,7,-10,-6};
    Line Loop(4) = {3,8,-11,-7};
    Line Loop(5) = {4,5,-12,-8};
    Line Loop(6) = {9,10,11,12};

    Plane Surface(1) = {1};
    Plane Surface(2) = {2};
    Plane Surface(3) = {3};
    Plane Surface(4) = {4};
    Plane Surface(5) = {5};
    Plane Surface(6) = {6};

    Physical Surface(1) = {1};
    Physical Surface(2) = {2};
    Physical Surface(3) = {3};
    Physical Surface(4) = {4};
    Physical Surface(5) = {5};
    Physical Surface(6) = {6};

    Surface Loop (1) = {1,2,3,4,5,6};

    Volume (1) = {1};

    Mesh.Algorithm = 6;
    """

    cube_shifted_geometry = (
        "l = " + str(length) + ";\n" +
        "orig0 = " + str(origin[0]) + ";\n" +
        "orig1 = " + str(origin[1]) + ";\n" +
        "orig2 = " + str(origin[2]) + ";\n" +
        "cl = " + str(h) + ";\n" + cube_shifted_stub)

    return __generate_grid_from_geo_string(cube_shifted_geometry)


