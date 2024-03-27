# test='''def test_file_name_check(file_name_check):
#     assert file_name_check('test.txt') == 'Yes'
#     assert file_name_check('test.exe') == 'Yes'
#     assert file_name_check('test.dll') == 'Yes'
#     assert file_name_check('test.txt.exe') == 'Yes'
#     assert file_name_check('test.txt.dll') == 'Yes'
#     assert file_name_check('test.exe.dll') == 'Yes'
#     assert file_name_check('test.exe.txt') == 'Yes'
#     assert file_name_check('test.exe.txt.exe') == 'Yes'
#     assert file_name_check('test.exe.txt.dll') == 'Yes'
#     assert file_name_check('test.exe.txt.exe.dll') == 'Yes'
#     assert file_name_check('test.exe.txt.exe.txt.exe.dll') == 'Yes'
#     assert file_name_check('test.exe.txt.exe.txt.exe.dll.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe.exe'''
# test = test.split("\n")[:-1]
# test = "\n".join(test)+'\n'

# print(test)


from test_generated import test_file_name_check
