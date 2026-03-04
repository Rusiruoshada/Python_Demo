stringText = """
    we can use \"\"\"<text> \"\"\" to do multi line string. also this can be.
    we use \\ as a escape character
    comment can do by using #.
    string concatenation done by +. it can use for addition too
"""
print(stringText)

exampleText = 'this is a string!'
# slicing ->
# string index start from 0 and when we gave a range its start from 0 if we gave negative values
print(exampleText[2]) # output : i
print(exampleText[:6]) # output :this i
print(exampleText[3:]) # output : s is a string!
print(exampleText[-3]) # output : n
print(exampleText[-1:-4]) # output : no input
print(exampleText[-2:4]) # output : no input
print(exampleText[2:-4]) # output : is is a str

