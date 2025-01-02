# qrscanner/views.py

from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from io import BytesIO

def generate_qr_code(request):
    # The address to encode in the QR code
    address = "https://maps.app.goo.gl/4Ajq2bpKJcQh5yY3A"
    
    # Create the QR code instance
    qr = qrcode.QRCode(
        version=1,  # QR code version (1 is the smallest size)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L is the lowest)
        box_size=10,  # Size of each box (unit for each module in the QR code)
        border=4,  # Border size
    )
    
    # Add data (address) to the QR code
    qr.add_data(address)
    qr.make(fit=True)
    
    # Create an image of the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a BytesIO object to send it as a response
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # Return the image as an HTTP response
    return HttpResponse(img_io, content_type='image/png')

def display_qr_code(request):
    return render(request, 'qrscanner/display_qr.html')