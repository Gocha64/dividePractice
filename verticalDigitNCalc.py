import docx

class CalcPractice:
    bank = [] #이전문제 저장
    baseP = '' #문제워드문서 베이스
    baseA = '' #해답워드문서 베이스
    fileName = 'digitNCalc' #저장될 문서 이름
    
    def __init__(self, baseForPracticeDocxName, baseForAnswerDocxName):
        self.baseP = baseForPracticeDocxName
        self.baseA = baseForAnswerDocxName
        self.fileName = self.fileName
        
    def check(self,curProblem): #중복문제 체크
        for b in self.bank:
            if b == curProblem:
                return True
        return False
    
    def getProblem(self):
        pass
    
    #세로식에만 적용
    def digitNCalc(self, n):
        self.bank = [] #이전문제 초기화
        c = '' #현재 문제
        i = 0 #현재 문제 위치
        file = open(self.fileName+'.txt', 'w')
        wFile = docx.Document(self.baseP)
        wFile._body.clear_content()
        
        while i < n:
            #문제 생성
            c = self.getProblem()
            
            #중복 검사
            if self.check(c):
                continue
        
            self.bank.append(c)
        
            if len(self.bank) > 51: #오래된 문제 삭제(50개이상
                self.bank = self.bank[1:]
        
    
            #문제 저장
            self.fileWrite(file, c)
            self.docxWrite(wFile, c)

            i += 1

        file.close()
        print(file.name + ' generated')
        wFile.save(self.fileName+'.docx')
        print(self.fileName+'.docx generated')
        

        #정답 생성           
        self.answering()
    
        #정답 저장
        self.txt2Docx(self.baseA)



    def fileWrite(self, file, c): #생성된 문제 c를 txt에 저장
        pass
    
    def docxWrite(self, wFile, c): #생성된 문제 c를 word에 저장
        pass

    def answering(self): #txt로 저장 포함
        pass
    
    def txt2Docx(self, answerBaseWordName):
        pass

