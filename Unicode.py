import unicodedata
import codecs
import os
try:
	import console
except:
	pass
		
#Always try by code
#Try by point if all numbers
#Always try name
#Try by character if length is one

#CREDITS
#https://unicode.org for all definitions (underneath)

widthdefs = {
	'F': 'Fullwidth',
	'H': 'Halfwidth',
	'W': 'Wide',
	'Na': 'Narrow',
	'A': 'Ambiguous',
	'N': 'Neutral'
}

categorydefs = {
	'Cc': 'Control',
	'Cf': 'Format',
	'Cn': 'Class not assigned',
	'Co': 'Private Use',
	'Cs': 'Surrrogate',
	'Ll': 'Lowercase Letter',
	'Lm': 'Modifier Letter',
	'Lo': 'Other Letter',
	'Lt': 'Titlecase Letter',
	'Lu': 'Uppercase Letter',
	'Mc': 'Spacing Mark',
	'Me': 'Enclosing Mark',
	'Mn': 'Nonspacing Mark',
	'Nd': 'Decimal Number',
	'Nl': 'Letter Number',
	'No': 'Other Number',
	'Pc': 'Connector Punctuation',
	'Pd': 'Dash Punctuation',
	'Pe': 'Close Punctuation',
	'Pf': 'Final Punctuation',
	'Pi': 'Initial Punctuation',
	'Po': 'Other Punctuation',
	'Ps': 'Open Punctuation',
	'Sc': 'Currency Symbol',
	'Sk': 'Modifier Symbol',
	'Sm': 'Math Symbol',
	'So': 'Other Symbol',
	'Zl': 'Line Separator',
	'Zp': 'Paragraph Separator',
	'Zs': 'Space Separator'
}

bidiclassesdefs = {
	'AL': 'Arabic Letter',
	'AN': 'Arabic Number',
	'B': 'Paragraph Separator',
	'BN': 'Boundary Neutral',
	'CS': 'Common Separator',
	'EN': 'European Number',
	'ES': 'European Separator',
	'ET': 'European Terminator',
	'FSI': 'First Strong Isolate',
	'L': 'Left To Right',
	'LRE': 'Left To Right Embedding',
	'LRI': 'Left To Right Isolate',
	'LRO': 'Left To Right Override',
	'NSM': 'Nonspacing Mark',
	'ON': 'Other Neutral',
	'PDF': 'Pop Directional Format',
	'PDI': 'Pop Directional Isolate',
	'R': 'Right To Left',
	'RLE': 'Right To Left Embedding',
	'RLI': 'Right To Left Isolate',
	'RLO': 'Right To Left Override',
	'S': 'Segment Separator',
	'WS': 'White Space'
}

combiningclassdefs = {
	'1': 'Overlay',
	'6': 'Unknown',
	'7': 'Nukta',
	'8': 'Kana Voicing',
	'9': 'Virama',
	'10': 'CCC10',
	'11': 'CCC11',
	'12': 'CCC12',
	'13': 'CCC13',
	'14': 'CCC14',
	'15': 'CCC15',
	'16': 'CCC16',
	'17': 'CCC17',
	'18': 'CCC18',
	'19': 'CCC19',
	'20': 'CCC20',
	'21': 'CCC21',
	'22': 'CCC22',
	'23': 'CCC23',
	'24': 'CCC24',
	'25': 'CCC25',
	'26': 'CCC26',
	'27': 'CCC27',
	'28': 'CCC28',
	'29': 'CCC29',
	'30': 'CCC30',
	'31': 'CCC31',
	'32': 'CCC32',
	'33': 'CCC33',
	'34': 'CCC34',
	'35': 'CCC35',
	'36': 'CCC36',
	'84': 'CCC84',
	'91': 'CCC91',
	'103': 'CCC103',
	'107': 'CCC107',
	'118': 'CCC118',
	'122': 'CCC122',
	'129': 'CCC129',
	'130': 'CCC130',
	'132': 'CCC132',
	'202': 'Attached Below',
	'214': 'Attached Above',
	'216': 'Attached Above Right',
	'218': 'Below Left',
	'220': 'Below',
	'222': 'Below Right',
	'224': 'Left',
	'226': 'Right',
	'228': 'Above Left',
	'230': 'Above',
	'232': 'Above Right',
	'233': 'Double Below',
	'234': 'Double Above',
	'240': 'Iota Subscript'
}

decompositiondefs = {
	'<circle>': 'Encircled form',
	'<compat>': 'Otherwise unspecified compatibility character',
	'<final>': 'Final presentation form (Arabic)',
	'<font>': 'Font variant',
	'<fraction>': 'Vulgar fraction form',
	'<initial>': 'Initial presentation form (Arabic)',
	'<isolated>': 'Isolated presentation form (Arabic)',
	'<medial>': 'Medial presentation form (Arabic)',
	'<narrow>': 'Narrow (or hankaku) compatibility character',
	'<noBreak>': 'No-break version of a space or hyphen',
	'<small>': 'Small variant form (CNS compatibility)',
	'<square>': 'CJK squared font variant',
	'<sub>': 'Subscript form',
	'<super>': 'Superscript form',
	'<vertical>': 'Vertical layout presentation form',
	'<wide>': 'Wide (or zenkaku) compatibility character'
}

def bypoint(inp):
	if int(inp) < 1 or int(inp) > 55291:
		return None
	return chr(int(inp))
	
def bycharacter(inp):
	return inp

def bycode(inp):
	out = []
	cs = []
	inp = inp.lower()
	if inp.startswith('u+'):
		inp = r'\u' + inp[2:]
		
	if inp.startswith(r'\u'):
		if not len(inp) > 6:
			cs.append(inp)
	elif inp.startswith(r'\x'):
		if not len(inp) > 4:
			cs.append(inp)
	else:
		if not len(inp) > 4:
			cs.append(r'\u' + inp)
		if not len(inp) > 2:
			cs.append(r'\x' + inp)
	for c in cs:
		try:
			out.append(codecs.decode(c, 'unicode-escape'))
		except UnicodeDecodeError:
			pass
	return out if len(out) > 0 else None


def byname(inp):
	inp = inp.lstrip(r'\Nn{').rstrip('}')
	try:
		return unicodedata.lookup(inp)
	except KeyError:
		return None

while True:
	characters = []
	methods = []
	inp = input()
	oginp = inp
	try:
		console.clear()
	except:
		try:
			os.system('clear')
		except:
			try:
				os.system('cls')
			except:
				pass
				
	if inp != '':
		#By character
		if len(inp) == 1:
			characters.append(bycharacter(inp))
			methods.append('character')
			
		#By name
		char = byname(inp)
		if char is not None:
			characters.append(char)
			methods.append('name')
		
		inp = inp.lower()
		
		#By point
		if inp.isnumeric() and '.' not in inp:
			characters.append(bypoint(inp))
			methods.append('point')
		
		#By code
		codes = bycode(inp)
		if codes is not None:
			for o in codes:
				characters.append(o)
				methods.append('code')
		
		remc = []
		remm = []
		for character, method in zip(characters, methods):
			if character is None:
				remc.append(character)
				remm.append(method)
		for c in remc:
			characters.remove(c)
		for m in remm:
			methods.remove(m)
					
		if len(characters) > 0:
			for character, method in zip(characters, methods):
				try:
					name = '\\N{' + unicodedata.name(character) + '}'
				except ValueError:
					name = 'Unknown'
				
				code = codecs.encode(character, 'unicode-escape').decode('utf-8')
				if code is character:
					code = hex(ord(character))
					code = code.replace('0', '\\')
				shortcode = code.lstrip(r'\u').upper()
				
				l = {
					'Character': character,
					'Name': name,
					'Code': code,
					'Point': ord(character),
					'Category': categorydefs[unicodedata.category(character)],
					'Width': widthdefs[unicodedata.east_asian_width(character)],
					'Bidi class': bidiclassesdefs[unicodedata.bidirectional(character)] if unicodedata.bidirectional(character) != '' else 'None',
					'Has mirror': 'No' if unicodedata.mirrored(character) == 0 else 'Yes',
					'Combining': unicodedata.combining(character) if unicodedata.combining(character) != 0 else 'No',
					'Decomposition': decompositiondefs[unicodedata.decomposition(character).split('>')[0] + '>'] if '<' in unicodedata.decomposition(character) else 'None'
				}
				
				print(f'DECODING BY {method.upper()}')
				print(''.join(['-' for i in range(50)]))
				for item in l.items():
					property = item[0]
					value = item[1]
					line = '{:>%i}' % 13
					print(line.format(property), '|', value)
				print(''.join(['-' for i in range(50)]))
				try:
					console.write_link('Character page', f'https://util.unicode.org/UnicodeJsps/character.jsp?a={shortcode}')
				except:
					print(f'Character page: https://util.unicode.org/UnicodeJsps/character.jsp?a={shortcode}')
				
				#print('\n\n') changed for compatibility
				print('')
				print('')
				print('')
		else:
			print(f'No results found for "{oginp}"')
