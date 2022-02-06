from django.apps import AppConfig


class MealConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "meal"

    def function(self):
        import meal.signals
