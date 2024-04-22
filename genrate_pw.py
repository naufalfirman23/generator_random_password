import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
symbol = "!@$%^&*()\/?><|"

use_for = lower_case + upper_case + num +  symbol 

panjang_pw = 55

pw = "".join(random.sample(use_for, panjang_pw))

kode = "U2FsdGVkX"+pw

print(kode)


