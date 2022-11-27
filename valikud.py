#neid valikuid saame kasutada küsimuste valimisel
import random
def valik(n):
    valik1=random.randint(1,n)
    valik2=random.randint(1,n)
    while valik1==valik2:
        valik2=random.randint(1,n)
    valik3=random.randint(1,n)
    while valik3==valik2 or valik3==valik1:
        valik3=random.randint(1,n)
    return valik1, valik2, valik3