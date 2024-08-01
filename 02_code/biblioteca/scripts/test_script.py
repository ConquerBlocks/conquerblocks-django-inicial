from books.models import Autor


def run():
    print(Autor.objects.all())
    print("Fin del script")
