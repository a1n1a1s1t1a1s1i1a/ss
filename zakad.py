def encode_to_morse(text):
    global a_1
    a_1 = {}
    a = ""
    morse = '''
    A,.-
    B,-...
    W,.--
    G,--.
    D,-..
    E,.
    V,...-
    Z,--..
    I,..
    J,.---
    K,-.-
    L,.-..
    M,--
    N,-.
    O,---
    P,.--.
    R,.-.
    S,...
    T,-
    U,..-
    F,..-.
    H,....
    C,-.-.
    ö,---.
    ch,----
    Q,--.-
    X,-..-
    Y,-.--
    é,..-..
    ü,..--
    ä,.-.-
    1,.----
    2,..---
    3,...--
    4,....-
    5,.....
    6,-....
    7,--...
    8,---..
    9,----.
    0,-----
    .,......
    comma,.-.-.-
    /,-..-.
    ?,..--..
    !,--..--
     ,-...-
    error,........
    @, .--.-.'''
    morse = morse.split("\n")
    for el in morse:
        a_1[el[4:el.find(",")]] = el[el.find(",") + 1:]
    for word in text:
        word = word.upper()
        a += a_1[word]
    return a















