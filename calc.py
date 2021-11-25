from decimal import Decimal
def plus(ch1, zn1, ch2, zn2):
    obshzn=zn1*zn2
    obshch=ch1*zn2+ch2*zn1
    print(obshch,"/",obshzn)
def plusdec(fr1,fr2):
    zeloe=Decimal(fr1)+Decimal(fr2)
    print(zeloe)

def minusdec(fr1,fr2):
    zeloe=Decimal(fr1)-Decimal(fr2)
    print(zeloe)

def umnozdec(fr1,fr2):
    zeloe=Decimal(fr1)*Decimal(fr2)
    print(zeloe)

def delendec(fr1,fr2):
    zeloe=Decimal(fr1)/Decimal(fr2)
    print(zeloe)

def minus(ch1, zn1, ch2, zn2):
    obshzn=zn1*zn2
    obshch=ch1*zn1-ch2*zn2
    print(obshch,'/', obshzn)

def umnoz(ch1, zn1, ch2, zn2):
    obshzn=zn1*zn2
    obshch=ch1*ch2
    print(obshch,"/",obshzn)

def delen(ch1, zn1, ch2, zn2):
    obshzn=zn1*ch2
    obshch=ch1*zn2
    print(obshch,"/",obshzn)

def isDecimal(s):
    return s.count(".")==1 or s.count(",")==1

def isRatio(s):
    return s.count("/")==1


if __name__ == '__main__':
    print('Привет! Это калькулятор дробей. В нем ты можешь проводить операции с любыми двумя дробями ')
    fraction1 = input("Введите первую дробь : ")
    znak=input("Введите знак : ")
    fraction2 = input("Введите вторую дробь : ")
    if ('.' in fraction1) or (',' in fraction1 ) or ('.' in fraction2) or (',' in fraction2 ) :
        if '.' in fraction1:
            if fraction1.count('.')>1 or fraction1.count(',')>0 or fraction1.count('/')>0:
                fraction1=input('ДОЛЖЕНА БЫТЬ ТОЛЬКО ОДНА ТОЧКА В ЭТОМ ЧИСЛЕ')
        if ',' in fraction1:
            if fraction1.count(',')>1 or fraction1.count('.')>0 or fraction1.count('/')>0:
                fraction1=input('ДОЛЖЕНА БЫТЬ ТОЛЬКО ОДНА ЗАПЯТАЯ В ЭТОМ ЧИСЛЕ')
        if '.' in fraction2:
            if fraction2.count('.')>1 or fraction1.count(',')>0 or fraction1.count('/')>0:
                fraction2=input('ДОЛЖЕНА БЫТЬ ТОЛЬКО ОДНА ТОЧКА В ЭТОМ ЧИСЛЕ')
        if ',' in fraction2:
            if fraction1.count(',')>1 or fraction1.count('.')>0 or fraction1.count('/')>0 :
                fraction2=input('ДОЛЖЕНА БЫТЬ ТОЛЬКО ОДНА ЗАПЯТАЯ В ЭТОМ ЧИСЛЕ')
    if '/' in fraction1 or '/' in fraction2:
        if fraction1.count('/')>1 or fraction1.count(',')>0 or fraction1.count('.')>0:
            fraction1=input('ДОЛЖЕН БЫТЬ ТОЛЬКО ОДИН СЛЕШ В ЭТОМ ЧИСЛЕ')



    #while(not fraction1.isnumeric()):
     #   fraction1 = input("Ошибка - допускаются только цифры, точка и запятая, а также /. Введите первую дробь : ")
    #znak=input("Введите знак ")

    if isDecimal(fraction1) or isDecimal(fraction2):
        if znak=="+":
            print(plusdec(fraction1,fraction2))
        if znak=="-":
            print(minusdec(fraction1,fraction2))
        if znak=="*":
            print(umnozdec(fraction1,fraction2))
        if znak==":":
            print(delendec(fraction1,fraction2))
    if isRatio(fraction1) or isRatio(fraction2):
        ch1,zn1 = fraction1.split('/')
        chisl1,znam1 = int(ch1),int(zn1)
        ch2,zn2 = fraction2.split('/')
        chisl2,znam2 = int(ch2),int(zn2)
        if znak=="+":
            print(plus(chisl1, znam1, chisl2, znam2))
        if znak=="-":
            print(minus(chisl1, znam1, chisl2, znam2))
        if znak=="*":
            print(umnoz(chisl1, znam1, chisl2, znam2))
        if znak==":" or znak=="/":
            print(delen(chisl1, znam1, chisl2, znam2))

