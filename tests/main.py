def stringReverser(str:str) ->str:
    return str[::-1]

def intfromstring(str:str)->str:
    result=[]
    for i in str:
        if i.isdigit():
            result.append(i)
    return ''.join(result)



def str_from_integer(strs):
    for word in strs:
        if word.istitle():
            return True
        else:
            return False       


class TestStringMethods:
    def test_case1(self):
        assert stringReverser('warsaw') == 'wasraw'

    def test_case2(self):
        assert intfromstring('krakow55krakow') == '55'

    def  test_case3(self):
        assert str_from_integer('Globallogic') == True      