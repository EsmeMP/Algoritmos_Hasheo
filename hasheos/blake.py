import hashlib
from rich.table import Table
from rich.console import Console
import blake3

console = Console()

def mostrar_hashes(texto: str):
    data = texto.encode()
    algoritmos = ["blake2b", "blake2s"]

    table = Table(title="BLAKE2 y BLAKE3")
    table.add_column("Algoritmo", style="green")
    table.add_column("Hash", style="white")

    # BLAKE2
    for algo in algoritmos:
        h = hashlib.new(algo, data).hexdigest()
        table.add_row(algo, h)

    # BLAKE3 (lib externa)
    h3 = blake3.blake3(data).hexdigest()
    table.add_row("blake3", h3)

    console.print(table)
