#  Algorithm for String compression (e.g  'aaaabbbccccd' => 'a4b3c4d')

def str_comp(string):
    j=''
    cnt=1
    output=''                      # initialization
    for i in string:
        temp=i
        if j == temp:             # if we are on repeating character? 
            cnt += 1
            output =output[:-1]+str(cnt) # keep updating last char
        else:                    
            cnt=1
            j=temp
            output =output+j+str(cnt)
        
    print(output.replace('1',''))

str_comp('aaabdcfffff')
