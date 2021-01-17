# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:41:50 2020

@author: Asifulla K
"""

import string
import random
def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
id_generator()
'G5G74W'
id_generator(3, "6793YUIO")
'Y3U'
myquestion7.id_generator()
