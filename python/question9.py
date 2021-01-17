# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:24:48 2020

@author: Asifulla K
"""
import string
import random
def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
id_generator()
'pENTA$89'
id_generator(16, 'PentagonSpace#12')
