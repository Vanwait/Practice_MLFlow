import sys

# Esto lo que hace es mirar si se han pasado parámetros al ejecutar. En el caso de que los hayan pasado, los coge.
# Si no se han pasado, coge los valores por defecto.
alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

print(f'alpha: {alpha}, l1_ratio: {l1_ratio}')