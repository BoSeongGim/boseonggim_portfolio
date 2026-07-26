"""
a=[ [[0 for col in range(3)]
      for row in range(4)]
    for depth in range(2) ]
print(a)
#3차원으로까지 할 수 있어야 합니다. 3차원까지 많이 다룸.
#리스트[높이인덱스][세로인덱스][가로인덱스]
"""

'''
print('Hello, world!'.replace('world','Python') )#출력시 world->Python으로 바뀜.

s = 'Hello, wrold'
s = s.replace('world!','Python')#출력시 world->Python으로 바뀜.
print(s)
'''

'''
table = str.maketrans('aeiou','12345')
print('apple'.translate(table))
'''

"""
print('apple pear grape pineapple orange'.split())
print('apple, pear, grape,pineapple, orange'.split(','))
"""
'''
print(' '.join(['apple', 'pear', 'grape', 'pineapple','orange']) )
print('-'.join(['apple','pear', 'grape', 'pineapple','orange']) )
'''
"""
print('python'.upper() )
print('PYTHON'.lower())
"""
'''
print('   Pyhton   '.lstrip())
print('   Python   '.rstrip())
print('   Python   '.strip())
'''
"""
print(',. python,. '.lstrip(',.') )
print(',. python ,.'.rstrip(',.') )
print(',. python ,.'.strip(',.') )
"""

'''
print('python'.ljust(10) )
print('python'.rjust(10) )
print('python'.center(10) )
'''

"""
print('python'.rjust(10).upper())
"""

'''
print('35'.zfill(4) )
print('3.5'.zfill(6) )
print('hello'.zfill(10) )
'''

print('apple pineapple'.find('pl') )
print('apple pineapple'.find('xy') )

print('apple pineapple'.rfind('pl') )
print('apple pineapple'.rfind('xy') )

print('apple pineapple'.index('pl') )









