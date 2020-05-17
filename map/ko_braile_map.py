from collections import defaultdict


temp_chosung = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ","ㄲ","ㄸ","ㅃ","ㅆ","ㅉ"]
temp_chosung_B = [chr(int('2808',16)),chr(int('2809',16)),chr(int('280A',16)),chr(int('2810',16)),chr(int('2811',16)),
                  chr(int('2818',16)),chr(int('2820',16)),chr(int('281B',16)),chr(int('2828',16)),chr(int('2830',16)),
                  chr(int('280B',16)),chr(int('2813',16)),chr(int('2819',16)),chr(int('281A',16)),
                  "".join([chr(int('2820',16)),chr(int('2808',16))]),
                  "".join([chr(int('2820',16)),chr(int('280A',16))]),
                  "".join([chr(int('2820',16)),chr(int('2818',16))]),
                  "".join([chr(int('2820',16)),chr(int('2820',16))]),
                  "".join([chr(int('2820',16)),chr(int('2828',16))])]

temp_jungsung = ["ㅏ","ㅑ","ㅓ","ㅕ","ㅗ","ㅛ","ㅜ","ㅠ","ㅡ","ㅣ","ㅐ","ㅒ","ㅔ","ㅖ","ㅘ","ㅙ","ㅚ","ㅝ","ㅞ","ㅟ","ㅢ"]
temp_jungsung_B = [chr(int('2823',16)),chr(int('281C',16)),chr(int('280E',16)),chr(int('2831',16)),chr(int('2825',16)),
                   chr(int('282C',16)),chr(int('280D',16)),chr(int('2829',16)),chr(int('282A',16)),chr(int('2815',16)),chr(int('2817',16)),
                   "".join([chr(int('281C',16)),chr(int('2817',16))]),
                   chr(int('281D',16)),
                   chr(int('280C',16)),
                   chr(int('2827',16)),
                   "".join([chr(int('2827',16)),chr(int('2817',16))]),
                   chr(int('283D',16)),
                   chr(int('280F',16)),
                   "".join([chr(int('280F',16)),chr(int('2817',16))]),
                   "".join([chr(int('280D',16)),chr(int('2817',16))]),
                   chr(int('283A',16))]

temp_jongsung = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ", "ㄳ","ㄵ","ㄶ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅄ","ㄲ","ㅆ"]
temp_jongsung_B = [chr(int('2801',16)),
                   chr(int('2812',16)),
                   chr(int('2814',16)),
                   chr(int('2802',16)),
                   chr(int('2822',16)),
                   chr(int('2803',16)),
                   chr(int('2804',16)),
                   chr(int('2836',16)),
                   chr(int('2805',16)),
                   chr(int('2806',16)),
                   chr(int('2816',16)),
                   chr(int('2826',16)),
                   chr(int('2832',16)),
                   chr(int('2834',16)),
                   "".join([chr(int('2801',16)),chr(int('2804',16))]),
                   "".join([chr(int('2812',16)),chr(int('2805',16))]),
                   "".join([chr(int('2812',16)),chr(int('2834',16))]),

                   "".join([chr(int('2802',16)),chr(int('2801',16))]),
                   "".join([chr(int('2802',16)),chr(int('2822',16))]),
                   "".join([chr(int('2802',16)),chr(int('2803',16))]),

                   "".join([chr(int('2802',16)),chr(int('2804',16))]),
                   "".join([chr(int('2802',16)),chr(int('2826',16))]),
                   "".join([chr(int('2802',16)),chr(int('2832',16))]),
                   "".join([chr(int('2802',16)),chr(int('2834',16))]),
                   "".join([chr(int('2803',16)),chr(int('2804',16))]),
                   "".join([chr(int('2801',16)),chr(int('2801',16))]),
                   chr(int('280C',16))]

temp_symbol = ["!","\"","#","$", "%","&","\'","(",")","*","+",",","-",".","/"]
temp_symbol_B = [chr(int('282E',16)),
                 chr(int('2810',16)),
                 chr(int('283C',16)),
                 chr(int('282B',16)),

                 chr(int('2829',16)),
                 chr(int('282F',16)),
                 chr(int('2804',16)),

                 chr(int('2837',16)),
                 chr(int('283E',16)),
                 chr(int('2821',16)),
                 chr(int('282C',16)),

                 chr(int('2820',16)),
                 chr(int('2824',16)),
                 chr(int('2828',16)),
                 chr(int('280C',16))

                 ]


temp_number = [0,1,2,3,4,5,6,7,8,9]
temp_number_B = [chr(int('281A',16)),chr(int('2801',16)),chr(int('2803',16)),chr(int('2809',16)),chr(int('2819',16)),chr(int('2811',16)),
                 chr(int('280B',16)),chr(int('281B',16)),chr(int('2813',16)),chr(int('280A',16))]

temp_UpperCase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
temp_UpperCase_B=["".join([chr(int('2820', 16)),chr(int('2801', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2803', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2809', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2819', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2811', 16))]),

                  "".join([chr(int('2820', 16)), chr(int('280B', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('281B', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2813', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('280A', 16))]),

                  "".join([chr(int('2820', 16)), chr(int('281A', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2805', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2807', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('280D', 16))]),

                  "".join([chr(int('2820', 16)), chr(int('281D', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2815', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('280F', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('281F', 16))]),

                  "".join([chr(int('2820', 16)), chr(int('2817', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('280E', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('281E', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2825', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2827', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('283A', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('282D', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('283D', 16))]),
                  "".join([chr(int('2820', 16)), chr(int('2835', 16))])

                  ]

temp_LowerCase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
temp_LowerCase_B=[chr(int('2801', 16)),
                  chr(int('2803', 16)),
                  chr(int('2809', 16)),
                  chr(int('2819', 16)),
                  chr(int('2811', 16)),

                  chr(int('280B', 16)),
                  chr(int('281B', 16)),
                  chr(int('2813', 16)),
                  chr(int('280A', 16)),

                  chr(int('281A', 16)),
                  chr(int('2805', 16)),
                  chr(int('2807', 16)),
                  chr(int('280D', 16)),

                  chr(int('281D', 16)),
                  chr(int('2815', 16)),
                  chr(int('280F', 16)),
                  chr(int('281F', 16)),

                  chr(int('2817', 16)),
                  chr(int('280E', 16)),
                  chr(int('281E', 16)),
                  chr(int('2825', 16)),
                  chr(int('2827', 16)),
                  chr(int('283A', 16)),
                  chr(int('282D', 16)),
                  chr(int('283D', 16)),
                  chr(int('2835', 16))
                  ]

#약어 - 라, 아, 차는 약어가 없으므로 풀어쓴 문자로 대체
temp_abbreviation = ['가', '나', '다', '라', '마', '바', '사', '아', '자', '차', '카', '타', '파', '하']
temp_abbreviation_B = ['$', 'C', 'I', '1<', 'E', '^', 'L', 'G<', '.', 'H<', 'F', 'H', 'D', 'J']

temp_abbreviation_jungjongsung = ["ㅓㄱ", "ㅓㄴ", "ㅓㄹ", "ㅕㄴ", "ㅕㄹ", "ㅕㅇ", "ㅗㄱ",
                                  "ㅗㄴ", "ㅗㅇ", "ㅜㄴ", "ㅜㄹ", "ㅡㄴ", "ㅡㄹ", "ㅣㄴ", "것"]
temp_abbreviation_jungjongsung_B = ['?', ')', 'T', '*', '\\', ']', 'X', '(', '=', 'G', '&', 'Z', '!', 'Q', '_S']

#construct mapping_dict
map_chosung = defaultdict()
map_jungsung = defaultdict()
map_jongsung = defaultdict()
map_number = defaultdict()

map_UpperCase = defaultdict()
map_LowerCase = defaultdict()

map_Symbol = defaultdict()

map_abbreviation = defaultdict()
map_jungjongsung_abbreviation = defaultdict()

for idx, sung in enumerate(temp_jongsung):
    map_jongsung[sung]=temp_jongsung_B[idx]
map_jongsung[" "]=""

for idx, sung in enumerate(temp_jungsung):
    map_jungsung[sung]=temp_jungsung_B[idx]

for idx, sung in enumerate(temp_chosung):
    map_chosung[sung]=temp_chosung_B[idx]

for idx, num in enumerate(temp_number):
    map_number[num]=temp_number_B[idx]

for idx, up in enumerate(temp_UpperCase):
    map_UpperCase[up] = temp_UpperCase_B[idx]

for idx, low in enumerate(temp_LowerCase):
    map_LowerCase[low] = temp_LowerCase_B[idx]

for idx, sym in enumerate(temp_symbol):
    map_Symbol[sym] = temp_symbol_B[idx]

for idx, abb in enumerate(temp_abbreviation):
    map_abbreviation[abb]=temp_abbreviation_B[idx]

for idx, j_abb in enumerate(temp_abbreviation_jungjongsung):
    map_abbreviation[j_abb] = temp_abbreviation_jungjongsung_B[idx]