#!/usr/bin/python3

import glob

user_prefix = 'users/'
problem_prefix = 'problems/'

users = glob.glob(user_prefix + '*')
problems = glob.glob(problem_prefix + '*')

users = [t[len(user_prefix):] for t in users]
problems = [t[len(problem_prefix):] for t in problems]

for current_user in users:
    for current_problem in problems:
        print('check problem=%s for user=%s'%(current_problem, current_user))
        dat_prefix = 'dat'
        res_prefix = 'res'
        problem_path = problem_prefix + current_problem + '/'
        dat_path = problem_path + dat_prefix
        res_path = problem_path + res_prefix
        print('\tdat_path=', dat_path)
        print('\tres_path=', res_path)
        dats = glob.glob(dat_path + '*')
        resources = glob.glob(res_path + '*')
        dats_suffixes = [t[len(dat_path):] for t in dats]
        print('\tdats_suffixes=', dats_suffixes)
        for current_suffix in dats_suffixes:
            current_res = res_path + current_suffix
            current_dat = dat_path + current_suffix
            print('\t\tcurrent_res = %s current_dat = %s' % (current_res, current_dat))
            
