def standard(brailleText):
    global count
    # 페이지 줄바꿈 (32글자가 한 라인)
    braillelist = brailleText.splitlines()  # '\n' 단위로 리스트화
    newbraille = ""  # 32자 단위로 자른 텍스트를 저장할 곳
    for j in range(len(braillelist)):  # 32자 단위로 잘라서 '\n'으로 연결
        newLine = [(braillelist[j])[i:i + 32] for i in range(0, len(braillelist[j]), 32)]
        newbraille += '\n'.join(newLine)
        newbraille += '\n'
    # 페이지 목차 (26라인이 한 페이지이지만 마지막 라인은 공백+목차이므로 25줄 단위로 카운트)
    numtostr = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e",
                "6": "f", "7": "g", "8": "h", "9": "i", "0": "j"}  # 목차에서는 0,1...9가 j,a...i로 치환되어 표시됨
    linenumber = newbraille.count('\n')  # 몇 줄인지 카운트
    pagelist = newbraille.splitlines()  # 32자 단위로 잘라서 하나로 합쳐둔 텍스트를 다시 '\n' 단위로 리스트화
    lastpage = ""
    count = 0
    for i in range(1, linenumber):  # 25줄 단위로 자르고 26줄째에는 공백+목차 줄 삽입
        pagenum = ""
        stringnum = str(int(i / 25))  # 25줄 당 1페이지
        if i != 0 and i % 25 == 0:
            for j in range(len(stringnum)):
                pagenum += numtostr[stringnum[j]]  # 숫자로 된 목차를 위에 있는 numtostr를 이용해 알파벳으로 치환
            pagelist.insert(i + (int(i / 25) - 1),
                            '%32s' % ('#' + pagenum))  # 26번째 줄은 32칸에서 오른쪽부터 #+목차를 채우고 나머지는 공백으로 채움
            count = i + int(i / 25)
        elif i == count:
            pagelist[i] = '' + pagelist[i]
        if i % 25 != 0 and i == linenumber - 1:
            for j in range(len(str(int(i / 25) + 1))):
                lastpage += numtostr[str(int(i / 25) + 1)[j]]
    if not linenumber % 25 == 0:  # 마지막 페이지에 줄이 남으면 공백 채우기
        for i in range(0, 25 - (linenumber % 25)):
            pagelist.append('')
    pagelist.append('%32s' % ('#' + lastpage))
    pagelist.append('')
    return pagelist