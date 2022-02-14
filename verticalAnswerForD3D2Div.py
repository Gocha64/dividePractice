import docx
# 1문제 -> 4줄 or 3줄
# line 1 -> 공백
# line 2 -> 피연산자)피연산자
# line 3 -> 공백
# line 4 -> 5번째 문제일경우) 공백
# 1페이지 -> 20문제



def line2nd(line):
    a = int(line[:2])
    b = int(line[3:])
    return a, b


def answering(fName):
    f1 = open(fName + '.txt', 'r')
    f2 = open(fName + "Answer.txt",'w')
    line = ''
    p = 1
    f1.readline()
    
    while True:
        f2.write("page. %d\n" %p)
        p += 1
        for i in range(20):
            a = 0
            b = 0
            o = ''
            data = ''
            for j in range(2):
                line = f1.readline()     
                #print('2. ' + line)
                if not line: # 파일의 마지막 라인을 거쳐감
                    data = "%d÷%d=%d...%d\n" %(a,b,(b//a),(b%a))
                    f2.write(data)
                    print(f2.name + ' generated')
                    f1.close()
                    f2.close()
                    return 0
                if j == 0:
                    a, b = line2nd(line)
            
            data = "%d÷%d=%d...%d\n" %(a,b,(b//a),(b%a))
            f2.write(data)

def answerText2Docx(fName, baseDocx):
    document = docx.Document(baseDocx)
    file = open(fName + 'Answer.txt', 'r')
    document._body.clear_content()
    for line in file:
        #print('1.'+line)
        document.add_paragraph(line[:-1])
    document.save(fName + 'Answer.docx')
    print(fName + 'Answer.docx generated')

if __name__ == '__main__':
    answering('D3D2Div')
    answerText2Docx('D3D2Div', 'baseForVerticalAnswer.docx')


