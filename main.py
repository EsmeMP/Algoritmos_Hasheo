from hasheos import sha1_sha2, sha3, blake
from rich.console import Console

console = Console()

def main():
    console.rule("[bold blue]Herramienta de Hashing[/bold blue]")
    console.print("Selecciona el algoritmo:")
    console.print("1. SHA-1 / SHA-2 (224, 256, 384, 512)")
    console.print("2. SHA-3 (224, 256, 384, 512)")
    console.print("3. BLAKE2 / BLAKE3")
    opcion = input("Opción (1-3): ").strip()

    texto = input("Ingresa el texto a hashear: ")

    if opcion == "1":
        sha1_sha2.mostrar_hashes(texto)
    elif opcion == "2":
        sha3.mostrar_hashes(texto)
    elif opcion == "3":
        blake.mostrar_hashes(texto)
    else:
        console.print("[red]Opción no válida[/red]")

if __name__ == "__main__":
    main()