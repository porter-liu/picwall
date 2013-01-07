picwall
=======

Combine several picture files into one. Write in Python.

Overview
--------

![from](https://raw.github.com/porter-liu/picwall/master/docs/img01.jpg)

    python picwall.py s=512x384 p=20 c=3 b=50,50,50 t=200,200,200 f=TempoFontItalic.ttf o=out.png 01.jpg "Monday" 02.jpg "Tuesday" 03.jpg "Wednesday" 04.jpg "Thursday" 05.jpg "Friday" 06.jpg "Saturday"

![to](https://raw.github.com/porter-liu/picwall/master/docs/img02.jpg)

Syntax
------

    python picwall.py [s=WIDTHxHEIGHT] [p=PADDING] [c=COLUMNS] [t=TEXT_COLOR] [b=BACKGROUND_COLOR] [f=FONT_FILE] o=OUTPUT_FILE INPUT_FILE1 [INPUT_TITLE1] ...

<table>
  <tr>
    <td>s</td> <td>The maximum <b>s</b>ize of each picture element.</td>
  </tr>
  <tr>
    <td>p</td> <td>The <b>p</b>adding between each picture element.</td>
  </tr>
  <tr>
    <td>c</td> <td>The <b>c</b>olumn number of the pictures in the output file.</td>
  </tr>
  <tr>
    <td>t</td> <td>The <b>t</b>ext color if any.</td>
  </tr>
  <tr>
    <td>b</td> <td>The <b>b</b>ackground color.</td>
  </tr>
  <tr>
    <td>f</td> <td>The filename of Truetype <b>f</b>ont.</td>
  </tr>
  <tr>
    <td>o</td> <td>The filename of the <b>o</b>utput file.</td>
  </tr>
</table>

Requirements
------------

picwall requires PIL to manipulate various format pictures. For more information, please refer to http://www.pythonware.com/products/pil/.
