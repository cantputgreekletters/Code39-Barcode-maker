from PIL import Image  
global pos

# function that creates a line on the image of the color that is given (in this case it's only black)
def line(Width : int = 1):
    global pos
    Width_ = Width
    color = (0,0,0) # = Black
    Width += pos
    for width in range(pos,Width):
        for height in range(150,251):
            img.putpixel((width,height),color) #(pos.x,pos.y),(colorR,colorG,colorB)
    pos += Width_

# Special Encoding to create the lines on the image, each number corresponds to a line
# Might replace Encoding with a formula that I believe exists which usies a character's ASCII value
def EncodeCharacter(C:str):
    #1 = Black Thin
    #2 = Black Wide
    #3 = White Thin
    #4 = White Wide
    D = {
        "A":"231314132",
        "B":"132314132",
        "C":"232314131",
        "D":"131324132",
        "E":"231324131",
        "F":"132324131",
        "G":"131314232",
        "H":"231314231",
        "I":"132314231",
        "J":"131324231",
        "K":"231313142",
        "L":"132313142",
        "M":"232313141",
        "N":"131323142",
        "O":"231323141",
        "P":"132323141",
        "Q":"131313242",
        "R":"231313241",
        "S":"132313241",
        "T":"131323241",
        "U":"241313132",
        "V":"142313132",
        "W":"242313131",
        "X":"141323132",
        "Y":"241323131",
        "Z":"142323131",
        "0":"131423231",
        "1":"231413132",
        "2":"132413132",
        "3":"232413131",
        "4":"131423132",
        "5":"231423131",
        "6":"132423131",
        "7":"131413232",
        "8":"231413231",
        "9":"132413231",
        " ":"142313231",
        "-":"141313232",
        "$":"141414131",
        "%":"131414141",
        ".":"241313231",
        "/":"141413141",
        "+":"141314141",
        "*":"141323231"
    }
    return D.get(C)

# Decode the number to a line  
def NumToLine(n,i):
    global pos
    n = int(n)
    thin = 2
    wide = 4
    if i == 1:
        line(thin,"white")
    if n == 1:
        line(thin)
    elif n == 2:
        line(wide)
    elif n == 3:
        pos += thin
    elif n == 4:
        pos += wide

#Input from the user
text = str(input("Give text\n"))

#For checking reasons 
alphabet_lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_upper = list(map(lambda x:x.upper(),alphabet_lower))
characters = [" ","-","$","%",".","/","+","*"]
numbers = [str(i) for i in range(10)]

#Adds a star as the first character because every barcode starts and ends with a star
Text = "*"
#Makes lower case character upper case
for i in text:
    if i in alphabet_lower:
        Text = Text + i.upper()
    else:
        Text = Text + i
#==================
del text
#Raises an error if there is an invalid character
for i in Text:
    if i not in characters and i not in alphabet_upper and i not in numbers:
        raise Exception("Invalid character")
#============================

#Adds a star as the last character because every barcode starts and ends with a star
Text = Text + "*"
pos = 10
#Adjusts the picture's width depending on the text's length
image_width = (len(Text)) * 30
#Image height is static
image_height = 400

img  = Image.new( mode = "RGB", size = (image_width, image_height),color=(255,255,255) )

#Creates the image
for i in Text:
    Index = 0
    for j in EncodeCharacter(i):    
        Index += 1
        NumToLine(j,Index)

#Shows the image
img.show()