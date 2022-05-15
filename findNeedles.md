
# findNeedles API documentation

## Summary

findNeedles() is a Python function used to search an user input character or string in an array of strings. This function can be used for character search use cases.


## Packages and Environment

- Atom Editor Environment

- <code>platformio-ide-terminal</code>
    - Python package for Atom


- <code>Script</code>
    - Package used for executing Python commands



## Pre-requisites

findNeedles() has 2 dependencies.

1. Regex library (re)

2. Python sys module (sys)

```
import re
import sys

```

## Parameters

There are 2 parameters defined in findNeedles API

```
def findNeedles(haystack, needlesArr)

```

- haystack : is the given group of characters/strings array

- needlesArr : is the user input character/string that should be searched in the haystack array.


## Limitations

- <code>findNeedles()</code> can find only up to 5 characters in length. Characters above 5 will throw an error prompt.

```
if len(needlesArr) > 5:        
    sys.stderr.write('Too many words!')

```

## Convert <code>needlesArr</code> into an array

- This code counts the length of <code>needlesArr</code> string and converts the user input string into a character array.

```
else:
    countArray = [0]*len(needlesArr)

```

## Convert <code>haystack</code> to an array

- This code splits and converts the entire <code>haystack</code> string into a string array based on the defined regex pattern.

- The results of the string split into characters are stored in <code>words</code> array

```

for i in range(len(needlesArr)):
    words = re.split("[ \"\'\t\n\b\f\r]", haystack)
```

## Search for <code>needlesArr</code> words in <code>haystack</code> array

- This code checks if the user input string <code>needlesArr</code> is present in the <code>words</code> array.

- If the string is found the counter is incremented by 1.

```
for j in range(len(words)):
    if words[j] == needlesArr[i]:
        countArray[i] += 1
```

## Print the number of occurrences found

- This code prints the number of <code>needlesArr</code> occurrences found in the <code>haystack</code> array.

```
for j in range(len(needlesArr)):
    print (needlesArr[j] + ": " + str(countArray[j]))

```


## Sample input

```
main_haystack= 'f a r i f i n d farida far 23'
needles='far 1'
```

## Execution

- Function Call

```
findNeedles(main_haystack,needles)

```



## Sample output

<!--
<img src = "../API-Documentation-Samples/findNeedles_output.jpg" width ="300">
-->

![](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/findNeedles_output.jpg)


## Big O Notation

**Time Complexity:**

- Time taken to execute this function is **0.086 seconds.**


**Space Complexity**

- !! TBD - Need inputs from SME  !!



## Source code

```
import re   
import sys

def findNeedles(haystack, needlesArr):    

    if len(needlesArr) > 5:        
        sys.stderr.write('Too many words!')

    else:
        countArray = [0]*len(needlesArr)   

        for i in range(len(needlesArr)):
            words = re.split("[ \"\'\t\n\b\f\r]", haystack)

            for j in range(len(words)):
                if words[j] == needlesArr[i]:
                    countArray[i] += 1

        for j in range(len(needlesArr)):
            print (needlesArr[j] + ": " + str(countArray[j]))

```

---


<code>Callout from Technical Writer to SME:</code>


1. Can the <code>countArray</code> ("Convert <code>needlesArr</code> into an array" section) be modified to include character array and string array?

    > For Example:
    >
    >
    > Input String <code>'far'</code> is converted to both
    >
    >
    > - <code>['f' 'a' 'r']</code> character list and,
    >
    >
    > - <code>['far']</code> string array.
    >
    >

  If this is out of scope, then kindly ignore this comment.

2. More information on string pattern extraction  using Regex is required for the code shown below.

    > ```re.split("[ \"\'\t\n\b\f\r]", haystack)```

3. More information on **"Space Complexity"** for future improvements is required. **Big O notation** formula for Space Complexity is needed.

# [](#displayline)

This draft documentation is ready to be reviewed. Content will be updated and published after more information is received.
