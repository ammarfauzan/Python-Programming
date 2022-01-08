def calculator(x, y, metode='penjumlahan'):
    """
    Objective
    Function Calculator for basic artimatic 2 variable number
    
    Arguments:
    - x = first number, type integer
    - y = second number, type integer
    - metode = (default 'penjumlahan'), 
        expected values: [penjumlahan, pengurangan, pembagian, perkalian, pangkat]
    """
    
    metode = metode.lower()
    if metode == 'penjumlahan':
        result = x+y
    elif metode == 'pengurangan':
        result = x-y
    elif metode == 'pembagian':
        result = x/y
    elif metode == 'perkalian':
        result = x*y
    elif metode == 'pangkat':
        result = x**y
    else:
        result = '-'
        print('Inputan tidak sesuai!')
    return result

def calculator_super(x, y, z=None, metode='penjumlahan'):
    """
    Objective
    Function Calculator for basic artimatic 3 variable number
    
    Arguments:
    - x = first number, type integer
    - y = second number, type integer
    - z = third number, type integer
    - metode = (default 'penjumlahan'), 
        expected values: [penjumlahan, pengurangan, pembagian, perkalian, pangkat]
    """
    
    metode = metode.lower()
    if metode == 'penjumlahan':
        result = x+y+z
    elif metode == 'pengurangan':
        result = x-y-z
    elif metode == 'pembagian':
        result = x/y/z
    elif metode == 'perkalian':
        result = x*y*z
    elif metode == 'pangkat':
        result = x**y
    else:
        result = '-'
        print('Inputan tidak sesuai!')
    return result
