import re

from map.ko_braile_map import *
from map.ko_braille_map_ASCII import *

Symbol_CODE=33

Upper_CODE=65
Lower_CODE=97

BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

LowerCase_List=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

UpperCase_List=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


Abbreviation_List = ["그래서", "그러나", "그러면", "그러므로", "그런데", "그리고", "그리하여"]

Abb_jungjongsung_List = ["ㅓㄱ", "ㅓㄴ", "ㅓㄹ", "ㅕㄴ", "ㅕㄹ", "ㅕㅇ", "ㅗㄱ",
                                  "ㅗㄴ", "ㅗㅇ", "ㅜㄴ", "ㅜㄹ", 'ㅡㄴ', "ㅡㄹ", "ㅣㄴ", "것"]

Abb_chosung_List = ['가', '까', '나', '다', '따', '라', '마', '바', '빠', '사', '싸', '아', '자', '짜', '차', '카', '타', '파', '하']


def ko_braile_convertor(sentence):
    #sentence = sentence.replace(" ", "/")
    # 어절 단위로 약어 처리
    for word in Abbreviation_List:  # sentence 내용 중 약어 리스트 안에 있는 단어가 있는지
        index = -1
        while True:
            index = sentence.find(word, index+1)  # sentence 안에 약어가 있다면 그 단어의 첫번째 인덱스를 저장
            if index == -1:
                break
            # 약어 앞에 문장부호나 공백 외의 단어가 있을 경우에는 줄여 쓰지 않으므로 그것을 검사 (ex. 쭈그리고, 찡그리고 등)
            if (index == 0 or sentence[index - 1] is "/" or
                    sentence[index - 1] is '\n' or sentence[index - 1] is "." or
                    sentence[index - 1] is "," or sentence[index - 1] is "!" or
                    sentence[index - 1] is "?" or sentence[index - 1] is "~"):
                sentence = sentence.replace(word, map_abbreviation_word[word], 1)

    split_keyword_list = list(sentence)  # 원문장 출력부분

    print("음절 분할 어절 : ")
    print(split_keyword_list)

    result = list()

    for i, keyword in enumerate(split_keyword_list):

        # 한글 여부 check 후 분리
        if re.match('[ㄱ-ㅎ]', keyword) is not None:
            result.append('='+map_chosung[keyword])
        elif re.match('[ㅏ-ㅣ]', keyword) is not None:
            result.append('='+map_jungsung[keyword])
        elif re.match('[가-힣]', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            if keyword in ['성', '썽', '정', '쩡', '청']:
                result.append(map_chosung[CHOSUNG_LIST[char1]])
                result.append(map_jungjongsung_abbreviation['ㅕㅇ'])
            elif keyword == '것':
                result.append(map_jungjongsung_abbreviation[keyword])
            elif (JUNGSUNG_LIST[char2]+JONGSUNG_LIST[char3]) in Abb_jungjongsung_List:
                result.append(map_chosung[CHOSUNG_LIST[char1]])
                result.append(map_jungjongsung_abbreviation[JUNGSUNG_LIST[char2]+JONGSUNG_LIST[char3]])
            elif (JUNGSUNG_LIST[char2] == 'ㅏ'):
                result.append(map_abbreviation[Abb_chosung_List[char1]])
                result.append(map_jongsung[JONGSUNG_LIST[char3]])
            elif CHOSUNG_LIST[char1] == 'ㅇ':
                result.append(map_jungsung[JUNGSUNG_LIST[char2]])
                result.append(map_jongsung[JONGSUNG_LIST[char3]])
            elif JONGSUNG_LIST[char3] == ' ' and i+1 < len(split_keyword_list):
                if re.match('[예-옣]', split_keyword_list[i+1]) is not None:
                    result.append(map_chosung[CHOSUNG_LIST[char1]])
                    result.append(map_jungsung[JUNGSUNG_LIST[char2]])
                    result.append(map_jongsung[JONGSUNG_LIST[char3]])
                    result.append('-')
            elif JUNGSUNG_LIST[char2] in ['ㅑ', 'ㅘ', 'ㅜ', 'ㅝ'] and i < len(split_keyword_list):
                if re.match('[애-앻]', split_keyword_list[i+1]) is not None:
                    result.append(map_chosung[CHOSUNG_LIST[char1]])
                    result.append(map_jungsung[JUNGSUNG_LIST[char2]])
                    result.append(map_jongsung[JONGSUNG_LIST[char3]])
                    result.append('-')
            else:
                result.append(map_chosung[CHOSUNG_LIST[char1]])
                result.append(map_jungsung[JUNGSUNG_LIST[char2]])
                result.append(map_jongsung[JONGSUNG_LIST[char3]])

        elif re.match('[0-9]', keyword) is not None:
            if len(split_keyword_list) == 1 or \
                    (re.match('[0-9]', split_keyword_list[i-1]) is None and split_keyword_list[i-1] != ","
                     and re.match('[0-9]', split_keyword_list[i+1]) is not None)\
                    or i == 0:
                result.append('#')
            result.append(map_number[int(keyword)])

        elif re.match('[A-Z]',keyword) is not None:
            char_code1=ord(keyword)-Upper_CODE
            charA = int(char_code1)
            result.append(map_UpperCase[UpperCase_List[charA]])

        elif re.match('[a-z]', keyword) is not None:
            char_code2 = ord(keyword) - Lower_CODE
            charB = int(char_code2)
            result.append(map_LowerCase[LowerCase_List[charB]])

        elif re.match('[^ \t\n\r\f\v a-zA-Z0-9]', keyword) is not None:
            # 숫자의 자릿수를 표시하는 ,는 1로 표시하므로 앞뒤가 숫자이면 1로 변경
            if re.match(',', keyword) is not None \
                    and re.match('[0-9]', split_keyword_list[i-1]) is not None \
                    and re.match('#', split_keyword_list[i+1]) is not None:
                result.append("1")
            else:
                #char_code3=ord(keyword) - Symbol_CODE
                #charS = int(char_code3)
                result.append(map_Symbol[keyword])

        else:
            result.append(keyword)


    result = "".join(result)
    #result = result.replace(" ", "")
    #result = result.replace("/", " ")

    # result
    return result


def convertor(sentence):
    # 어절 분할
    print("원문장 : "+sentence)
    word_list = sentence.split()
    print("어절 분할 문장: ")
    print(word_list)
    temp_list = list()
    for word in word_list:
        word_mod = word.replace(word, ko_braile_convertor(word))
        temp_list.append(word_mod)
    word_list = temp_list
    print("convertor 수행 후 : ")
    print(word_list)

    word_list = "".join(word_list)
    word_list = word_list.replace(" ", "")
    word_list = word_list.replace("/", " ")
    return word_list


if __name__ == '__main__':
    result = ko_braile_convertor("")
    print(result)






