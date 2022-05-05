import re
import sys

def findNeedles(haystack, needlesArr):
    print (type(needlesArr))
    if len(needlesArr) > 5:
        sys.stderr.write('Too many words!')
    else:
        countArray = [0]*len(needlesArr) # creating list with len(needlesArr)
        print('countArray',type(countArray))
        for i in range(len(needlesArr)):
            words = re.split("[ \"\'\t\n\b\f\r]", haystack)
            print ('words', words)
            word_len= len(words)
            print('word_len',word_len)

            for j in range(len(words)):
                if words[j] == needlesArr[i]:
                    countArray[i] += 1

        for j in range(len(needlesArr)):
            print (needlesArr[j] + ": " + str(countArray[j]))


main_haystack= 'f a r i f i n d farida far'
needles='far f'
findNeedles(main_haystack,needles)
