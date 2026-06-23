import subprocess
import sys

def run_step(script, step_name):
    print(f"\n{'='*40}")
    print(f"Ejecutando: {step_name}")
    print(f"{'='*40}")
    
    result = subprocess.run(
        [sys.executable, script], 
        capture_output=False
    )
    
    if result.returncode != 0:
        print(f"\nError en {step_name}. Pipeline detenido.")
        sys.exit(1)
    
    print(f"{step_name} completado.")

if __name__ == "__main__":
    run_step("src/extract.py",   "Extract — Obteniendo datos de la API")
    run_step("src/transform.py", "Transform — Limpiando y transformando")
    run_step("src/load.py",      "Load — Subiendo a S3")
    
    print(f"\n Pipeline completado exitosamente.")