
from poly_llm.to_test.closest_integer import closest_integer
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.to_test.find_closest_elements import find_closest_elements
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import separate_paren_groups
from poly_llm.to_test.closest_integer import test_closest_integer
from poly_llm.to_test.file_name_check import test_file_name_check
from poly_llm.to_test.find_closest_elements import test_find_closest_elements
from poly_llm.to_test.numerical_letter_grade import test_numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import test_separate_paren_groups


from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import json

import importlib


puts=[closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]
puts_names=['closest_integer', 'file_name_check', 'find_closest_elements', 'numerical_letter_grade', 'separate_paren_groups']

model_name = "Salesforce/codet5-large-ntp-py"
tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
model = T5ForConditionalGeneration.from_pretrained(model_name)

def q_1():
    tests=[test_closest_integer, test_file_name_check, test_find_closest_elements, test_numerical_letter_grade, test_separate_paren_groups]
    
    i=0
    for test in tests:
        executor2 = AbstractExecutor(test)
        coverage_data = executor2._execute_input()
        print(f"{i}----------------\nCoverage data for {puts_names[i]}")
        print(coverage_data)
        try:print(coverage_data['coverage']['covered_branches']/coverage_data['coverage']['num_branches'])
        except:pass
        i+=1
# q_1()


def q_2():
    model_name = "Salesforce/codet5-large-ntp-py"
    tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
    model = T5ForConditionalGeneration.from_pretrained(model_name) 
    i=0
    for put in puts[i:]:
        executor = AbstractExecutor(put)
        prompt_generator = PromptGenerator(put)

        llm_generator = LLMTestGenerator(model, tokenizer, put)
        prompt = prompt_generator.generate_prompt()

        # print(f"THE PROMPT {prompt}")
        test, test_name = llm_generator.create_test_function(prompt)

        # remove the last line of test

        test = test.split("\n")[:-2]
        test = "\n".join(test)+'\n' +'    return\n'
        test_name='test_'+puts_names[i]
        filename = "test_generated.py"
        llm_generator.write_test_to_file(test, filename=filename)
        # input('finished training and writing test to file check it for mistakes, press enter to continue...\n')
        module_name = filename.split(".")[0]
        function_name = test_name

        # Dynamically import the module
        module = importlib.import_module(module_name)
        if i==0:
            module = importlib.import_module(module_name)
        else:
            module = importlib.reload(module)
        function = getattr(module, function_name)

        executor2 = AbstractExecutor(function)

        coverage_data = executor2._execute_input(put)
        print(f"Coverage data for {puts_names[i]}")
        print(coverage_data)
        try:print(coverage_data['coverage']['covered_branches']/coverage_data['coverage']['num_branches'])
        except:pass
        i+=1
        # break
# q_2()


def q_3():

    few_shot_examples = ["""def test_closest_integer():
        assert closest_integer("10") == 10, "Test 1"
        assert closest_integer("14.5") == 15, 'Test 2' """,

        '''def test_file_name_check(): \n 
        assert file_name_check("example.txt") == 'Yes'\n
        assert file_name_check("1example.dll") == 'No' \n''',

        '''def test_find_closest_elements():
        assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
        assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    ''',
    '''def test_numerical_letter_grade():# pragma: no cover
        assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
        assert numerical_letter_grade([1.2]) == ['D+']
    ''',

    '''def test_separate_paren_groups():
        assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
        assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    '''
        ]
    i=0
    for put in puts[i:]:
        executor = AbstractExecutor(put)
        prompt_generator = PromptGenerator(put)



        llm_generator = LLMTestGenerator(model, tokenizer, put)
        prompt = prompt_generator.generate_prompt(few_shot_examples=[few_shot_examples[i]])

        # print(f"THE PROMPT {prompt}")
        test, test_name = llm_generator.create_test_function(prompt)

        # remove the last line of test

        test = test.split("\n")[:-1]
        test = "\n".join(test)+'\n'
        
        filename = "test_generated.py"
        llm_generator.write_test_to_file(test, filename=filename)
        input('presssomehting')
        # input('finished training and writing test to file check it for mistakes, press enter to continue...\n')
        module_name = filename.split(".")[0]
        function_name = test_name

        # Dynamically import the module
        module = importlib.import_module(module_name)
        if i==0:
            module = importlib.import_module(module_name)
        else:
            module = importlib.reload(module)
        function = getattr(module, function_name)

        executor2 = AbstractExecutor(function)

        coverage_data = executor2._execute_input(put)
        print(f"Coverage data for {puts_names[i]}")
        print(coverage_data)
        try:print(coverage_data['coverage']['covered_branches']/coverage_data['coverage']['num_branches'])
        except:pass
        i+=1
# q_3()


def q_4():

    few_shot_examples = ["""
        assert closest_integer("10") == 10, "Test 1"
        assert closest_integer("14.5") == 15, 'Test 2' """,

        '''
        assert file_name_check("example.txt") == 'Yes'\n
        assert file_name_check("1example.dll") == 'No' \n''',

        '''
        assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
        assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    ''',
    '''
        assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
        assert numerical_letter_grade([1.2]) == ['D+']
    ''',

    '''
        assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
        assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    '''
        ]
    few_shot_examples2=[ '''
    assert closest_integer("15.3") == 15, "Test 3"''',
    
    '''
    assert file_name_check("example1234.txt") == 'No' ''',
    
    '''
    assert find_closest_elements([1.0, 3.0]) == (1.0, 3.0)
    ''',
    
    '''
    assert numerical_letter_grade([0.5]) == ['E'] ''',

    '''
    assert separate_paren_groups('(())') == ['(())']'''

    ]
    few_shot_examples3=[
    '''
    assert closest_integer("-17.5") == -18, "Test 4" ''',
    '''
    assert file_name_check("1example.txt") == 'No'
    ''',
    '''
    assert find_closest_elements([-1.0, -2.0, -3.0, -4.0, -5.0, -2.2]) == (-2.2, -2.0)'''
    ,'''
    assert numerical_letter_grade([4.0, 3.0, 2.0, 1.0, 0.5]) == ['A+', 'C', 'C+', 'D', 'E'] ''',
    '''
    assert separate_paren_groups('abc def ghi') == [] '''
    ]


    i=4
    for put in puts[i:]:
        executor = AbstractExecutor(put)
        prompt_generator = PromptGenerator(put)

        # model_name = "Salesforce/codet5-large-ntp-py"
        # tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
        # model = T5ForConditionalGeneration.from_pretrained(model_name) 

        llm_generator = LLMTestGenerator(model, tokenizer, put)
        # prompt = prompt_generator.generate_prompt(few_shot_examples=[few_shot_examples2[i]])
        # prompt = prompt_generator.generate_prompt(few_shot_examples=[few_shot_examples[i],few_shot_examples2[i]])
        prompt = prompt_generator.generate_prompt(few_shot_examples=[few_shot_examples[i],few_shot_examples2[i],few_shot_examples3[i]])

        # print(f"THE PROMPT {prompt}")
        test, test_name = llm_generator.create_test_function(prompt)

        # remove the last line of test

        # test = test.split("\n")[:-1]
        # test = "\n".join(test)+'\n'
        
        filename = "test_generated.py"
        test_name= 'test_'+puts_names[i]
        llm_generator.write_test_to_file(test, filename=filename)
        # input('presssomehting')
        input('finished training and writing test to file check it for mistakes, press enter to continue...\n')
        module_name = filename.split(".")[0]
        function_name = test_name

        # Dynamically import the module
        module = importlib.import_module(module_name)
        if i==0:
            module = importlib.import_module(module_name)
        else:
            module = importlib.reload(module)
        function = getattr(module, function_name)

        executor2 = AbstractExecutor(function)

        coverage_data = executor2._execute_input(put)
        print(f"Coverage data for {puts_names[i]}")
        print(coverage_data)
        try:print(coverage_data['coverage']['covered_branches']/coverage_data['coverage']['num_branches'])
        except:pass
        i+=1

        # break
q_4()