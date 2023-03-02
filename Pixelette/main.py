import math
from PIL import Image
import itertools

DEBUG = 1

''' Words and alphabhet data-mapping using dictionary
    along with their flagging code points binded to a dictionary. '''

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
    file_name = input('Enter the file name: ')
    img.save(file_name + '.png')

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

        if (d.lower() in dbwords):
            if (DEBUG):
                print("Word present: ", d.lower())
            value = list(i for i in db if db[i] == d.lower())[0]
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
    print('Analyse: ', pixel_analysis(_encoded))

    # print("\nTesting the data: ", analyse(_encoded))

def preprocess(word_list: list, flags_el: list, flag_val: dict):
    ''' Now process the data elements into a sentence using the words and flags.
        Lengthly and complex processes. '''
    
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
            break
        else:
            final_data = " ".join(word_list)
            if (DEBUG):
                print("\nProcessed data: " + final_data)
            break

def analyse(data: tuple):
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


# chars = (153, 154, 163, 157, 0, 158, 1, 159, 229, 160, 153)
# test_data = [153, 161, 161, 161, 161, 161, 161, 146, 108, 105, 103, 15, 120, 155, 30, 155, 1, 120, 108, 105, 108, 15, 120, 228, 159, 100, 159, 100, 159, 100, 159, 100, 159, 100, 159, 100, 153]
# text: "How are you dear?"

chars = (153, 162, 155, 156, 37, 70, 35, 100, 104, 105, 101, 118, 100, 159, 100, 153)

''' chars = """
(153, 156, 81, 155, 0, 100, 101, 109, 104, 105, 119, 100, 155, 65, 155, 0, 100, 114, 109, 107, 108, 120, 100, 100, 119, 108, 109, 106, 120, 100, 100, 104, 118, 109, 106, 120, 100, 100, 115, 106, 106, 100, 155, 20, 100, 119, 112, 105, 105, 116, 229, 100, 100, 118, 105, 119, 109, 104, 105, 114, 120, 119, 100, 100, 110, 121, 113, 116, 100, 155, 72, 155, 5, 100, 102, 105, 104, 228, 100, 100, 146, 109, 116, 120, 115, 105, 100, 155, 64, 100, 108, 101, 112, 112, 123, 101, 125, 119, 100, 155, 20, 155, 0, 100, 118, 105, 103, 118, 105, 101, 120, 109, 115, 114, 100, 100, 118, 115, 115, 113, 228, 100, 156, 14, 155, 31, 155, 25, 100, 108, 109, 120, 119, 100, 155, 0, 100, 112, 109, 107, 108, 120, 119, 228, 100, 100, 141, 114, 103, 105, 100, 100, 112, 115, 114, 107, 245, 112, 109, 113, 102, 105, 104, 100, 100, 102, 105, 101, 121, 120, 109, 105, 119, 229, 100, 155, 49, 100, 103, 118, 105, 116, 105, 245, 116, 101, 116, 105, 118, 100, 100, 119, 111, 109, 114, 114, 105, 104, 229, 100, 155, 90, 100, 119, 108, 109, 113, 113, 125, 229, 100, 155, 90, 100, 119, 108, 101, 111, 105, 229, 100, 155, 90, 100, 119, 108, 109, 113, 113, 105, 118, 228, 100, 100, 133, 118, 105, 120, 101, 100, 155, 21, 100, 128, 100, 100, 107, 118, 101, 102, 119, 100, 100, 129, 108, 101, 118, 112, 105, 119, 100, 155, 21, 100, 220, 137, 228, 100, 156, 0, 100, 120, 123, 115, 100, 100, 113, 101, 113, 102, 115, 229, 100, 100, 146, 109, 120, 115, 100, 100, 142, 121, 105, 114, 120, 105, 100, 155, 25, 155, 42, 100, 108, 105, 101, 104, 119, 228, 100, 100, 131, 104, 113, 115, 114, 104, 100, 100, 102, 101, 118, 105, 112, 125, 100, 100, 113, 109, 119, 119, 105, 119, 100, 100, 116, 115, 115, 118, 100, 100, 131, 104, 114, 101, 212, 119, 100, 100, 120, 115, 105, 119, 228, 100, 100, 145, 108, 109, 118, 112, 105, 125, 100, 100, 119, 112, 109, 104, 105, 119, 100, 155, 33, 155, 15, 100, 119, 116, 112, 109, 120, 228, 100, 100, 141, 108, 255, 100, 156, 0, 100, 104, 101, 125, 119, 100, 100, 130, 105, 102, 100, 100, 104, 101, 114, 103, 105, 104, 100, 155, 23, 100, 133, 109, 114, 107, 105, 118, 228, 100, 156, 81, 100, 146, 109, 113, 100, 100, 103, 118, 115, 115, 114, 105, 104, 100, 100, 110, 121, 119, 120, 100, 155, 23, 100, 132, 118, 101, 114, 111, 228, 100, 156, 0, 100, 104, 101, 125, 119, 229, 100, 155, 0, 100, 104, 101, 125, 119, 229, 100, 155, 0, 100, 125, 105, 101, 118, 119, 229, 100, 155, 0, 100, 125, 105, 101, 118, 119, 228, 100, 156, 90, 100, 104, 101, 114, 103, 105, 228, 100, 156, 82, 100, 119, 112, 105, 105, 116, 100, 155, 23, 100, 102, 101, 102, 109, 105, 119, 228, 100, 156, 3, 155, 5, 155, 87, 100, 114, 105, 122, 105, 118, 100, 100, 123, 101, 111, 105, 100, 100, 121, 116, 228, 100, 159, 100, 153)
""" '''

# analyse(chars)
# analyse((153, 161, 161, 161, 161, 161, 161, 156, 0, 100, 103, 15, 120, 100, 155, 30, 155, 1, 155, 0, 100, 100, 159, 100, 159, 100, 159, 100, 159, 100, 159, 100, 159, 100, 153))

sample_text = """
                This is more like a constant feeling of being watched. There is a small passage connecting our bedroom to main hall. I have at times felt that I was being stared at by someone from the hall while we were in bedroom. The moment I try to see through the passage in to the hall, the feeling stops. But I always dismissed it on the account of me being a kind of day dreamer kind of person.
                Then I had a weird dream. In my dream, I woke up on my bed and opened my eyes while lying. I could see in the ambient light coming from the society lights, that my wife was up. She was standing in from of the mirror and just staring. She seemed to be wearing some very dark colored night gown. She had let her hair down and her hair seemed strangely puffed up. I called her name asking what are you doing? She seemed to have ignored my call. After a few seconds she silently turned and climbed back on the bed. She came next to me and sat facing me, not saying anything. I kept asking her what are you doing? why are you up so late? After some time she told me that I should go back to sleep. I went to sleep that very instant. Then I woke up again. This time I saw my wife roaming in the house, not doing anything, just roaming from here to there. Then I slept again. Third time I opened my eyes I saw my wife floating above me, starring at me and smiling. Her hair somehow not falling down due to gravity. This was it! I was creeped out enough to actually wake up from my real sleep.
                After waking up I saw my wife sleeping next to me as usual. I realized it was a scary dream. I drank some water and went back to sleep. A thought in my mind told me that it will be fun next morning when I tell her that I had a nightmare starring her.
                In morning, we got up and sat on our bed talking to each other. The nightmare I had last night was now tickling me from inside because I wanted to tell my wife that she scarred me in my dream.
                Then what happened was beyond scary for me. She started laughing and told she had a scary dream last night in which she saw me standing next to the mirror, roaming aimlessly in the house and floating above her.
                I did not know how to react. I have not told her that I had a similar nightmare as well. I thought its better to have one scarred person than two, living in a large spacious house with two bedrooms always unoccupied.
            """

secondary_text = "This is just the begining and not the end. The real part of match is going to start now dear, be ready for it. Sometimes i feel soo bad, then i think about you and i feel better. I love you so much. but then i hate you sooo hard because you are not a friend."

third_text = """

             I met Mohit when I stopped at that dingy gas station, half a kilometer south of the last town. He was a jolly fellow, in his late twenties. The next town was nearly 50 miles away and he was in dire need of a lift, and offered to pay half of my gas bill. He looked like a decent guy, and I was short on cash. So, I thought why not!
            He immediately struck up a conversation with me. He told me that he worked at a firm a couple of towns away, and he traveled about once a month to meet his girlfriend. Soon, the conversation was in full flow, twisting and turning around various topics, just like the bends on the road. He was an avid reader, a die hard cricket fan, and madly passionate about movies, just like me.
            Suddenly, with another sharp twist in the road, my headlight fell on a shabbily dressed man, standing about a hundred meters down the road, waving wildly for a lift. I had almost applied the brakes, when Mohit said, in a very serious tone, "Dude, what are you doing!!! Didn't you hear the news? Keep going. Do not stop."
            Something in his voice made me hit the gas pedal instead of brakes. I saw the silhoutte of the hitchhiker whirring past us, as I sped full throttle. Soon, he was nothing but a distant shadow in the rear view mirror.
            My grip on the steering relaxed a bit. I turned towards Mohit. His face was still white, his expression ghastly.
            "Dude relax, and what fucking news are you talking about?" I shot at him, uneasily.
            There was still a tinge of fear in his tone when he replied - "Dude, I just read it today. This 30 km stretch that we are on right now is very infamous for a serial killer who lurks here after dark. There have been 3 murders in past couple of months. The reports say that he pretends to be a hitchhiker and signals passing cars for lift. If they are stupid enough to stop and let him in, ..." he let his words hang.
            Then, he pulled out his cell, googled something, and then shoved it in my face.
            What I saw sent chills up and down my spine. A few pics, one of a girl, her head smashed in with what could only have been a crowbar, her neck bent at a very strange angle, another one of a couple, both stabbed multiple times in the heart and again, their necks broken, blood splattered everywhere, the corpses still left in the car to rot.
            As I scrolled through the pictures, the realization now hit me with full force. I already had a hitchhiker in the car! I looked up from the phone.
            Mohit was staring at me. His expression had changed. Gone was the ghastly expression. There was a sudden gleam in his eyes, a gleam that only comes from knowledge of how the future is about to unfold.
            This is it. This is how it's going to end. Maybe, I should stall?
            I uttered, slowly - "But why hasn't police been able to catch him, this killer? Apparently, he's been doing it for a couple of months now. He has a pretty obvious modus operandi. Pretending to be a hitchhiker, flagging down cars, and gutting their owners. He must live somewhere close."
            Mohit replied - "Dunno". His tone was neutral, dangerously so.
            I had to act confident. I looked directly into his eyes - "I have a theory. Would you like to hear it?"
            He stared back at me. By now, we both knew that this was just wordplay. Soon it would end and then, the real horror would begin. We both realized that there was no escape from it. And we both had made peace with it. I knew I had.
            "Sure, go ahead ", he smiled.
            "Maybe the reason police haven't been able to catch this serial killer is because they have got it all wrong. Maybe, the killer is not the hitchhiker. Maybe he is the driver!!! The killer steals a car and drives along this road. When he sees anyone stranded on the roadside, he offers them lift. And once they get into the car, ..." .
            In one swift motion, I took out the dagger hidden carefully besides my seat and plunged it right into his heart. He gasped, his eyes wide in shock. Then slowly, I twisted the dagger. I felt life draining from his body, which was still convulsing violently. Once again, I felt that power, surging through my veins. The same power I had felt, when I had mutilated the half dead bodies of that girl, and that married couple. The power that made me God, the destroyer.
            I smiled in satisfaction. This one was not like the others. When I saw that change in his expression earlier, the gleam in his eyes, I knew he had understood who I was. Pretty intuitive, eh! But somehow, that made it even more fun - to play with him, before gutting him. Poor Mohit. Trapped like a rat who knows the cat is just playing with it before going for the kill!
            I slowed down the car and parked it on the roadside. It was pitch black. I got out and carefully shifted Mohit's, now lifeless body to the driver's side. Then I wrapped my ice cold fingers around his limp neck. As my hand jerked, I heard a crunching sound.
            It was the sound of a neck snapping.

        """
# bytecode(third_text)
data = read('second_story.png')
analyse(data)