#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s.split(":")
    if s[-2:] == 'AM':
        if time[0] == "12":
            time[0] = "00"
    else:
        if time[0] != "12":
            time[0] = str(int(time[0]) + 12)
    ntime = ':'.join(time)
    return str(ntime[:-2])

##################################################
#   [0][1][2]
#   [09][:][30PM]
#   09:30PM
#   é AM? -> Não
#   Entra no Elser
#       Tempo [0] é 12? --> Não
#       Então o valor é somado com 12, no caso 09 + 12 -> 21:30
#
#   12:40AM
#   é AM? -> SIm
#   Entra no primeiro IF
#       [-2:] valida o valor da segunda posição de tras para frente, o ':' é usado para validar
#                                                                              Oque esta depos da segunda posição
#        Exemplo: 09:30PM -> o -'valor': realiza a validação da seguinte forma:
#                 M -> [-1]
#                 P -> [-2]
#                 0 -> [-3] e assim por diante
#           
#                 O ":' 'pega' o balor -2 nesse caso e tudo oque estiver a frente dele, no caso o 'M'
#
#   O tempo na posição [0] é 12? -> sim
#   Então altera 12 por 00
###################################################

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
