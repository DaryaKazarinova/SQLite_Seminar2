from database import DatabaseConnection
from services import IngredientService, MealService
from ui import ConsolePrinter, Presenter, View


db = DatabaseConnection()
ingredient_service = IngredientService(db)
meal_service = MealService(db)
view = View()
presenter = Presenter(ingredient_service, meal_service, view)
presenter.run()
db.close_connection()

#comments to commit