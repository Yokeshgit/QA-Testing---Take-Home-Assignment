from main import Solution

def test_positive():
    s = Solution()
    cases="[]{}[][{}]"
    assert s.isValid(cases) == True

def test_negative():
    s = Solution()
    cases="]{}[][{}]"
    assert s.isValid(cases) == False

def test_negative_2():
    s = Solution()
    cases="][]{}[][{}]["
    assert s.isValid(cases) == False
    
def test_negative_3():
    s = Solution()
    cases="`{ [](){}([]){}"
    assert s.isValid(cases) == False
  
def test_Positive_1():
    s = Solution()
    cases="[[]{}[]{}]"
    assert s.isValid(cases) == True

def test_Negative_4():
    s = Solution()
    cases="][]{}[][{}]["
    assert s.isValid(cases) == False    
    
def test_Positive_3():
    s = Solution()
    cases="({}()[{}])"
    assert s.isValid(cases) == True
    
def test_negative_5():
    s = Solution()
    cases="][]}{[][()]["
    assert s.isValid(cases) == False
    
def test_Positive_4():
    s = Solution()
    cases="{[]{}[][{}]}"
    assert s.isValid(cases) == True
    
def test_Positive_5():
    s = Solution()
    cases="((){}[]([]))"
    assert s.isValid(cases) == True