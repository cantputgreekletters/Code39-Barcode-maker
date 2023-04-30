from PIL import Image  
global pos
def line(Width : int = 1 ,color = "black"):
    global pos
    Width_ = Width
    if color == "white":
        color = (255,255,255)
    else:
        color = (0,0,0)
    Width += pos
    for width in range(pos,Width):
        for height in range(150,251):
            img.putpixel((width,height),color) #(pos.x,pos.y),(colorR,colorG,colorB
    pos += Width_
    
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
    
def NumToLine(n,i):
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
        line(thin,"white")
    elif n == 4:
        line(wide,"white")


def star():
    
    #first space
    line(2,"white")
    # -----
    line(2)
    line(4,"white")
    line(2)
    line(2,"white")
    line(4)
    line(2,"white")
    line(4)
    line(2,"white")
    line(2)
text = str(input("Give text\n"))
alphabet_lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_upper = list(map(lambda x:x.upper(),alphabet_lower))
characters = [" ","-","$","%",".","/","+","*"]
numbers = [str(i) for i in range(10)]
Text = "*"
for i in text:
    if i in alphabet_lower:
        Text = Text + i.upper()
    else:
        Text = Text + i
del text
for i in Text:
    if i not in characters and i not in alphabet_upper and i not in numbers:
        raise Exception("Invalid character")
Text = Text + "*"
pos = 10
image_width = (len(Text)) * 30
image_height = 400

img  = Image.new( mode = "RGB", size = (image_width, image_height),color=(255,255,255) )

for i in Text:
    Index = 0
    for j in EncodeCharacter(i):    
        Index += 1
        NumToLine(j,Index)

img.show()

