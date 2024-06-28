import random
import urllib.request
def handle_response(message) -> str:    #handle responses
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello there!'
    
    if p_message == 'roll d20':
        return str(random.randint(1,20))
    
    if p_message == 'help':
        return "You can type the following commands in: hello; tryout name,pronoun; gay, crazy or wiki sexuality/genderidentity"
    
    name = dadjoke(p_message) 
    if (name != ""):
        return "Hello" + name + ". I'm a bot"
    
    if p_message.startswith("try out"):
        if include(p_message,","):
            return tryout2(message[8::])
        return tryout1(message[8::])
    
    if p_message.startswith("am i gay") or p_message.startswith("gay"):
        return "yes"
    
    if include(p_message, "crazy"):
        return crazy()
    
    if (p_message.startswith("wiki")):
        return wiki(message[5::])
    
    if (p_message.startswith("lamp")):
        return "LAMP"
    
    if (p_message.startswith("form")):
        return "DO THE FORM"
    
    if (p_message.startswith("thinking bee")):
        erg = ""
        for i in range (0, 20):
            erg = erg + "THINKING BEE \n"
        return erg
    

def dadjoke(message) -> str: 
    name = ""
    search1 = "i'm"
    search2 = "im"
    search3 = "i am"
    name = search(message,search1)
    if name == "":
        name = search(message, search2)
    if name == "":
        name = search(message, search3)
    return name

def search(message, search) -> str: #search methid for dadjoke()
    name = ""
    j = 0
    for i in range (0,len(message)): 
        if j == len(search):
            name = name + message[i]
            
        elif message[i] == search[j]: 
            j = j +1
        else:
            j = 0
    return name

def tryout1(name) -> str:   #tryout names
    ausgabe = options(name,"", random.randint(0,4))
    return ausgabe

def tryout2(message) -> str:
    name = ""
    i = 0
    while (message[i] != ','):
        name = name +message[i]
        i = i+1
    pronoun = message[i+1::]
    return options(name, pronoun, random.randint(0,3))



def options(name,pronoun, zahl): 
    if pronoun == "":
        pronoun = name
    verb = "is"
    verb2 = "has"
    if pronoun == "they" or pronoun == " they":
        verb = "are"
        verb2 = "have"

    ausgabe = [f"Have you seen {name}? I've been searching for {name} for hours now. {pronoun} just kinda disappeared right before my eyes. No? Dang it! Thanks anyways! Where are you {name}? {name.upper()}??",
               f"You know {name} too? Oh my god! I like {name} so much! {pronoun} really {verb} great!",
               f"Today I went to get ice cream with {name}. It was so fun! {pronoun} {verb} just such a fun person! {name}'s favourite ice-cream is a mix of all of them",
               f"{name.upper()} I have a question for you! What's your favorite song at the moment? I really need new music to listen to and you know what they say, if you need someone with great music taste, ask {name}. {pronoun} {verb2} the best recs!",
               f"Nice to meet you {name}! {name} is such a cool name! I'd love to get to know you more!"]
    return ausgabe[zahl]

def crazy() -> str:
    amount = random.randint(1,8)
    ausgabe = ""
    for i in range(0,amount):
        ausgabe = ausgabe + "Crazy? I was crazy once. They put me in a room. A rubber room. A rubber room with rats. And rats make me crazy. "
    return ausgabe 

def include(message,pattern):   
    j = 0
    for i in range (0, len(message)-len(pattern)+1):
        while (message[i+j] == pattern[j]):
            j = j +1
            if j == len(pattern):
                return True
    return False


def wiki(search): #search lgtbq wiki for definition
    url = "https://lgbtqia.fandom.com/wiki/"+search
    page = urllib.request.urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    # for debugging and looking at the html code
    #with open("insert pathToTxtFile","a",encoding = "utf-8") as datei:
        #datei.write(html)
    # Websites change: this code might not work in the future
    start_index = html.find("""</aside>""")
    print(start_index)
    end_index = html.find("""<div id="toc" class="toc" role="navigation" aria-labelledby="mw-toc-heading">""")
    print(end_index)
    text = html[start_index:end_index]
    text = removeSigns(text)
    text = removeNumbers(text)
    return text

def removeSigns(text):
    newText = ""
    notWrite = False
    for i in text:
        if i == '<' or i == '&' or i == '#':
            notWrite = True
        if notWrite == False: 
            newText += i
        if i == '>' or i == ';':
            notWrite = False
    return newText

def removeNumbers(text):
    newText =""
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for i in text: 
        if i not in numbers: 
            newText = newText + i
    return newText
