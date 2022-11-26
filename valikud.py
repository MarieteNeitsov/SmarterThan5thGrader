#neid valikuid saame kasutada küsimuste valimisel
import random
def valik():
    valik1=random.randint(1,3)
    valik2=random.randint(1,3)
    while valik1==valik2:
        valik2=random.randint(1,3)
    valik3=random.randint(1,3)
    while valik3==valik2 or valik3==valik1:
        valik3=random.randint(1,3)
    return valik1, valik2, valik3