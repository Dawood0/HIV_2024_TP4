# from poly_llm.to_test.separate_paren_groups import separate_paren_groups
# from poly_llm.to_test.parse_nested_parens import parse_nested_parens
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
from transformers import AutoModel, AutoTokenizer
import json
from transformers import AutoTokenizer, AutoModelWithLMHead
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import torchvision
# from coverage import Coverage
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
if __name__ == '__main__':
    # executor = AbstractExecutor(file_name_check)
    # prompt_generator = PromptGenerator(file_name_check)

    checkpoint = "Salesforce/codet5p-770m-py"
    device = "cuda" # for GPU usage or "cpu" for CPU usage

    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = T5ForConditionalGeneration.from_pretrained(checkpoint)






import importlib
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

puts=[closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]
puts_names=['closest_integer', 'file_name_check', 'find_closest_elements', 'numerical_letter_grade', 'separate_paren_groups']

few_shot_examples = ["""assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, 'Test 2' """,

    '''assert file_name_check("example.txt") == 'Yes'\n
    assert file_name_check("1example.dll") == 'No' \n''',

    '''assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
''',
'''assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([1.2]) == ['D+']
''',

'''assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
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

    # test = test.split("\n")[:-2]
    # test = "\n".join(test)+'\n' +'    return\n'
    test_name='test_'+puts_names[i]
    filename = "test_generated.py"
    llm_generator.write_test_to_file(test, filename=filename)
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
    try:print('line: ',coverage_data['coverage']['percent_covered_display'])
    except:pass
    try:print('branch: ',coverage_data['coverage']['covered_branches']/coverage_data['coverage']['num_branches'])
    except:pass
    i+=1
    
    

