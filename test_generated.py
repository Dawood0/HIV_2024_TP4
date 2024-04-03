def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, 'Test 2'
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, 'Test 2'
def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, 'Test 2'
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, 'Test 2'
def test_separate_paren_groups(separate_paren_groups):
    assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
    assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert separate_paren_groups('abc def ghi') == []
    assert separate_paren_groups('(())') == ['(())']
    assert separate_paren_groups('abc def ghi') == []
    assert separate_paren_groups('(())) (())') == ['(()())', '((()))', '()', '((())())']

