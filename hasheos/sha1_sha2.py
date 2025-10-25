import hashlib
from rich.table import Table
from rich.console import Console

console = Console()

def mostrar_hashes(texto: str):
    data = texto.encode()
    algoritmos = ["sha1", "sha224", "sha256", "sha384", "sha512"]

    table = Table(title="SHA-1 y SHA-2")
    table.add_column("Algoritmo", style="cyan")
    table.add_column("Hash", style="white")

    for algo in algoritmos:
        h = hashlib.new(algo, data).hexdigest()
        table.add_row(algo, h)

    console.print(table)
