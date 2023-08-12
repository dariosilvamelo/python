import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1'],  # usado no windows
    # ['ping', '127.0.0.1', '-c', '4'], usado no linux e mac
    capture_output=True,  # o resultado não vai sair no terminal vai para a variavel
    text=True  # ter a saida em modulo texto.
)

saida = proc.stdout
print(saida)
