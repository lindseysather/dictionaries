
def main():
    
    codes = {'a':'!', 'b':'@', 'c':'#', 'd':'$', 'e':'%', 'f':'^',
    'g':'&', 'h':'*', 'i':'(', 'j':')', 'k':'_', 'l':'-', 'm':'+',
    'n':'=', 'o':'~', 'p':'`', 'q':'{', 'r':'}', 's':'[', 't':']',
    'u':'|', 'v':':', 'w':';', 'x':'<', 'y':'>', 'z':'?'}

    infile = open('info_security.txt', 'r')
    outfile = open('encrypted_file.txt', 'w')

    file_contents = infile.read()

    for x in file_contents:
        if x.isalpha():
            z = x.lower()
            outfile.write(z.replace(z, codes[z]))
        else:
            outfile.write(x)

main()