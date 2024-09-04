import time

class TiempoDeProcesamientoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Código que se ejecuta antes de que la vista sea llamada
        tiempo_inicio = time.time()

        response = self.get_response(request)

        # Código que se ejecuta después de que la vista ha sido llamada
        tiempo_fin = time.time()
        tiempo_total = tiempo_fin - tiempo_inicio

        # Añadir el tiempo de procesamiento a la respuesta como una cabecera HTTP
        response['X-Tiempo-De-Procesamiento'] = str(tiempo_total)
        print(tiempo_total)

        return response