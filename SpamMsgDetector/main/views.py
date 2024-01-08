import csv
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Message

def Home(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'C:/Users/Lab1/projectDir/SpamMsgDetector/spam.csv')

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  

        for row in csv_reader:
         if len(row) >= 2:
            msg_type = row[0]
            msg = ','.join(row[1:])
            message = Message(type=msg_type,msg = msg)
            message.save()
         else:
          print(f"Ignoring row: {row} - Expected 2 columns, found {len(row)}")
    
    firstpage = loader.get_template('home.html')
    return HttpResponse(firstpage.render())

def SpamDetector(request):
   return HttpResponse("Hello")
