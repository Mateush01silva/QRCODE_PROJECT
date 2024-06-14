from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import qrcode
import io

def generate_qr(request):
    data = request.GET.get('data')
    if not data:
        return JsonResponse({'error': 'No data provided'}, status=400)
    
    # Gerar QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return HttpResponse(img_io, content_type='image/png')

