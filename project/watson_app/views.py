from rest_framework.response import Response
from rest_framework.views import APIView
from watson_app.serializers import FileSerializer
from watson_app.watson_services import WatsonService


class FileUploadView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.FILES)
        if serializer.is_valid(raise_exception=True):
            file = request.FILES["file"]
            service = WatsonService()
            result = service.add_document(file=file)
            return Response(result)

