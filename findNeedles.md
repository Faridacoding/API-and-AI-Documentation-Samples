
# findNeedles API documentation

## Summary

find_Needles() is a Python function used to search a given input character or string in an array of strings. This function can be used for character search use cases.


## Pre-requisites

find_Needles() has 2 dependencies.

1. Regex library (re)

2. Python sys module (sys)

```
import re
import sys
```


## Packages and Environment

- Atom Editor Environment

- <code>platformio-ide-terminal</code>
    - Python package for Atom


- <code>Script</code>
    - Package used for executing Python commands



## Source code

```
#Import dependencies
import re
import sys

#findNeedles Function
def findNeedles(haystack, needlesArr):

    # Check for character length >5
    if len(needlesArr) > 5:
        sys.stderr.write('Too many words!')

    else:
        # Count the character and create a list for user
        countArray = [0]*len(needlesArr)

        # Convert
        for i in range(len(needlesArr)):
            words = re.split("[ \"\'\t\n\b\f\r]", haystack)

            for j in range(len(words)):
                if words[j] == needlesArr[i]:
                    countArray[i] += 1

        for j in range(len(needlesArr)):
            print (needlesArr[j] + ": " + str(countArray[j]))

```


### Big O Notation

> **- Time Complexity**
>
>
> **- Space Complexity**


## Limitations

findNeedles() can find characters only upto 5 characters in length. Characters above 5 with throw an error prompt.


## Sample input


## Sample output
