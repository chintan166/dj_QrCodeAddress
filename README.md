http://127.0.0.1:8016/qrscanner/generate_qr/

pip install qrcode[pil]

django-admin startproject qr_code_project

cd qr_code_project/

django-admin startapp qrscanner

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver 8016


![image](https://github.com/user-attachments/assets/a9485e5b-9c26-4529-95f0-93692ee5cf6c)

scan the QR and get my current address
