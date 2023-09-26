import re
import sys
import xml.etree.ElementTree as ET


def main(source_xml_path):
    """Convert an Adobe XML discrete color map to QGIS color map file.

    This script requires that the Adobe color map have exactly this structure:

        <palette>
            <color name='...' r='...' g='...' b='...'/>
            ...
        </palette>

    Other attributes to ``color`` are allowed but not used.

    The ``name`` attribute of ``color`` must end in an integer.  This integer
    is interpreted as the lulc class.

    Output is printed to stdout.
    """
    tree = ET.parse(source_xml_path)
    palette = tree.getroot()

    print("INTERPOLATION:EXACT")  # indicate this is a discrete color map
    for color in palette:
        name = color.attrib['name']
        lucode = re.findall('[0-9]+$', name)[0]
        r = color.attrib['r']
        g = color.attrib['g']
        b = color.attrib['b']
        alpha = 255  # assume full opacity

        print(f"{lucode},{r},{g},{b},{alpha},{name}")


if __name__ == '__main__':
    main(sys.argv[1])
