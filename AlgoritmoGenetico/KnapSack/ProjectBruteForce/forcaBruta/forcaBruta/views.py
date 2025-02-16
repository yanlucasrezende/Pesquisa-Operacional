from django.shortcuts import render
import subprocess
import os

def index(request):
    # Executa o algoritmo automaticamente ao carregar a página
    resultado = None
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(base_dir, 'algoritmo.py')
        
        execucao = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            check=True
        )
        resultado = execucao.stdout
        if execucao.stderr:
            resultado += f"\nErro: {execucao.stderr}"
    except Exception as e:
        resultado = f"Erro ao executar o algoritmo: {str(e)}"

    return render(request, "index.html", {"resultado": resultado})