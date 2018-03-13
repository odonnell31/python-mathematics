def decile(array, score, kind='weak'):
	"""
	Accepts an array of values and a singleton score.
	
	The score is run against the array to determine its percentile score.

	The value is then translated into a decile grouping and returned as an integer.
	
	By default, the percentile method used is weak. Others are detailed in the documentation below.
	
	h3. Example usage
	
		>>> import calculate
		>>> calculate.decile([1, 2, 3, 3, 4], 3)
		9
	
	h3. Dependencies
	
		* "scipy":http://www.scipy.org/SciPy
	
	h3. Documentation
	
		* "percentile rank":http://en.wikipedia.org/wiki/Percentile_rank
		* "decile":http://en.wikipedia.org/wiki/Decile
	
	"""
	from calculate import percentile
	
	if not isinstance(array, list):
		raise TypeError('first value input must be a list')
	percentile_score = percentile(array, score, kind=kind)
	if percentile_score == 100.0:
		return 10
	else:
		decile = int(percentile_score * 0.1) + 1
		return decile