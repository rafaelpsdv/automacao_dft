import os
import shutil
import psutil
from time import sleep


# Setting variables, parameter, final and variation.
param_c = 18.0
final_c = 8
var_c = -2
quantumexpress_process = ''
path = os.getcwd()
input_name = 'pt.scf.in'
output_name = 'pt.scf.out'

# READING INITIAL INPUT FILE
with open(f'{path}/{input_name}', 'r') as file:
    text = file.readlines()

# PARAM C IS IN LINE 12

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

    # RUNNING QUANTUM EXPRESS
    os.system(f'~/qe-7.0/bin/pw.x < {input_name} > {output_name}')

    # VERIFYING IF QUANTUM EXPRESS PROCCESS IS RUNNING BEFORE CONTINUE
    process_exists = True 
    while process_exists == True:
        process = [proc.name() for proc in psutil.process_iter()]
        if quantumexpress_process not in process:
            process_exists = False
            os.rename(f'{path}/{output_name}', f'{path}/ptC{param_c}.out')
        else:
            sleep(60*20)
            
    #REMOVE OUTPUT FILE
    print(f'AVISO! Cálculos para {param_c} finalizados!')
    os.remove(output_name)
    param_c += var_c

print('Todas os dados foram gerados e coletados.')
