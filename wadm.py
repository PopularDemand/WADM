###Program helps user make decision by weighing choices mathematically

def _line_break():
	print '*' * 25

def get_choices():
	"""Gets decision choices from user"""
	choices = []
	more_choices = True

	while more_choices:
		choice = raw_input(("What is one option you're considering? "
			"If you are done inputting choices, enter 'done'."
			"\n>>>"))
		if choice == "done":
			more_choices = False
			_line_break()
		else:
			choices.append(choice)
			_line_break()

	return choices


def get_factors():
	"""Gets decision factors from user"""
	factors = {}
	more_factors = True

	while more_factors:
		factor = raw_input(("What is one factor to judge this decision (e.g family, climate, schooling)? "
			"If you are done inputting factors, enter 'done'."
			"\n>>>"))
		if factor == "done":
			more_factors = False
			_line_break()
		else:
			weight = int(raw_input(("On a scale of 1-10, how heavily do you weigh this factor?"
				"\n>>>")))
			factors[factor] = weight
			_line_break()
	
	return factors


def evaluate():
	"""Does the math to determine which decision is better"""
	choices = get_choices()
	factors = get_factors()
	choice_totals = {}

	for choice in choices:
		total = 0
		for factor in factors:
			rating = int(raw_input("On a scale of 1-10, how would you rate %s for %s?" 
				"\n>>>" % (choice, factor)))
			total += (rating*factors[factor])
			choice_totals[choice] = total
			_line_break()

	return choice_totals


def run_matrix():
	"""Prints out final product"""
	goal = raw_input("What decision do you need help with?\n>>>")
	print "Okay, let's get started with that.\n"
	_line_break()

	choice_totals = evaluate()

	for choice in choice_totals:
		print "The decision to %s scored %d.\n" % (choice, choice_totals[choice])

	print "The higher the score, the more likely you should do it! Good luck!"