from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document
from .serializer import DocumentSerializer
from django.core.files.storage import default_storage
import pytesseract
from PIL import Image

class DocumentUploadView(APIView):
    def post(self, request, format=None):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Save uploaded file
        file_path = default_storage.save(file.name, file)

        # Open image and run Tesseract OCR
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)

        # Save document in DB
        document = Document.objects.create(file=file, content=text)
        serializer = DocumentSerializer(document)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DocumentListView(APIView):
    def get(self, request, format=None):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)
