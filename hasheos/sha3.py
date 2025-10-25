import hashlib
from rich.table import Table
from rich.console import Console

console = Console()

def mostrar_hashes(texto: str):
    data = texto.encode()
    algoritmos = ["sha3_224", "sha3_256", "sha3_384", "sha3_512"]

    table = Table(title="SHA-3")
    table.add_column("Algoritmo", style="magenta")
    table.add_column("Hash", style="white")

    for algo in algoritmos:
        h = hashlib.new(algo, data).hexdigest()
        table.add_row(algo, h)

    console.print(table)
