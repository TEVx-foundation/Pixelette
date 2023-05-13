from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from api.models import *
import json
import math
from PIL import Image
import itertools
from django.conf import settings

DEBUG = 1
FILE_NAME = str()
WORD_LIST = str()

db = {
	0: 'the', 
	1: 'at', 
	2: 'there', 
	3: 'some', 
	4: 'my', 
	5: 'of', 
	6: 'be', 
	7: 'use', 
	8: 'her', 
	9: 'than', 
	10: 'and', 
	11: 'this', 
	12: 'an', 
	13: 'would', 
	14: 'first', 
	15: 'a', 
	16: 'have', 
	17: 'each', 
	18: 'make', 
	19: 'water', 
	20: 'to', 
	21: 'from', 
	22: 'which', 
	23: 'like', 
	24: 'been', 
	25: 'in', 
	26: 'or', 
	27: 'she', 
	28: 'him', 
	29: 'call', 
	30: 'is', 
	31: 'one', 
	32: 'do', 
	33: 'into', 
	34: 'who', 
	35: 'you', 
	36: 'had', 
	37: 'how', 
	38: 'time', 
	39: 'oil', 
	40: 'that', 
	41: 'by', 
	42: 'their', 
	43: 'has', 
	44: 'its', 
	45: 'it', 
	46: 'word', 
	47: 'if', 
	48: 'look', 
	49: 'now', 
	50: 'he', 
	51: 'but', 
	52: 'will', 
	53: 'to', 
	54: 'find', 
	55: 'was', 
	56: 'not', 
	57: 'up', 
	58: 'more', 
	59: 'long', 
	60: 'for', 
	61: 'what', 
	62: 'other', 
	63: 'write', 
	64: 'down', 
	65: 'on', 
	66: 'all', 
	67: 'about', 
	68: 'go', 
	69: 'day', 
	70: 'are', 
	71: 'were', 
	72: 'out', 
	73: 'see', 
	74: 'did', 
	75: 'as', 
	76: 'we', 
	77: 'many', 
	78: 'number', 
	79: 'get', 
	80: 'with', 
	81: 'when', 
	82: 'then', 
	83: 'no', 
	84: 'come', 
	85: 'his', 
	86: 'your', 
	87: 'them', 
	88: 'way', 
	89: 'made', 
	90: 'they', 
	91: 'can', 
	92: 'these', 
	93: 'could', 
	94: 'may', 
	95: 'i', 
	96: 'said', 
	97: 'so', 
	98: 'people', 
	99: 'part', 
	100: ' ', 
	101: 'a', 
	102: 'b', 
	103: 'c', 
	104: 'd', 
	105: 'e', 
	106: 'f', 
	107: 'g', 
	108: 'h', 
	109: 'i', 
	110: 'j', 
	111: 'k', 
	112: 'l', 
	113: 'm', 
	114: 'n', 
	115: 'o', 
	116: 'p', 
	117: 'q', 
	118: 'r', 
	119: 's', 
	120: 't', 
	121: 'u', 
	122: 'v', 
	123: 'w', 
	124: 'x', 
	125: 'y', 
	126: 'z', 
	127: 'A', 
	128: 'B', 
	129: 'C', 
	130: 'D', 
	131: 'E', 
	132: 'F', 
	133: 'G', 
	134: 'H', 
	135: 'I', 
	136: 'J', 
	137: 'K', 
	138: 'L', 
	139: 'M', 
	140: 'N', 
	141: 'O', 
	142: 'P', 
	143: 'Q', 
	144: 'R', 
	145: 'S', 
	146: 'T', 
	147: 'U', 
	148: 'V', 
	149: 'W', 
	150: 'X', 
	151: 'Y', 
	152: 'Z', 
	153: '__FLAG__', 
	154: '__UPPER__', 
	155: '__LOWER__', 
	156: '__CAP__', 
	157: '__APPOS__', 
	158: '__INDENT__', 
	159: '__JOINT__', 
	160: '__NEW__', 
	161: '__SENTENCE__', 
	162: '__QUESTION__', 
	163: '__EXCLAMATION__',
	164: '__NULL__', 
	165: '__UPPER_SINGLE__', 
	166: '__LOWER_SINGLE__', 
	167: '__CAP_SINGLE__', 
	168: 'Word', 
	169: 'Word', 
	170: 'Word', 
	171: 'Word', 
	172: 'Word', 
	173: 'Word', 
	174: 'Word', 
	175: 'Word', 
	176: 'Word', 
	177: 'Word', 
	178: 'Word', 
	179: 'Word', 
	180: 'Word', 
	181: 'Word', 
	182: 'Word', 
	183: 'Word', 
	184: 'Word', 
	185: 'Word', 
	186: 'Word', 
	187: 'Word', 
	188: 'Word', 
	189: 'Word', 
	190: 'Word', 
	191: 'Word', 
	192: 'Word', 
	193: 'Word', 
	194: 'Word', 
	195: 'Word', 
	196: 'Word', 
	197: 'Word', 
	198: 'Word', 
	199: 'Word', 
	200: 'Word', 
	201: 'Word', 
	202: 'Word', 
	203: 'Word', 
	204: 'Word', 
	205: 'Word', 
	206: 'Word', 
	207: 'Word', 
	208: 'Word', 
	209: 'Word', 
	210: 'Word', 
	211: 'Word', 
	212: '’', 
	213: '\'', 
	214: '9', 
	215: '8', 
	216: '7', 
	217: '6', 
	218: '5', 
	219: '4', 
	220: '3', 
	221: '2', 
	222: '1', 
	223: '0', 
	224: '~', 
	225: '`', 
	226: '/', 
	227: '?', 
	228: '.', 
	229: ',', 
	230: '>', 
	231: '<', 
	232: '"', 
	233: '\'', 
	234: ':', 
	235: ';', 
	236: '|', 
	237: '\\', 
	238: '}', 
	239: '{', 
	240: ']', 
	241: '[', 
	242: '_', 
	243: '=', 
	244: '+', 
	245: '-', 
	246: ')', 
	247: '(', 
	248: '*', 
	249: '&', 
	250: '^', 
	251: '%', 
	252: '$', 
	253: '#', 
	254: '@', 
	255: '!'
}

dbwords = tuple(db.values())[:100]
dbletters = tuple(db.values())[101:153]
flag_start, flag_end = 153, 223
word_start, word_end = 0, 99

_flag_val = {
		"join": None,
	}

def _error(code: int):
	next

def create(height, width, data):
	''' Create an image from the data. '''

	global FILE_NAME
	
	img = Image.new('RGB', (width, height), color = (164, 164, 164))
	pixels = img.load()
	image_size = img.size
	print("Image size: ", image_size, " Given size: ", width, height)
		  
	for i in range(width):
		for j in range(height):
			try:
				img.putpixel((i, j), tuple(data[i][j]))
				if (DEBUG):
					print("Pixel: ", i, j, "Value: ", tuple(data[i][j]))
			except:
				pixel_value = (164, 164, 164)
				img.putpixel((i, j), pixel_value)
				if (DEBUG):
					print("Pixel: ", i, j, "Null value: ", pixel_value)
	file_name = str(uuid.uuid1())
	img.save('general/files/' + file_name + '.png')
	FILE_NAME = 'general/files/' + file_name + '.png'

def read(file_name):
	''' Read the image and return the data. '''
	
	img = Image.open(file_name)
	pixels = img.load()
	image_size = img.size
	data = []
	for i in range(image_size[0]):
		for j in range(image_size[1]):
			data.append(pixels[i, j])

	''' Remove the null values. '''

	for i in range(data.count((164, 164, 164))):
		data.pop()

	print("Extracted data: ", data)
	data = list(itertools.chain(*data))
	return data


def _pixel_split(a, n):
	''' Analyse the data and calculate the deminesion and pixels
		this makes it into an equally shaped matrix. '''
	
	k, m = divmod(len(a), n)
	return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

def chunks_split(data: list):
	''' Analyse the data and calculate the deminesion and pixels
		this groups the data into a pair of 3. '''
	
	for i in range(0, len(data), 3):
		yield data[i:i + 3]

def pixel_analysis(data: tuple):
	''' Analyse the data and calculate the deminesion and pixels
		of the required image. '''

	_pexel = list(chunks_split(data))

	''' Analyse the data and correct the pixel count into multiple of 3.'''

	if len(_pexel[-1]) % 3 != 0:
		_pexel[-1].extend([164] * (3 - len(_pexel[-1]) % 3))

	_root = int(math.sqrt(len(_pexel)))
	if (DEBUG):
		print("\nPexel Analysis: ", _pexel)

	analyse = tuple(_pixel_split(tuple(_pexel), _root))
	print("\nRow Analysis: ", analyse)

	pixel_width, pixel_height = len(analyse[0]), len(analyse)
	print("\nPixel Width: ", pixel_width, "\nPixel Height: ", pixel_height)

	''' Initiate the creation of the image. '''

	create(pixel_height, pixel_width, analyse)


def bytecode(data: str, delimiter: str = " "):
	''' Encode the data into a list of numbers. '''

	final_data, ds = list(), data.split()
	flag_begin, flag_end = [153], list()

	''' Now process the basic flags for the data - flag_end
		Lengthly and complex processes. '''

	delimiter_code = list(i for i in db if db[i] == delimiter)[0]
	flag_end.extend([159, delimiter_code])

	''' Now process the basic flags for the data - flag_begin
		Lengthly and complex processes. '''

	''' if (data.endswith("?")):
		flag_begin.append(162)
	elif (data.endswith("!")):
		flag_begin.append(163)
	elif (data.endswith(".")):
		flag_begin.append(161) '''

	if (DEBUG):
		print("Data after type removal: ", ds)

	for d in ds:

		''' Now process the basic flags for the data - data_codes
		Lengthly and complex processes. '''

		if (DEBUG):
			print("Data element: ", d)

		_listx = list(i for i in db if db[i] == d.lower())
		if (d.lower() in dbwords and len(_listx) != 0):
			if (DEBUG):
				print("Word present: ", d.lower())
				print("Word code: ", _listx[0])
			value = _listx[0]
			if (d.istitle()):
				final_data.append(156)
				final_data.append(value)
			elif (d.isupper()):
				final_data.append(154)
				final_data.append(value)
			elif (d.islower()):
				final_data.append(155)
				final_data.append(value)
			else: final_data.append(value)
		else:
			if (DEBUG):
				print(":: Delimiter adding: ", delimiter_code, ", Letter: ", d)
			final_data.append(delimiter_code)
			for letter in d:
				print("Letter: ", letter)
				_ = list(i for i in db if db[i] == letter)
				final_data.append(_[-1])
				if (DEBUG):
					print(":: Letter added: ", letter, " , code: ", _ , " :: ", end = "")
			final_data.append(delimiter_code)
			if (DEBUG):
				print("\n:: Delimiter contained: ", delimiter_code, ", Letter: ", d)
		
	flag_end.append(153)
	_encoded = flag_begin + final_data + flag_end

	if (DEBUG):
		print(f'Flag begin: {flag_begin}, Flag end: {flag_end}, Data: {final_data}')
		print(f'\nFinal data: {flag_begin + final_data + flag_end}')
	pixel_analysis(_encoded)

	print("\nTesting the data: ", analyse(_encoded))

def preprocess(word_list: list, flags_el: list, flag_val: dict):
	''' Now process the data elements into a sentence using the words and flags.
		Lengthly and complex processes. '''
	
	global WORD_LIST
	
	final_data = str()
	if (DEBUG):
		print("Flag values are: ", flag_val)
	
	for flag in flags_el:
		if (flag == "__UPPER__"):
			word_list = [word.upper() for word in word_list]
		elif (flag == "__LOWER__"):
			word_list = [word.lower() for word in word_list]
		elif (flag == "__SENTENCE__"):
			word_list[-1] = word_list[-1] + "."
		elif (flag == "__QUESTION__"):
			word_list[-1] = word_list[-1] + "?"
		elif (flag == "__EXCLAMATION__"):
			word_list[-1] = word_list[-1] + "!"
		elif (flag == "__NEW__"):
			word_list[-1] = word_list[-1] + "\n"

	''' Now merge the data using final flags present in the flag_val dictionary.
		Error-prone and complex processes. '''
		
	for val in flag_val.keys():
		if (val == "join" and flag_val["join"] != None):
			final_data = (flag_val["join"]).join(word_list)
			if (DEBUG):
				print("\nProcessed data: " + final_data)
			WORD_LIST = final_data
			break
		else:
			final_data = " ".join(word_list)
			if (DEBUG):
				print("\nProcessed data: " + final_data)
			WORD_LIST = final_data
			break

def analyse(data: tuple):

	global WORD_LIST

	flag_on, join_on, index_count = False, False, 0
	flags_el, word_list, letter_bind = list(), list(), str()
	flag_val = dict(_flag_val)

	join_value, join_index = data[data.index(159) + 1], data.index(159)

	''' Splitting the data elements into a single words and letters
			in the set of following data elements. '''
	
	_flag, sub_el, res = False, list(), list()
	wordlimit = list(i for i in range(0, 100))

	for i in data[:join_index]:
		if (not _flag):
			if (i != join_value): res.append(i)
			else: _flag = 1
		else:
			if ((i != join_value) and (i not in wordlimit)): sub_el.append(i)
			elif((i != join_value) and (i in wordlimit)): res.append(i)
			elif (i == join_value):
				res.append(list(sub_el))
				sub_el.clear()
				_flag = 0
			
	data = tuple(res) + tuple(data[join_index:])
	print("Data after parsing: ", data)

	for dat in data:
		''' Flag element authorization used to skip the next element
			in the set of following data elements. '''
		
		if (DEBUG):
			print("Parsing data element: " + str(dat))
		
		if (join_on):
			join_on = False
		
		''' Analyse the data elements sequentially and check if they are null characters or not.
			more-like pos in a sentence. '''
		
		if (dat == 164):
			index_count += 1
			continue

		''' Analyse the data elements sequentially and split the data into words and flags.
			more-like pos in a sentence. '''
		
		if ((not flag_on) and dat == 153):
			flag_on = True
			if (DEBUG):
				print("::: Debugging turned on.")

		elif ((type(dat) == int) and dat > 153 and dat <= 223):
			flags_el.append(db[dat])
			if (DEBUG):
				print("Flag element: " + db[dat])

			if (dat == 159):
				join_on = True
				flag_val["join"] = db[(data[index_count + 1])]
				if (DEBUG):
					print("Using join flag for: " + db[(data[index_count + 1])])
				''' Join the next element with the current elements.'''

			elif (dat == 157):
				db[(data[index_count + 1])] += "'s"
				''' Join an appostraphe to the next element.'''

			elif (dat == 165):
				db[(data[index_count + 1])] = db[(data[index_count + 1])].upper()
				''' Upper the next element.'''

			elif (dat == 156):
				db[(data[index_count + 1])] = db[(data[index_count + 1])].capitalize()
				''' Captialize the next element.'''

			elif (dat == 158):
				word_list.append("    ")
				''' Add 4 spaces to the next element.'''

		elif (dat == 153):
			print("Flag turned off.")
			if (flag_on):
				flag_on = False
				if (DEBUG):
					print("final word-list: ", word_list)
					WORD_LIST = list(word_list)
				preprocess(word_list, flags_el, flag_val)
				flags_el, word_list = list(), list()
				flag_val = dict(_flag_val)
		else:
			if (flag_on):
				if ((type(dat) == int) and dat in db.keys()):
					if (DEBUG):
						print("Word: " + db[dat])
					word_list.append(db[dat])
				else:
					for i in dat:
						if (i in db.keys()):
							if (DEBUG):
								print("Letter: " + db[i])
							letter_bind += db[i]
						else:
							if (DEBUG):
								print("Letter: " + chr(i))
							letter_bind += chr(i)
					if (DEBUG):
						print("Word: " + letter_bind)
					word_list.append(letter_bind)
					letter_bind = str()
			else:
				_error(100)
				break
		index_count += 1

# bytecode(third_text)
# data = read('second_story.png')
# analyse(data)

@csrf_exempt
def encode(request):
	if request.method == "POST":
		serializer = json.loads(request.body)
		# print(request.POST)
		# data = request.POST["text"]
		data = serializer["text"]
		reqHistory = History.objects.create()
		bytecode(data)

		reqHistory.data = data
		reqHistory.link = FILE_NAME
		reqHistory.save()

		return render(request, "Encode.json", {"link": FILE_NAME, "data": data}, content_type="application/json")
	else:
		return render(request, "Encode.html", {"posted": False })

@csrf_exempt
def decode(request):
	if request.method == "POST":
		pic = request.FILES.get('pixelpic')
		reqHistory = History.objects.create()
		reqHistory.pixel = pic
		data = read(pic)
		analyse(data)

		reqHistory.data = WORD_LIST
		reqHistory.save()
		return render(request, "Decode.json", {"data": WORD_LIST}, content_type="application/json")
	else:
		return render(request, "Decode.html", {"posted": False })

def listAll(request):
	return render(request, "List.html", {})