print("DataAccess Start")

#All requests are dictionaries
#If a request has required or optional fields,
#these are listed at the top of the function as dictionaries - requiredfields and optionalfields
#key - the expected key in the request dictionary
#value - the expected value type corresponding to the key in the request dictionary
#If fields are optional they still must follow their provided type in th optionalfields dictionary

#If an error occurs during any request, the error is returned

#Validation
#Check that a request has the appropriate request format
def CheckRequestFormat(request, requiredFields, optionalFields):
	if requiredFields is not None:
		for field in requiredFields.items():
			if field[0] not in request:
				return False
			elif type(request[field[0]]) is not field[1]:
				return False
	if optionalFields is not None:
		for field in optionalFields.items():
			if field[0] in request and type(request[field[0]]) is not field[1]:
				return False
	return True

#Validation failed error message
#Create an error message for a misformated request
def FormatErrorMessage(requiredFields, optionalFields):
	formaterrormessage = "Unexpected format! Expected:"
	if requiredFields is not None:
		formaterrormessage += "\nRequired:"
		for field in requiredFields.items():
			formaterrormessage += "\n" + field[0] + " as " + field[1].__name__
	if optionalFields is not None:
		formaterrormessage += "\nOptional:"
		for field in optionalFields.items():
			formaterrormessage += "\n" + field[0] + " as " + field[1].__name__
	return formaterrormessage

print("DataAccess End")