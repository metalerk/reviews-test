def get_or_none(model, *args, **kwargs):
	""" Helper function for Model.object.get() """

	try:
		return model.objects.get(*args, **kwargs)
	except model.DoesNotExist:
		return None


def get_ip_address(request, *args, **kwargs):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')

	return ip