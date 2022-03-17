# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:13:28 2022

@author: nikheel
"""

# https://aws.amazon.com/premiumsupport/knowledge-center/lambda-python-runtime-errors/

import os
import sys

    
def create_layer(module):
    layer_name = f'{module}_module'
    
    commands = [
        
        f'mkdir -p {layer_name}/python',
        f'pip install {module} -t {layer_name}/python > /dev/null 2>&1',
        f'(cd {layer_name} && zip -r ../{layer_name}.zip ./) > /dev/null 2>&1',
        f'rm -rf {layer_name}'
        ]
    
    for command in commands:
        os.system(command)
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Define Python Module")
        exit()
    create_layer(sys.argv[1])

