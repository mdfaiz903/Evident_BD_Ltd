from django.shortcuts import render
from .models import InputValues
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.method == 'POST':
        input_values_str = request.POST.get('input_values', '')
        search_value = request.POST.get('search_value', '')

        # Split the input_values_str and convert to integers
        input_values = [int(num.strip()) for num in input_values_str.split(',')]

        # Sort the input_values in descending order
        input_values.sort(reverse=True)

        # Get the logged-in user
        user = request.user

        # Store the input values in the database
        InputValues.objects.create(user=user, input_values=','.join(map(str, input_values)))

        # Check if the search value exists in the input values
        search_value_exists = int(search_value) in input_values

        # Render the template with the search result
        return render(request, 'main/khoj.html', {'search_result': search_value_exists})

    return render(request, 'main/khoj.html')



from . models import InputValues
def get_all_input_values(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id', None)
        start_datetime = request.GET.get('start_datetime', None)
        end_datetime = request.GET.get('end_datetime', None)

        # Validate the input parameters
        if user_id is None or start_datetime is None or end_datetime is None:
            return JsonResponse({"status": "error", "message": "Missing parameters."}, status=400)

        try:
            

            user = get_object_or_404(User, id=user_id)

            # Retrieve the input values within the date range for the user
            input_values = InputValues.objects.filter(user=user, timestamp__gte=start_datetime, timestamp__lte=end_datetime)

            # Prepare the response payload in JSON format
            payload = []
            for value in input_values:
                payload.append({
                    "timestamp": value.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    "input_values": value.input_values
                })

            # Create and return the JSON response
            response_data = {
                "status": "success",
                "user_id": int(user_id),
                "payload": payload
            }
            return JsonResponse(response_data)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)
