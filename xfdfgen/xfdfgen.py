import os
import xml.dom.minidom
from typing import Dict


def xfdfgen(name: str, field_dictionary: Dict[str, str]) -> xml.dom.minidom.Document:
    """
    Generates an xml.dom.minidom xml document in xfdf format given a pdf containing form fields
    and a dictionary containing the fields

    Args:
        name (str): path to the pdf document
        field_dictionary (Dict[str, str]): a dictionary with form field id as key and their values as value

    Returns: an xml.dom.minidom.Document in xfdf format

    """
    xfdf = xml.dom.minidom.Document()

    # xfdf peculiarities   #############################################################################################
    # see https://docs.aspose.com/display/pdfnet/Whats+the+Difference+Between+XML%2C+FDF+and+XFDF

    top = xfdf.createElement("xfdf")
    top.setAttribute("xmlns", "http://ns.adobe.com/xfdf/")
    top.setAttribute("xml:space", "preserve")
    xfdf.appendChild(top)

    f = xfdf.createElement("f")
    f.setAttribute("href", name)
    top.appendChild(f)

    # insert fields from field dictionary   ############################################################################
    fields = xfdf.createElement("fields")
    for field_name, field_value in field_dictionary.items():
        field = xfdf.createElement("field")
        field.setAttribute("name", field_name)
        fields.appendChild(field)

        value = xfdf.createElement("value")
        field.appendChild(value)

        text1 = xfdf.createTextNode(field_value)
        value.appendChild(text1)
    top.appendChild(fields)

    return xfdf


class Xfdf:
    def __init__(self, name: str, field_dictionary: Dict[str, str]):
        """
        Initializes an xfdf form xml.
        Use .write_xfdf() to write to a file
        Use .get_xfdf to return the raw xfdf string
        Use .pretty_print to pretty print the xfdf file to console

        Args:
            name (str): path to the pdf document
            field_dictionary (Dict[str, str]): a dictionary with form field id as key and their values as value
        """
        # Sanity checks
        if not name.endswith(".pdf"):
            raise ValueError("The document name must end with .pdf")

        self.name = name
        self.field_dictionary = field_dictionary
        self.xfdf = xfdfgen(self.name, self.field_dictionary)

    def write_xfdf(self, output_path: str):
        """
        Writes the xfdf document to a file

        Args:
            output_path: must be .xfdf extension
        """
        # Sanity checks
        if not output_path.endswith(".xfdf"):
            raise ValueError("Output must end with .xfdf")
        if os.path.isfile(output_path):
            raise OSError("The output file already exists.")

        try:
            with open(output_path, "w") as xfdf_file:
                self.xfdf.writexml(xfdf_file, encoding='UTF-8')
        except IOError:
            print("Error whilst writing the file")

    def pretty_print(self):
        """
        Prints the xfdf document in a human legible format onto the console

        """
        print(self.xfdf.toprettyxml())
