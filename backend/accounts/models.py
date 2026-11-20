from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Benutzer der Lernplattform.

    Vorerst identisch mit dem Django-Standardbenutzer. Rollen
    (Schüler, Lehrkraft, Administrator) folgen in #11/#13.
    """
