import hashlib
from rich.table import Table
from rich.console import Console

console = Console()

def mostrar_hashes(texto: str):
    data = texto.encode()
    algoritmo = "md5"

    table = Table(title="MD5")
    table.add_column("Algoritmo", style="magenta")
    table.add_column("Hash", style="white")

    h = hashlib.new(algoritmo, data).hexdigest()
    table.add_row(algoritmo, h)

    console.print(table)
