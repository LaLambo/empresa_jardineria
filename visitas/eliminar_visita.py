import os
import django
from visitas.models import Visita

# Configuración del entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empresa_jardineria.settings')
django.setup()

def eliminar_visita(visita_id):
    # Obtener la visita por su ID
    visita = Visita.objects.get(id=visita_id)

    # Eliminar la visita
    visita.delete()

    # Confirmación de eliminación
    print(f"Visita con ID {visita_id} eliminada correctamente.")

if __name__ == "__main__":
    import sys
    eliminar_visita(int(sys.argv[1]))