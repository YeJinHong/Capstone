from collections import defaultdict


# 약어 - 라, 아, 차는 약어가 없으므로 풀어쓴 문자로 대체
#'아'에서 ㅇ은 적지않는게 일반적 (아 = '7<', '<')
# 나, 다, 마, 바, 자, 카, 타, 파, 하 + 모음 = 'ㅏ'생략하지 않음
# 다만 줄이 바뀌때에는 'ㅏ'를 생략함
# 된소리 앞에 된소리표 추가
temp_abbreviation = ['가', '까', '나', '다', '따', '라', '마', '바', '빠', '사', '싸', '아', '자', '짜', '차', '카', '타', '파', '하']
temp_abbreviation_B = ['$', ',$', 'C', 'I', ',I', '"<', 'E', '^', ',^', 'L', ',L', '<', '.', ';<', ',;<', 'F', 'H', 'D', 'J']


#성, 썽, 정, 쩡, 청 = ㅅ,ㅆ,ㅈ,ㅉ,ㅊ +ㅕㅇ약자
temp_abbreviation_jungjongsung = ["ㅓㄱ", "ㅓㄴ", "ㅓㄹ", "ㅕㄴ", "ㅕㄹ", "ㅕㅇ", "ㅗㄱ",
                                  "ㅗㄴ", "ㅗㅇ", "ㅜㄴ", "ㅜㄹ", 'ㅡㄴ', "ㅡㄹ", "ㅣㄴ", "것"]
temp_abbreviation_jungjongsung_B = ['?', ')', 'T', '*', '\\', ']', 'X', '(', '=', 'G', '&', 'Z', '!', 'Q', '_S']

#앞음절-약어 사용, 뒷음절-약어 미사용
temp_abbreviation_word = ["그래서", "그러나", "그러면", "그러므로", "그런데", "그리고", "그리하여"]
temp_abbreviation_word_B = ["AS", "AC", "A3", "A5", "AN", "AU", "A:"]


map_abbreviation = defaultdict()
map_jungjongsung_abbreviation = defaultdict()

for idx, abb in enumerate(temp_abbreviation):
    map_abbreviation[abb]=temp_abbreviation_B[idx]

for idx, j_abb in enumerate(temp_abbreviation_jungjongsung):
    map_jungjongsung_abbreviation[j_abb] = temp_abbreviation_jungjongsung_B[idx]