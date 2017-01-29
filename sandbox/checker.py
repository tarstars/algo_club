#!/usr/bin/python3

import glob
import subprocess

user_prefix = 'users/'
problem_prefix = 'problems/'

users = glob.glob(user_prefix + '*')
problems = glob.glob(problem_prefix + '*')

users = [t[len(user_prefix):] for t in users]
problems = [t[len(problem_prefix):] for t in problems]

results = {}

for current_user in users:
    results[current_user] = {}
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
                program = solutions_path + current_language + '/main.py'
                print ('check program ', program, ' with input ', current_dat, ' and output', current_res)
                try:
                    program_instance = subprocess.Popen(['/usr/bin/python3', program],
                                                        stdin=subprocess.PIPE,
                                                        stdout=subprocess.PIPE,
                                                        universal_newlines = True)
                    output = program_instance.communicate(open(current_dat).read())[0]
                    expected = open(current_res).read()
                    print('\toutput = "%s"'%output, ' expected = "%s"'%expected)
                    pre_final_results = results[current_user][current_problem]
                    pre_final_results[current_language] = pre_final_results.get(current_language, True) and output == expected 
                except:
                    print('check failed')

print(results)
            
            
