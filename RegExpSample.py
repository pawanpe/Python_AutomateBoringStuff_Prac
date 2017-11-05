import re

def NumberOfProfessionals():
    lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds'
    xmasReg = re.compile(r'\d+\s\w+')

    print(xmasReg.findall(lyrics))

    vowelRegex = re.compile(r'[aeiouAEIOU]')
    print(vowelRegex.findall('this is a test for vowel regex'))

    vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
    print(vowelRegex.findall('this is a test for vowel regex'))


    vowelRegex = re.compile(r'[^aeiouAEIOU]')
    # or vowelRegex = re.compile(r'[^aeiou]', re.I) # case insensitive
    print(vowelRegex.findall('this is a test for vowel regex'))

def BeginEnd():
    begingsWithHelloRegex = re.compile(r'^Hello')
    print(begingsWithHelloRegex.search('Hello there!'))

    endsWithHelloRegex = re.compile(r'there!$')
    print(endsWithHelloRegex.search('Hello there!'))

    allDigits = re.compile(r'^\d+$')
    print(allDigits.search('23493423094bqq4uq234324'))

    allDigits = re.compile(r'\d+$')
    print(allDigits.search('23493423094bqq4uq323423'))

NumberOfProfessionals()
BeginEnd()