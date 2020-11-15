# EntropyCalculator
Recreating Shannon's experiment on Romanian language to find it's entropy

### Documentation
*Entropy and Redundancy in English* [Link](https://cs.stanford.edu/people/eroberts/courses/soco/projects/1999-00/information-theory/entropy_of_english_9.html)

*Prediction and Entropy of printed English* [Link](https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf)

*Entropy Formula* [Link](https://rosettacode.org/wiki/Entropy)


### How it works?

The program loads the text from the *.docx* file, counts the letters using a dictionary (ignore cases included) and applies the entropy formula.

### Results

```
4.138825064085823 -> groups of 1
4.203439927000855 -> groups of 2
3.8524560238133767 -> groups of 3
3.45292692639294 -> groups of 4
3.095140822500855 -> groups of 5
2.780363150734319 -> groups of 6
2.5066994397329236 -> groups of 7
2.273232653402789 -> groups of 8
2.0701024646971957 -> groups of 9
1.8995542006029116 -> groups of 10
```

### Language used

Python, Ruby
