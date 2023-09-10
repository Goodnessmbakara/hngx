from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
import datetime

import pytz

# Create your views here.

class InformationView(APIView):
    def get(self, request):
        slack_name = request.GET.get('slack_name', '')
        track = request.GET.get('track', '')
        current_day = datetime.datetime.now().strftime('%A')
        utc_time = datetime.datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        github_file_url = 'https://github.com/Goodnessmbakara/hngx/blob/taskOne/get_endpoints/views.py'
        github_repo_url = 'https://github.com/Goodnessmbakara/hngx'

        return Response({
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': utc_time,
            'track': track,
            'github_file_url': github_file_url,
            'github_repo_url': github_repo_url,
            'status_code': 200,})

class PersonView(
