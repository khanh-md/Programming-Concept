# Programming pair: Elizabeth Franklin (U67587808) and Khanh Dong (U14837275)
# Driver: Khanh Dong
# Navigator: Elizabeth Franklin
# Description: The file convert a text file into a new encrypted text file.


encrypt_code =  {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8', 
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5', 
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2', 
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y', 
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v', 
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s', 
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p', 
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m', 
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j', 
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g', 
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d', 
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a', 
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<', 
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=', 
        '{':'[','[':'{','}':']',']':'}'} 

def main():
    text = open(input("Enter the name of the text file: "), 'r')
    contents = text.read()
    text.close()
    enc_text = ''
    for letter in contents:
        if letter.isspace() == True:
            enc_text += ' '
        if letter.isspace() == False:
            new_letter = encrypt_code[letter]
            enc_text += new_letter
    return enc_text

encrypted = input('Enter the name of the new file: ')
new_enc = open(encrypted, 'w')
new_enc.write(main())
new_enc.close()