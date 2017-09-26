#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random


n = 10
chars = string.ascii_letters + string.digits
random_str = ''.join([random.choice(chars) for i in range(n)])
print(random_str)


