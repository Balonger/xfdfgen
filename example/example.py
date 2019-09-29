"""
This is an example on how to create and output an xfdf file
"""


from xfdfgen.xfdfgen import Xfdf

field_dictionary = {
    'first_name': 'foo',
    'last_name': 'bar'
}

document = Xfdf('example_pdf.pdf', field_dictionary)

# Pretty print xfdf onto the console. Not strictly necessary, but makes sanity checks easier
document.pretty_print()

document.write_xfdf('example_output.xfdf')
