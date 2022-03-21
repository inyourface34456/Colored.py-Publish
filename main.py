from time import sleep

css_colors = {
	'black': [0,0,0],
	'silver': [192, 192, 192],
	'grey': [128,128,128],
	'gray': [128,128,128],
	'white': [255,255,255],
	'maroon': [128,0,0],
	'red': [255, 0, 0],
	'purple': [128,0,128],
	'fuchsia': [255,0,255],
	'green': [0,128,0],
	'lime': [0,255,0],
	'olive': [128,128,0],
	'yellow': [255,255,0],
	'navy': [0,0,128],
	'blue': [0,0,255],
	'teal': [0,128,128],
	'aqua': [0,255,255],
	'aliceblue': [240,248,255],
	'antiquewhite': [250,235,215],
	'aquamarine': [127,255,212],
	'azure': [240,255,255],
	'beige': [245,245,220],
	'bisque': [255,228,196],
	'blanchedalmond': [255,235,205],
	'blueviolet': [138,43,226],
	'brown': [165,42,42],
	'burlywood': [222,184,135],
	'cadetblue:': [95,158,160],
	'chartreuse': [127,255,0],
	'chocolate': [210,105,30],
	'coral': [255,127,80],
	'cornflowerblue': [100,149,237],
	'cornsilk': [255,248,220],
	'crimson': [220,20,60],
	'cyan': [0,255,255],
	'darkblue': [0,0,139],
	'darkcyan': [0,139,139],
	'darkgoldenrod': [184,134,11],
	'darkgray': [169,169,169],
	'darkgreen': [0,100,0],
	'darkgrey': [169,169,169],
	'darkkhaki': [189,183,107],
	'darkmagenta': [139,0,139],
	'darkolivegreen': [85,107,47],
	'darkorange': [255,140,0],
	'darkorchid': [153,50,204],
	'darkred': [139,0,0],
	'darksalmon': [233,150,122],
	'darkseagreen': [143,188,143],
	'darkslateblue': [72,61,139],
	'darkslategray': [47,79,79],
	'darkslategrey': [47,79,79],
	'darkturquoise': [0,206,209],
	'darkviolet': [148,0,211],
	'deeppink': [255,20,147],
	'deepskyblue': [0,191,255],
	'dimgray': [105,105,105],
	'dimgrey': [105,105,105],
	'dodgerblue': [30,144,255],
	'firebrick': [178,34,34],
	'floralwhite': [255,250,240],
	'forestgreen': [34,139,34],
	'gainsboro': [220,220,220],
	'ghostwhite': [248,248,255],
	'gold': [255,215,0],
	'goldenrod': [218,165,32],
	'greenyellow': [173,255,47],
	'honeydew': [240,255,240],
	'hotpink': [255,105,180],
	'indianred': [205,92,92],
	'indigo': [75,0,130],
	'ivory': [255,255,240],
	'khaki': [240,230,140],
	'lavender': [230,230,250],
	'lavenderblush': [255,240,245],
	'lawngreen': [124,252,0],
	'lemonchiffon': [255,250,205],
	'lightblue': [173,216,230],
	'lightcoral': [240,128,128],
	'lightcyan': [224,255,255],
	'lightgoldenrodyellow': [250,250,210],
	'lightgray': [211,211,211],
	'lightgreen': [144,238,144],
	'lightgrey': [211,211,211],
	'lightpink': [255,182,193],
	'lightsalmon': [255,160,122],
	'lightseagreen': [32,178,170],
	'lightskyblue': [135,206,250],
	'lightslategray': [119,136,153],
	'lightslategrey': [119,136,153],
	'lightsteelblue': [176,196,222],
	'lightyellow': [255,255,224],
	'limegreen': [50,205,50],
	'linen': [250,240,230],
	'magenta': [255,0,255],
	'mediumaquamarine': [102,205,170],
	'mediumblue': [0,0,205],
	'mediumorchid': [186,85,211],
	'mediumpurple': [147,112,219],
	'mediumseagreen': [60,179,113],
	'mediumslateblue': [123,104,238],
	'mediumspringgreen': [0,250,154],
	'mediumturquoise': [72,209,204],
	'mediumvioletred': [199,21,133],
	'midnightblue': [25,25,112],
	'mintcream': [245,255,250],
	'mistyrose': [255,228,225],
	'moccasin': [255,228,181],
	'navajowhite': [255,222,173],
	'oldlace': [253,245,230],
	'olivedrab': [107,142,35],
	'orange': [255,165,0],
	'orangered': [255,69,0],
	'orchid': [218,112,214],
	'palegoldenrod': [238,232,170],
	'palegreen': [152,251,152],
	'paleturquoise': [175,238,238],
	'palevioletred': [219,112,147],
	'papayawhip': [255,239,213],
	'peachpuff': [255,218,185],
	'peru': [205,133,63],
	'pink': [255,192,203],
	'plum': [221,160,221],
	'powderblue': [176,224,230],
	'rosybrown': [188,143,143],
	'royalblue': [65,105,225],
	'saddlebrown': [139,69,19],
	'salmon': [250,128,114],
	'sandybrown': [244,164,96],
	'seagreen': [46,139,87],
	'seashell': [255,245,238],
	'sienna': [160,82,45],
	'skyblue': [135,206,235],
	'slateblue': [106,90,205],
	'slategray': [112,128,144],
	'slategrey': [112,128,144],
	'snow': [255,250,250],
	'springgreen': [0,255,127],
	'steelblue': [70,130,180],
	'tan': [210,180,140],
	'thistle': [0,128,128],
	'tomato': [255,99,71],
	'turquoise': [64,224,208],
	'violet': [238,130,238],
	'wheat': [245,222,179],
	'whitesmoke': [245,245,245],
	'yellowgreen': [154,205,50],
	'default': [32, 36, 52]
}

def check_in_array(list_to_cheack, thing_to_cheack_for, case_sensativity):
	ltc = list_to_cheack
	ttcf = thing_to_cheack_for
	t = ''
	for i in range(len(ltc)):
		t = str(ltc[i])
		if case_sensativity:
			if t == ttcf:
				return True
				break
		else:
			if t.lower().strip() == ttcf:
				return True
				break

# this will define the cprint function. This function suports RGB, HEX, and all extended css keyword color values.  This also suports mixed color methods (i.e hex and RGB simultaneously).


def cprint(toprint, rgb = None, on_rgb = None, hex = None, on_hex = None, keyword = None, on_keyword = None, attrs = None):
	fore_count = 0
	back_count = 0
	fore_in_use = ''
	back_in_use = ''
	string_to_print = ''

	if attrs != None:
		if check_in_array(attrs, 'bold', False):
			string_to_print += '\u001b[1m'
		if check_in_array(attrs, 'fade', False):
			string_to_print += '\u001b[2m'
		if check_in_array(attrs, 'italic', False):
			string_to_print += '\u001b[3m'
		if check_in_array(attrs, 'underline', False):
			string_to_print += '\u001b[4m'
		if check_in_array(attrs, 'reversed', False):
			string_to_print += '\u001b[7m'
		if check_in_array(attrs, 'hidden', False):
			string_to_print += '\u001b[8m'
		if check_in_array(attrs, 'strikeout', False):
			string_to_print += '\u001b[9m'
	
	if rgb != None:
		fore_count += 1
		fore_in_use = 'RGB'
	
	if on_rgb != None:
		back_count += 1
		back_in_use = 'RGB'
	
	if hex != None:
		fore_count += 1
		fore_in_use = 'HEX'
	
	if on_hex != None:
		back_count += 1
		back_in_use = 'HEX'
	
	if keyword != None:
		fore_count += 1
		fore_in_use = 'KEYWORD'
	
	if on_keyword != None:
		back_count += 1
		back_in_use = 'KEYWORD'

	if rgb == None:
		rgb = []
	if on_rgb == None:
		on_rgb = []
	
	if (back_count == 1) and (fore_count == 1):
		# seeing wich type of color the user is using
		if fore_in_use == 'RGB':
			string_to_print += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}'
		
		if fore_in_use == 'HEX':
			for i in (0, 2, 4):
				decimal = int(hex[i:i+2], 16)
				rgb.append(decimal)	
			string_to_print += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}'
		
		if fore_in_use == 'KEYWORD':
			rgb = css_colors[keyword.lower().strip()]
			string_to_print += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}'

		if back_in_use == 'RGB':
				string_to_print += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m{toprint}\u001b[0m'
			
		if back_in_use == 'HEX':
			for i in (0, 2, 4):
				decimal = int(on_hex[i:i+2], 16)
				on_rgb.append(decimal)
			
			string_to_print += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m{toprint}\u001b[0m'
		
		if back_in_use == 'KEYWORD':
			on_rgb = css_colors[on_keyword.lower().strip()]
			string_to_print += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m{toprint}\u001b[0m'
	
	else:
		raise ValueError('Only one forground and one background is allowed.')
	
	print(string_to_print)

# this will define the type print function.  This will print out the letters of a given string value with a given delay (defults to .1 seconds).


def type_print(toprint, delay = 0.1, end = '\n', rgb = None, on_rgb = None, hex = None, on_hex = None, keyword = None, on_keyword = None, attrs = None):
	fore_count = 0
	back_count = 0
	fore_in_use = ''
	back_in_use = ''
	colors = ''

	if attrs != None:
		if check_in_array(attrs, 'bold', False):
			colors += '\u001b[1m'
		if check_in_array(attrs, 'fade', False):
			colors += '\u001b[2m'
		if check_in_array(attrs, 'italic', False):
			colors += '\u001b[3m'
		if check_in_array(attrs, 'underline', False):
			colors += '\u001b[4m'
		if check_in_array(attrs, 'reversed', False):
			colors += '\u001b[7m'
		if check_in_array(attrs, 'hidden', False):
			colors += '\u001b[8m'
		if check_in_array(attrs, 'strikeout', False):
			colors += '\u001b[9m'
	
	if rgb != None:
		fore_count += 1
		fore_in_use = 'RGB'
	
	if on_rgb != None:
		back_count += 1
		back_in_use = 'RGB'
	
	if hex != None:
		fore_count += 1
		fore_in_use = 'HEX'
	
	if on_hex != None:
		back_count += 1
		back_in_use = 'HEX'
	
	if keyword != None:
		fore_count += 1
		fore_in_use = 'KEYWORD'
	
	if on_keyword != None:
		back_count += 1
		back_in_use = 'KEYWORD'

	if rgb == None:
		rgb = []
	if on_rgb == None:
		on_rgb = []
	
	if (back_count == 1) and (fore_count == 1):
		# seeing wich type of color the user is using
		if fore_in_use == 'RGB':
			colors += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}'
		
		if fore_in_use == 'HEX':
			for i in (0, 2, 4):
				decimal = int(hex[i:i+2], 16)
				rgb.append(decimal)	
			colors += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}'
		
		if fore_in_use == 'KEYWORD':
			rgb = css_colors[keyword.lower().strip()]
			colors += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}'

		if back_in_use == 'RGB':
			colors += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m'
			
		if back_in_use == 'HEX':
			for i in (0, 2, 4):
				decimal = int(on_hex[i:i+2], 16)
				on_rgb.append(decimal)
			colors += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m'
		
		if back_in_use == 'KEYWORD':
			on_rgb = css_colors[on_keyword.lower().strip()]
			colors += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m'
	
	else:
		raise ValueError('Only one forground and one background is allowed.')

	print(colors, end = '')
	for i in range(len(toprint)):
		print(f'{toprint[i]}', end = "", flush = True)
		sleep(delay)
	reset(toprint = True)

# This defines the avarge function.  This function can take either a directly inputted list, or an array.  It will also take a persion value, wich will allow that user to select the number of decmal places a number is rounded to.

def average(*nums, array = None, persion = 2):
	c = 0
	if array == None:
		for i in range(len(nums)):
			c += nums[i]
		c /= len(nums)
		return round(c, persion)
	else:
		for i in range(len(array)):
			c += array[i]
		c /= len(array)
		return round(c, persion)
	
# This defines tha genorator function.  This will allow the user to genorate a string that has the ecape sequence to color and reset a string to the deired color.  If no string is passed, it will genorate a string that is just an ecape sequence, without the reset code at the end.

def generator(toprint, rgb = None, on_rgb = None, hex = None, on_hex = None, keyword = None, on_keyword = None, attrs = None):
	fore_count = 0
	back_count = 0
	fore_in_use = ''
	back_in_use = ''
	string_to_return = ''

	if attrs != None:
		if check_in_array(attrs, 'bold', False):
			string_to_return += '\u001b[1m'
		if check_in_array(attrs, 'fade', False):
			string_to_return += '\u001b[2m'
		if check_in_array(attrs, 'italic', False):
			string_to_return += '\u001b[3m'
		if check_in_array(attrs, 'underline', False):
			string_to_return += '\u001b[4m'
		if check_in_array(attrs, 'reversed', False):
			string_to_return += '\u001b[7m'
		if check_in_array(attrs, 'hidden', False):
			string_to_return += '\u001b[8m'
		if check_in_array(attrs, 'strikeout', False):
			string_to_return += '\u001b[9m'
	
	if rgb != None:
		fore_count += 1
		fore_in_use = 'RGB'
	
	if on_rgb != None:
		back_count += 1
		back_in_use = 'RGB'
	
	if hex != None:
		fore_count += 1
		fore_in_use = 'HEX'
	
	if on_hex != None:
		back_count += 1
		back_in_use = 'HEX'
	
	if keyword != None:
		fore_count += 1
		fore_in_use = 'KEYWORD'
	
	if on_keyword != None:
		back_count += 1
		back_in_use = 'KEYWORD'

	if rgb == None:
		rgb = []
	if on_rgb == None:
		on_rgb = []
	
	if (back_count == 1) and (fore_count == 1):
		# seeing wich type of color the user is using
		if fore_in_use == 'RGB':
			string_to_return += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}'
		
		if fore_in_use == 'HEX':
			for i in (0, 2, 4):
				decimal = int(hex[i:i+2], 16)
				rgb.append(decimal)	
			string_to_return += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}'
		
		if fore_in_use == 'KEYWORD':
			rgb = css_colors[keyword.lower().strip()]
			string_to_return += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}'

		if back_in_use == 'RGB':
			if toprint == '':
				string_to_return += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m{toprint}'
			else:
				string_to_return += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m{toprint}\u001b[0m'
			
		if back_in_use == 'HEX':
			for i in (0, 2, 4):
				decimal = int(on_hex[i:i+2], 16)
				on_rgb.append(decimal)
			
			if toprint == '':
				string_to_return += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m{toprint}'
			else:
				string_to_return += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m{toprint}\u001b[0m'
		
		if back_in_use == 'KEYWORD':
			on_rgb = css_colors[on_keyword.lower().strip()]
			
			if toprint == '':
				string_to_return += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m{toprint}'
			else:
				string_to_return += f';48;2;{on_rgb[0]};{on_rgb[1]};{on_rgb[2]}m{toprint}\u001b[0m'
	
	else:
		raise ValueError('Only one forground and one background is allowed.')
	
	return string_to_return

def reset(toprint = False):
	if toprint:
		print('\u001b[0m')
	else:
		return '\u001b[0m'


def clear(toprint = False):
	if toprint:
		print('\033c')
	else:
		return '\033c'
