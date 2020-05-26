from collections import defaultdict


temp_chosung = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ","ㄲ","ㄸ","ㅃ","ㅆ","ㅉ"]
temp_chosung_B = ["`","C","I","\"","E",
                  "^",",","G",".",";",
                  "F","H","D","J",
                  "".join([",","@"]),
                  "".join([",","I"]),
                  "".join([",","^"]),
                  "".join([",",","]),
                  "".join([",","."])
                  ]


temp_jungsung = ["ㅏ","ㅑ","ㅓ","ㅕ","ㅗ","ㅛ","ㅜ","ㅠ","ㅡ","ㅣ",
                 "ㅐ","ㅒ","ㅔ","ㅖ","ㅘ","ㅙ","ㅚ","ㅝ","ㅞ","ㅟ","ㅢ"]
temp_jungsung_B = ["<"," >"," S ",":"," U"," +"," M"," %", "["," O",
                   "R","".join([">","R"]) ,"N","/","V", "".join(["V","R"]), "Y","P",
                   "".join(["P","R"]),"".join(["M","R"]),"W"

                   ]

temp_jongsung = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ",
                 "ㄳ","ㄵ","ㄶ","ㄺ",
                 "ㄻ","ㄼ","ㄽ","ㄾ",
                 "ㄿ","ㅀ","ㅄ",
                 "ㄲ","ㅆ"]

temp_jongsung_B = ["A","3","9","1",
                   "5","B","\'","7",
                   "K","2","6","8",
                   "4","0",
                   "".join(["A","\'"]), "".join(["3","K"]), "".join(["3","0"]),"".join(["1","A"]),
                   "".join(["1","5"]),"".join(["1","B"]),"".join(["1","\'"]),"".join([" 1","8 "]),
                   "".join(["1","4"]),"".join(["1","0"]),"".join(["B","\'"]),
                   "".join(["A","A"]),"/"
                   ]

temp_symbol = ["!","\"","#","$",
               "%","&","\'","(",
               ")","*","+",",","-",".","/"]
temp_symbol_B = ["6","8","#","$",
                "".join(["0","p"]),"&","".join([",","8"]),"".join(["8","\'"]),
                "".join([",","0"]),"*","5","\"","_","4","".join(["_","/"])
                ]
#여는 큰 따옴표는 8 / 닫는 큰 따옴표는 0
#물음표 아직 안 넣어서 오류 날지도 모름.
temp_number = [0,1,2,3,4,5,6,7,8,9]
temp_number_B = ["".join(["","J"]),
                 "".join(["","A"]),
                 "".join(["","B"]),
                 "".join(["","C"]),
                 "".join(["","D"]),
                 "".join(["","E"]),
                 "".join(["","F"]),
                 "".join(["","G"]),
                 "".join(["","H"]),
                 "".join(["","I"]),
                 ]

temp_UpperCase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
temp_UpperCase_B=["".join([",","A"]),
                  "".join([ ",","B" ]),
                  "".join([",","C"]),
                  "".join([",","D" ]),
                  "".join([",","E "]),

                  "".join([" ,","F "]),
                  "".join([",","G "]),
                  "".join([",","H "]),
                  "".join([",","I"]),

                  "".join([",","J"]),
                  "".join([",","K "]),
                  "".join([",","L "]),
                  "".join([",","M "]),

                  "".join([",", "N "]),
                  "".join([",","O"]),
                  "".join([",", "P "]),
                  "".join([",","Q"]),

                  "".join([",","R"]),
                  "".join([",", "S "]),
                  "".join([",","T"]),
                  "".join([",","U "]),
                  "".join([",","V"]),
                  "".join([",", "W "]),
                  "".join([",","X"]),
                  "".join([",", "Y "]),
                  "".join([",","Z"]),

                  ]

temp_LowerCase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
temp_LowerCase_B=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" ]

#앞음절-약어 사용, 뒷음절-약어 미사용
temp_abbreviation_word = ["그래서", "그러나", "그러면", "그러므로", "그런데", "그리고", "그리하여"]
temp_abbreviation_word_B = ["as", "ac", "a3", "a5", "an", "au", "a:"]

#construct mapping_dict
map_chosung = defaultdict()
map_jungsung = defaultdict()
map_jongsung = defaultdict()
map_number = defaultdict()

map_UpperCase = defaultdict()
map_LowerCase = defaultdict()

map_Symbol = defaultdict()

map_abbreviation_word = defaultdict()



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

for idx, abb in enumerate(temp_abbreviation_word):
    map_abbreviation_word[abb] = temp_abbreviation_word_B[idx]
