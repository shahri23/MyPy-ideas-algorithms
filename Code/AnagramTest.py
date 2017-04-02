# Are two strings anagrams? SILENT/LISTEN or LISten/SilENT or LIS ten/sile nt
# strategy:lower all, sort, remove spaces if any

def anagramTest (str1, str2):
    if sorted(str1.replace(" ","").lower()) == sorted(str2.replace(" ","").lower()):
        print('True')
    else:
        print('False')
        
anagramTest('liste              n','  si LE nt')
