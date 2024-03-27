def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, 'Test 2'
    assert closest_integer("15.3") == 15, 'Test 3'
    assert closest_integer("-17.5") == -18, 'Test 4'
def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example1234.txt") == 'No'
    assert file_name_check("1example.txt") == 'No'
def test_find_closest_elements(find_closest_elements):
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert find_closest_elements([1.0, 3.0]) == (1.0, 3.0)
    assert find_closest_elements([-1.0, -2.0, -3.0, -4.0, -5.0, -2.2]) == (-2.2, -2.0)
def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([3.9, 3, 1.7, 2, 3.5]) == ['A', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([1.3]) == ['D+']
    assert numerical_letter_grade([1.4]) == ['C-']
    assert numerical_letter_grade([0.1]) == ['D-']
def test_separate_paren_groups(separate_paren_groups):
    assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
    assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert separate_paren_groups('abc def ghi') == []
    assert separate_paren_groups('(())') == ['(())']
    assert separate_paren_groups('(()) (())') == ['(())', '(())']

