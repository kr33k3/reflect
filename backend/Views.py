from Models.User import User, Recipe, Ingredient, Step

printErrors = False

#If an error occurs during any request, the error is returned

#SafeCommit
#If an error occurs on commit, rolls back the changes and returns the eroor
#Otherwise, returns the provided returnValue
def SafeCommit(session, returnValue):
	try:
		session.commit()
	except Exception as exception:
		session.rollback()
		ex_str = exception.__str__() #type(exception).__name__
		if printErrors:
			print("\nError: " + ex_str + "\n\n")
		return ex_str
	else:
		return returnValue if returnValue is not None else "Success"

#Create User
#Creates a user
#_username, password - strings
def CreateUser(session, _username, _password):
	new_user = User(username = _username, password = _password)
	session.add(new_user)
	return SafeCommit(session, new_user)
	
#Create Ingredient
#Create an ingredient and add it to the Ingredient table
#_name - string
#output - new ingredient - Ingredient Model
def CreateIngredient(session, _name):
	new_ingredient = Ingredient(name = _name)
	session.add(new_ingredient)
	return SafeCommit(session, new_ingredient)

def CreateStep(session, _instructions, _order, _recipe):
	new_step = Step(instructions = _instructions, order = _order, Recipe = _recipe.name)
	session.add(new_step)
	return SafeCommit(session, new_step)
#Create Recipe
#Creates a new Recipe and adds it to the Recipe Table
#Adds ingredients that don't yet exist in the Ingredient table
#Adds RecipeIngredient relationship entires in the RecipeIngredient table 
#recipe - dict corrsponding to recipe requirements
#output - new recipe - Recipe Model
def CreateRecipe(session, recipe):
	new_recipe = Recipe(
		name = recipe["RecipeName"],
		MealType=recipe["MealType"],
		PrepTime=recipe["PrepTime"],
		Ingredients=[],
		Steps=[]
	)
	for ingredientName in recipe["Ingredients"]:
		new_recipe.Ingredients.append(GetIngredientByName(session, ingredientName))
	currentOrder = 1
	for step in recipe["Steps"]:
		new_recipe.Steps.append(Step(order = currentOrder, instructions = step))
		currentOrder += 1
	session.add(new_recipe)
	return SafeCommit(session, new_recipe)

#Validate login credientials
#username, password - strings
#output bool - True if valid credentials
def Login(session, username, password):
	validation = None
	try:
		validation = session.query(User).filter( \
			User.username==username, \
			User.password==password
			).first()
	except Exception as exception:
		session.rollback()
		ex_str = exception.__str__()
		if printErrors:
			print("\nLogin Error: " + ex_str + "\n\n")
		return ex_str
	else:
		return validation != None

#Get all ingredients
#output - list of ingredients (strings) 
def GetAllIngredients(session):
	ingredientsList = []
	for ingredient in session.query(Ingredient).all():
		ingredientsList.append(ingredient.to_str())
	return ingredientsList

#Get an ingredient by its name, if it doesn't exist, create it
#ingredientName - string
#output - Ingredient model class
def GetIngredientByName(session, ingredientName):
	ingredient = session.query(Ingredient).filter(Ingredient.name == ingredientName).first()
	if ingredient is not None:
		return ingredient
	else:
		return CreateIngredient(session, ingredientName)

#Set a user's ingredients
#username - string
#ingredientNames - list of ingredients (strings)
def SetUserIngredients(session, username, ingredientNames):
	user = session.query(User).filter(User.username == username).first()
	ingredients = []
	for ingredientName in ingredientNames:
		ingredients.append(GetIngredientByName(session, ingredientName))
	user.pantry = ingredients
	SafeCommit(session, None)

#Get a user's ingredients
#username - string
#output - list of ingredients (strings)
def GetUserIngredients(session, username):
	user = session.query(User).filter(User.username == username).first()
	ingredients = []
	for ingredient in user.pantry:
		ingredients.append(ingredient.to_str())
	return ingredients

#Get recipes that use only the given ingredients
#request - dict
#	required:
#		ingredients - list of strings
#	optional:
#		meal type - string
#		prep_time - integer
#output - list of recipe dictionaries
def GetRecipes(session, ingredients, meal_type, prep_time):
	recipes_with_ingredients = []
	recipes = None 
	try:
		recipes = session.query(Recipe)
		if meal_type is not None:
			recipes = recipes.filter(Recipe.MealType == meal_type)
		if prep_time is not None:
			recipes = recipes.filter(Recipe.PrepTime <= prep_time)
		recipes = recipes.all()
		for recipe in recipes:
			recipe_is_included = True
			recipe_dict = recipe.to_dict()
			for ingredient in recipe_dict["Ingredients"]:
				if ingredient not in ingredients:
					recipe_is_included = False
					break
			if (recipe_is_included):
				recipes_with_ingredients.append(recipe.searchresult_dict())
	except Exception as exception:
		session.rollback()
		ex_str = exception.__str__()
		if printErrors:
			print("\nGetRecipes Error: " + ex_str + "\n\n")
		return ex_str
	else:
		return recipes_with_ingredients

#Get recipe by name
#recipeName - recipe name (string)
#output - recipe (dict)
def GetRecipe(session, recipeName):
	return session.query(Recipe).filter(Recipe.name == recipeName).first().to_dict()

#Get all meal types
#output - list of meal types (strings)
def GetMealTypes(session):
	mealtypes = session.query(Recipe.MealType).distinct().all()
	to_return = []
	for mealtype in mealtypes:
		to_return.append(mealtype[0])
	return to_return