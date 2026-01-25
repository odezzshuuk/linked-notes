# SVG

## What is SVG?

- stands for `Scalable vector Graphics`
- use [ XML ](xml.md) markup to describe the 2D graphics

## Feature

- resolution independent

## Create SVG

[Svg Create](svg-create.md)

## attribute of svg

- `width` and `height`: The dimensions of the SVG viewport. These attributes specify the size of the SVG in pixels, and can be set to absolute values (e.g. width="200") or relative values (e.g. width="50%").
- `viewBox`: Specifies the position and dimensions of the viewport within the SVG coordinate system. The value of the viewBox attribute is a list of four space-separated numbers: min-x, min-y, width, and height. For example, viewBox="0 0 100 100" would specify a viewport that covers the entire SVG canvas.
- `xmlns`: Specifies the XML namespace for the SVG document. This attribute is usually set to "http://www.w3.org/2000/svg".
- `fill` and `stroke`: Control the color of the fill and stroke of SVG shapes. value of these attributes can be a named color, a hex color code, an RGB color value, or a URL pointing to an external image.
- `style`: Allows you to apply CSS styles to the SVG elements.
- `id`: A unique identifier for the SVG element.
- `preserveAspectRatio`: Specifies how the SVG viewport should be scaled to fit the dimensions of its
- `version`: Specifies the version of SVG used in the document. The value of this attribute is typically "1.1" or "1.2".

## tag inside svg

- `<rect>`: Used to draw rectangles.
- `<circle>`: Used to draw circles.
- `<path>`: Used to define custom shapes and paths.
- `<line>`: Used to draw straight lines.
- `<polyline>`: Used to draw a series of connected straight lines.
- `<polygon>`: Used to draw a closed shape with three or more sides.
- `<text>`: Used to add text to an SVG.
- `<g>`: Used to group multiple SVG elements together.
- `<use>`: Used to reuse an SVG element from another location.
- `<defs>`: Used to define and store reusable SVG elements.
