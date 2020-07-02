from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


def handle_api_exception(exc, context):
	response = exception_handler(exc, context)

	if not response:
		exc = APIException(exc)
		response = exception_handler(exc, context)

	if response is not None:
		error_message = response.data.get('detail')
		response.data.pop('detail', {})
		response.data['success'] = False
		response.data['message'] = error_message
		response.data['status_code'] = response.status_code

	return response