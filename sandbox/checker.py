#!/usr/bin/python3

import glob
import os
import subprocess

def my_run(*args, **kwargs):
    if 'call' in subprocess.__dict__:
        return subprocess.call(*args, **kwargs)
    if 'run' in subprocess.__dict__:
        return subprocess.run(*args, **kwargs)

def split_by_groups(s):
    return [t for t in s.split() if t]

def not_so_strict_compare(actual, expected):
    return split_by_groups(actual) == split_by_groups(expected)

user_prefix = 'users/'
problem_prefix = 'problems/'

users = glob.glob(user_prefix + '*')
problems = glob.glob(problem_prefix + '*')

users = [t[len(user_prefix):] for t in users]
problems = [t[len(problem_prefix):] for t in problems]

results = {}

for current_user in users:
    results[current_user] = {}
    print()
    print('user = ', current_user)
    for current_problem in problems:
        dat_prefix = 'dat'
        res_prefix = 'res'
        problem_path = problem_prefix + current_problem + '/'
        dat_path = problem_path + dat_prefix
        res_path = problem_path + res_prefix
        dats = glob.glob(dat_path + '*')
        resources = glob.glob(res_path + '*')
        dats_suffixes = [t[len(dat_path):] for t in dats]

        solutions_path = user_prefix + current_user + '/' + current_problem + '/'
        languages = [t[len(solutions_path):] for t in glob.glob(solutions_path + '*')]
        languages = [t for t in languages if t in ['c++', 'python', 'go']]
        results[current_user][current_problem] = {}
        
        for current_suffix in dats_suffixes:
            current_res = res_path + current_suffix
            current_dat = dat_path + current_suffix
            for current_language in languages:
                print ('check program ', current_problem, ' with input ', current_dat, ' and output', current_res)
                program_prefix = solutions_path + current_language
                try:
                    if current_language == 'python':
                        program = program_prefix + '/main.py'
                        program_instance = subprocess.Popen(['python3', program],
                                                            stdin=subprocess.PIPE,
                                                            stdout=subprocess.PIPE,
                                                            universal_newlines = True)
                    elif current_language == 'c++':
                        try:
                            os.remove('prog')
                        except Exception:
                            pass
                        compile_command = ['g++', '-std=c++11', program_prefix + '/main.cpp', '-o', 'prog']
                        print('c++: trying to compile: ', compile_command)
                        my_run(compile_command)
                        open('prog')
                        print('c++ compilation successfull')
                        program_instance = subprocess.Popen(['./prog'],
                                                            stdin=subprocess.PIPE,
                                                            stdout=subprocess.PIPE,
                                                            universal_newlines = True)
                    elif current_language == 'go':
                        print('\tcompile go program')
                        try:
                            os.remove('main')
                        except Exception:
                            pass
                        source_path = program_prefix + '/main.go'
                        print('source_path = ', source_path)
                        my_run(['go', 'build', source_path])
                        program_instance = subprocess.Popen(['./main'],
                                                            stdin=subprocess.PIPE,
                                                            stdout=subprocess.PIPE,
                                                            universal_newlines = True)
                        if program_instance:
                            print('program instance ready')
                    else:
                        raise NameError('language %s is not supported'%current_language)
                        
                    output = program_instance.communicate(open(current_dat).read())[0]
                    expected = open(current_res).read()
                    pre_final_results = results[current_user][current_problem]
                    test_result = not_so_strict_compare(output, expected)
                    pre_final_results[current_language] = pre_final_results.get(current_language, True) and test_result
                    if not test_result:
                        print('\tinput ="%s"\n'%open(current_dat).read(), 
                            '\toutput = "%s"\n'%output,
                              '\n\texpected = "%s"'%expected)
                except Exception as ec:
                    print('check failed:', ec)

for t in range(4):
    print()
                    
for user, results_per_user in results.items():
    print(user)
    for problem, stats_for_user_problem in results_per_user.items():
        print("\t", problem)
        for language, result in stats_for_user_problem.items():
            print("\t\t", language, result)
            
            
