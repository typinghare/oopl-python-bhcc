"""Shape, Rectangle, Circle, and Canvas."""

import xml


class Shape:
    """Abstract shape."""

    def draw(self):
        """Draw this shape."""
        pass


class Rectangle(Shape):
    def __init__(self, x, y, width, height, stroke_color="blue", fill_color="blue"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.stroke_color = stroke_color
        self.fill_color = fill_color

    def draw(self):
        """Returns an element string of this rectangle."""
        return xml.element(
            "rect",
            {
                "x": self.x,
                "y": self.y,
                "width": self.width,
                "height": self.height,
                "style": f"fill:{self.fill_color};stroke:{self.stroke_color};",
            },
        )


class Circle(Shape):
    def __init__(
        self, cx, cy, radius, stroke_color="blue", fill_color="blue", stroke_width=2
    ):
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.stroke_color = stroke_color
        self.fill_color = fill_color
        self.stroke_width = stroke_width

    def draw(self):
        """Returns an element string of this circle."""
        return xml.element(
            "circle",
            {
                "cx": self.cx,
                "cy": self.cy,
                "r": self.radius,
                "stroke": self.stroke_color,
                "stroke-width": self.stroke_width,
                "fill": self.fill_color,
            },
        )


class Canvas:
    """Canvas."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shape_list = []

    def add_shape(self, shape):
        """Adds a shape."""
        self.shape_list.append(shape)

    def draw(self):
        """Print a svg element based on the width and height."""

        element_list = []
        for shape in self.shape_list:
            element_list.append(shape.draw())

        svg_element = xml.element(
            "svg",
            {
                "version": "1.0",
                "xmlns": "http://www.w3.org/2000/svg",
                "width": self.width,
                "height": self.height,
            },
            f"\n{' '* 4}".join(element_list) + "\n",
        )

        print(svg_element)
