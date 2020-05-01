import re

from map.ko_braile_map import *


Upper_CODE=65
Lower_CODE=97

BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

LowerCase_List=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

UpperCase_List=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def ko_braile_convertor(sentence):
    sentence = sentence.replace(" ", "/")


    split_keyword_list = list(sentence) #원문장 출력부분

    # print(split_keyword_list)


    result = list()
    for keyword in split_keyword_list:
        # 한글 여부 check 후 분리
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result.append(map_chosung[CHOSUNG_LIST[char1]])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result.append(map_jungsung[JUNGSUNG_LIST[char2]])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            result.append(map_jongsung[JONGSUNG_LIST[char3]])

        elif re.match('[0-9]', keyword) is not None:
            result.append(map_number[int(keyword)])


        elif re.match('[A-Z]',keyword) is not None:
            char_code1=ord(keyword)-Upper_CODE
            charA = int(char_code1)
            result.append(map_UpperCase[UpperCase_List[charA]])

        elif re.match('[a-z]', keyword) is not None:
            char_code2 = ord(keyword) - Lower_CODE
            charB = int(char_code2)
            result.append(map_LowerCase[LowerCase_List[charB]])



        else:
            result.append(keyword)


    result = "".join(result)
    result = result.replace(" ", "")
    result = result.replace("/", " ")


    # result
    return result


'''if __name__ == '__main__':
    Inputtext = TableWidget.text

    result= ko_braile_convertor(Inputtext)
    return result'''






