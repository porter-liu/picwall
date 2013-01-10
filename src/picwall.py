#
# Author: Porter (Zhifeng) Liu
# E-mail: liuzhf@gmail.com
# Version History:
#     v0.1   - 2012/10/04, first version, could only process 4 pictures
#     v0.2   - 2012/12/25, could process any number of pictures
#     v0.2.1 - 2013/01/09, make parameter "f" optional
#
import sys
import re
import os
import Image, ImageDraw, ImageFont


def resize( img, width, height ):
	if img.size == ( width, height ):
		return( img )

	f = (float)( img.size[0] ) / (float)( img.size[1] )
	if f > ( (float)( width ) / (float)( height ) ):
		img = img.resize( ( width, (int)( width / f ) ), Image.ANTIALIAS )
	else:
		img = img.resize( ( (int)( f * height ), height ), Image.ANTIALIAS )

	return( img )


# optional parameters (have default value)
limitWidth      = 1024
limitHeight     = 768
padding         = 50
columns         = 2
textColor       = ( 255, 255, 255 )
backgroundColor = ( 0, 0, 0 )
fontFile        = ''

# required parameters
outputFile  = ''


if len( sys.argv ) <= 1:
	print( 'Usage: ' + sys.argv[0] + ' [s=WIDTHxHEIGHT] [p=PADDING] [c=COLUMNS] [t=TEXT_COLOR] [b=BACKGROUND_COLOR] [f=FONT_FILE] o=OUTPUT_FILE INPUT_FILE1 [INPUT_TITLE1] ...' )
	exit( 1 )

#
# parameters parsing & verifying
#
inputFiles  = []
inputTitles = []

titlesPresent = False

for i in range( 1, len( sys.argv ) ):

	if sys.argv[i][1] == '=':  # options

		option = sys.argv[i][0]
		value  = sys.argv[i][2:]

		if option == 's' or option == 'S':  # maximum size
			pattern = r'(\d+)[xX](\d+)'
			po = re.compile( pattern )
			mo = po.match( value )
			if mo:
				limitWidth  = int( mo.group( 1 ) )
				limitHeight = int( mo.group( 2 ) )
			else:
				print( 'Invalid option - ' + sys.argv[i] )
				exit( 1 )

		elif option == 'p' or option == 'P':  # padding
			padding = int( value )

		elif option == 'c' or option == 'C':  # columns
			columns = int( value )

		elif option == 'o' or option == 'O':  # ouput filename
			outputFile = value

		elif option == 'f' or option == 'F':  # truetype font filename
			fontFile = value

		elif option == 't' or option == 'T':  # text color
			pattern = r'(\d+),(\d+),(\d+)'
			po = re.compile( pattern )
			mo = po.match( value )
			if mo:
				textColor = ( int( mo.group( 1 ) ), int( mo.group( 2 ) ), int( mo.group( 3 ) ) )
			else:
				print( 'Invalid text color - ' + value )
				exit( 1 )

		elif option == 'b' or option == 'B':  # background color
			pattern = r'(\d+),(\d+),(\d+)'
			po = re.compile( pattern )
			mo = po.match( value )
			if mo:
				backgroundColor = ( int( mo.group( 1 ) ), int( mo.group( 2 ) ), int( mo.group( 3 ) ) )
			else:
				print( 'Invalid background color - ' + value )
				exit( 1 )

		else:
			print( 'Unsupported option - ' + option )
			exit( 1 )

	else:  # input files/titles

		if os.path.exists( sys.argv[i] ):  # input file
			if len( inputFiles ) > len( inputTitles ):
				inputTitles.append( '' )
			inputFiles.append( sys.argv[i] )

		else:  # title
			if len( inputTitles ) >= len( inputFiles ):
				print( 'Invalid input parameters' )
				exit( 1 )
			inputTitles.append( sys.argv[i] )
			titlesPresent = True


if len( inputFiles ) > len( inputTitles ):  # make sure the number of input titles is the same with the input files
	inputTitles.append( '' )

if titlesPresent and fontFile == '':  # there's no 'f' option, but title(s) present
	print( 'Did not provide trurtype font filename' )
	exit( 1 )

if outputFile == '':  # there's no 'o' option
	print( 'Did not provide output filename' )
	exit( 1 )

if len( inputFiles ) <= 0:  # there's no input files
	print( 'Did not provide any input file' )
	exit( 1 )


inputImages = []
for file in inputFiles:
	try:
		img = Image.open( file )
		inputImages.append( resize( img, limitWidth, limitHeight ) )
	except Exception, e:
		print( 'Error: ' + e.message )
		exit( 1 )

rows = len( inputFiles ) / columns
if len( inputFiles ) % columns != 0:
	rows += 1

width  = padding * ( columns + 1 ) + limitWidth * columns
height = padding * ( rows + 1 ) + limitHeight * rows


outputImage = Image.new( 'RGB', ( width, height ) )
draw = ImageDraw.Draw( outputImage )
font = None
if titlesPresent:
	font = ImageFont.truetype( fontFile, padding - padding / 10 )

# fill background
draw.rectangle( [ ( 0, 0 ), ( width, height ) ], fill = backgroundColor )

for i in range( len( inputImages ) ):

	column = i % columns
	row    = i / columns

	# draw title
	if inputTitles[i] != '':
		draw.text(
			(
				( column + 1 ) * padding + column * limitWidth,
				row * padding + row * limitHeight
			),
			inputTitles[i],
			font = font, fill = textColor )

	# draw image
	outputImage.paste(
		inputImages[i],
		(
			( column + 1 ) * padding + column * limitWidth,
			( row + 1 ) * padding + row * limitHeight )
		)

# write the output image
try:
	outputImage.save( outputFile )
except Exception, e:
	print( 'Error: ' + e.message )
	exit( 1 )
