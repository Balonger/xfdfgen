import xml.dom.minidom


def xfdfgen(name, field_dictionary):
    """
    Generates an xml.dom.minidom xml document in xfdf format given a pdf containing form fields
    and a dictionary containing the fields
    :param name: path to the pdf document
    :param field_dictionary: a dictionary with form field id as key and their values as value
    :return:
    """

    xfdf = xml.dom.minidom.Document()

    # --------------------------------    xfdf peculiarities ------------------------------------
    # see https://docs.aspose.com/display/pdfnet/Whats+the+Difference+Between+XML%2C+FDF+and+XFDF

    top = xfdf.createElement("xfdf")
    top.setAttribute("xmlns", "http://ns.adobe.com/xfdf/")
    top.setAttribute("xml:space", "preserve")
    xfdf.appendChild(top)

    f = xfdf.createElement("f")
    f.setAttribute("href", name)
    top.appendChild(f)

    # ------------------------------   insert fields from dictionary   --------------------------------
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
    def __init__(self, name, field_dictionary):
        """
        Initializes an xfdf form xml.
        Use .write_xfdf() to write to a file
        Use .get_xfdf to return the raw xfdf string
        Use .pretty_print to pretty print the xfdf file to console

        :param name: path to the pdf document
        :param field_dictionary: a dictionary with form field id as key and their values as value
        """
        self.name = name
        self.field_dictionary = field_dictionary
        self.xfdf = xfdfgen(self.name, self.field_dictionary)

    def write_xfdf(self, output_path):
        """
        Writes the xfdf document to a file
        :param output_path: must be .xfdf extension
        :return:
        """
        with open(output_path, "w") as xfdf_file:
            self.xfdf.writexml(xfdf_file, encoding='UTF-8')

    def get_xfdf(self):
        """
        :return: raw xfdf documentá
        """
        return self.xfdf

    def pretty_print(self):
        """
        Prints the xfdf document in a human legible format onto the console
        """
        print(self.xfdf.toprettyxml())
