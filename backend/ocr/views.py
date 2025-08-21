import pytesseract
from PIL import Image
from django.http import JsonResponse

def ocr_view(request):
    # Example: open an image and extract text
    image = Image.open('path/to/image.png')
    text = pytesseract.image_to_string(image)
    return JsonResponse({'text': text})