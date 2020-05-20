from collections import defaultdict

#초성
temp_chosung = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
temp_chosung_B = ["@",",@","C","I",",I","\"","E","^",",^",",",",,","G",".",",.",";", "F","H","D","J"]

#중성
temp_jungsung = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"]
temp_jungsung_B = ["<","R", ">",">R","S ","N", ":","/","U", "V","VR","Y","+","M", "P","PR","MR", "%","[","W","O"]

#종성
temp_jongsung = ["ㄱ","ㄲ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄼ","ㄽ","ㄾ","ㅀ",
                 "ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
temp_jongsung_B = ["A","AA","A'","3","3K","30","9","1","1A","1B","1'","18","14","10", "5","B","B'","\'","/",
                   "7", "K","2","6","8", "4","0"]


temp_symbol = ["!","\"","#","$",
               "%","&","\'","(",
               ")","*","+",",","-",".","/",
               ":",";","<","=",">","?","@","[","\\","^"
               ,"_","`","{","}","~"]
temp_symbol_B = ["6","8","#","$","0P","&",",8","8'",",0","*","5","\"","_","4","_/",
            "\"1",";2","\"8","33","01","8","@","82","\\","^","_","@","81","\"0","^" ]

temp_number = [0,1,2,3,4,5,6,7,8,9]
temp_number_B = ["#J","#A","#B","#C","#D","#E","#F","#G","#H","#I"]

temp_UpperCase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
                  "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
temp_UpperCase_B=[",A",",B",",C",",D",",E",",F",",G",",H",",I",",J",",K",",L",",M",",N",",O",
                  ",P",",Q",",R",",S",",T",",U",",V",",W",",X",",Y",",Z"]

temp_LowerCase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
temp_LowerCase_B=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" ]

#construct mapping_dict
map_chosung = defaultdict()
map_jungsung = defaultdict()
map_jongsung = defaultdict()
map_number = defaultdict()

map_UpperCase = defaultdict()
map_LowerCase = defaultdict()

map_Symbol = defaultdict()



#종성
for idx, sung in enumerate(temp_jongsung):
    map_jongsung[sung]=temp_jongsung_B[idx]
map_jongsung[" "]=""

#중성
for idx, sung in enumerate(temp_jungsung):
    map_jungsung[sung]=temp_jungsung_B[idx]


#초성
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

