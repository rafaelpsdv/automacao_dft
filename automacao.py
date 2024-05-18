import os
import shutil
from time import sleep

path = os.getcwd()

input_name = 'pt.scf.in'
output_name = 'pt.scf.out'

with open(f'{path}/{input_name}', 'r') as file:
    text = file.readlines()

# PARAM C IS IN LINE 12

# Defining parameter, final and variation.
param_c = 18.0
final_c = 8
var_c = -2

while param_c > final_c -1:
    print(f'AVISO! Iniciando cálculos para C = {param_c} ...')
    shutil.copyfile(input_name, f'TEMP{input_name}')
    text[12] = f'    C = {param_c},\n'
    try:
        with open(f'TEMP{input_name}', 'w') as file:
            file.writelines(text)
        os.remove(input_name)
        os.rename(f'TEMP{input_name}', input_name)
    except: 
        os.remove(f'TEMP{input_name}')
    os.system(f'~/qe-7.0/bin/pw.x < {input_name} > {output_name}')
    # VERIFY IF EXISTS THE OUTPUT FILE TO CONTINUE
    output_exists = False
    while output_exists == False:
        try:
            with open(f'{path}/{output_name}', 'r') as file:
                output_exists = True
        except IOError:
            sleep(60*20)
    #EXTRACT INFOS OF OUTPUT FILE


    #REMOVE OUTPUT FILE
    print(f'AVISO! Cálculos para {param_c} finalizados!')
    os.remove(output_name)

    param_c += var_c

print('Todas os dados foram gerados e coletados.')
