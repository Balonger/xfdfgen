# xfdfgen

xfdfgen is a Python library for creating xfdf files that can be used to populate pdf form fields.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install xfdfgen.

```bash
pip install xfdfgen
```

## Usage

```python
from xfdfgen import Xfdf

pdf_document_name = 'example_document.pdf'
dictionary_of_fields= {
    'first_name': 'foo',
    'last_name': 'bar'
}

document = Xfdf(pdf_document_name, dictionary_of_fields)

output_path = 'example_out.xfdf'
document.write_xfdf(output_path)
```

pdf_document_name should match the name of the document containing the form fields you want to fill in.

The keys of the dictionary_of_fields are the form field ids 
in the document. To find them, you can use 
[Adobe Acrobat](https://acrobat.adobe.com/us/en/acrobat.html),
[pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/),
or [PDFescape](https://www.pdfescape.com/open/) if you don't want
to install anything.
   
The output can be imported with various programs/libraries, such as
[pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/),
[Foxit Reader](https://www.foxitsoftware.com/),
[Adobe Acrobat](https://acrobat.adobe.com/us/en/acrobat.html),
and [pypdftk](https://github.com/revolunet/pypdftk).

Alternatively, you can use [pdfformfields](https://github.com/Balonger/pdfformfields)
which this package was created for. pdfformfields is capable
of reading in the metadata of the pdf and 
filling in the form for you.

To view the xfdf file in a more human readable format, use

```python
document.pretty_print()
``` 
which should output

```
<?xml version="1.0" ?>
<xfdf xml:space="preserve" xmlns="http://ns.adobe.com/xfdf/">
	<f href="example_pdf.pdf"/>
	<fields>
		<field name="first_name">
			<value>foo</value>
		</field>
		<field name="last_name">
			<value>bar</value>
		</field>
	</fields>
</xfdf>
```

An example is included in the example folder.

## Compatibility
This package has been tested on Windows 10 using Python 3.7

## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/#)