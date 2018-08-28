picwall
=======

Combine several picture files into one. Written in Python.

Overview
--------

Let's say you have 6 pictures, and you want to put them into one new dark picture in 3 columns. The maximum size of every picture element will be 512x384, and there is 20 pixels of padding surround each of them. Every picture has a light gray title, from Monday to Saturday.

![from](https://raw.github.com/porter-liu/picwall/master/docs/img01.jpg)

Use following command-line to generate exactly what you want:

    python picwall.py s=512x384 p=20 c=3 b=50,50,50 t=200,200,200 f=TempoFontItalic.ttf o=out.png 01.jpg Monday 02.jpg Tuesday 03.jpg Wednesday 04.jpg Thursday 05.jpg Friday 06.jpg Saturday

![to](https://raw.github.com/porter-liu/picwall/master/docs/img02.jpg)

Syntax
------

    picwall.py [s=WIDTHxHEIGHT] [p=PADDING] [c=COLUMNS] [t=TEXT_COLOR] [b=BACKGROUND_COLOR] [f=FONT_FILE] o=OUTPUT_FILE INPUT_FILE1 [INPUT_TITLE1] ...

<table>
  <tr>
    <td>s</td> <td><i>optional</i>, the default value is 1024x768.</td> <td>The maximum <b>s</b>ize of each picture element. The format is "WIDTHxHEIGHT", for example, 100x100. Each picture will be zoomed into the box as their original ratio.</td>
  </tr>
  <tr>
    <td>p</td> <td><i>optional</i>, the default value is 50.</td> <td>The <b>p</b>adding between each picture element.</td>
  </tr>
  <tr>
    <td>c</td> <td><i>optional</i>, the default value is 2.</td> <td>The <b>c</b>olumn number of the pictures in the output file.</td>
  </tr>
  <tr>
    <td>t</td> <td><i>optional</i>, the default value is 255,255,255 (white).</td> <td>The <b>t</b>ext color if any. The format is "R,G,B", decimal number, for example, 255,0,0 (red).</td>
  </tr>
  <tr>
    <td>b</td> <td><i>optional</i>, the default value is 0,0,0 (black).</td> <td>The <b>b</b>ackground color. The format is the same with <b>t</b>.</td>
  </tr>
  <tr>
    <td>f</td> <td><i>optional</i>, no default value.</td> <td>The filename of Truetype <b>f</b>ont. It's required if there's any titles.</td>
  </tr>
  <tr>
    <td>o</td> <td><i>required</i></td> <td>The filename of the <b>o</b>utput file.</td>
  </tr>
</table>

Requirements
------------

You need Python (http://www.python.org/) 2.x to run this tool script.

picwall requires Pillow to manipulate various format pictures. For more information, please refer to https://github.com/python-pillow/Pillow.

License
-------

picwall is available under the MIT license.
