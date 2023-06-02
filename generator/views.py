from django.shortcuts import render
#from django.http import HttpResponse
import random
import string
import hashlib

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def password(request):
    
    characters = list(string.ascii_lowercase)
    
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))
        
    if request.GET.get('special'):
        characters.extend(list(string.punctuation))
    
    generated_password = ''
    lenght = int(request.GET.get('length'))         
    
    for x in range(lenght):
        generated_password += random.choice(characters)
        
        
        
    def check_strength(password):
        # Check the strength of the password based on criteria such as length, complexity, etc.
        # Return True if the password is strong enough, False otherwise.
        if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
            return "strong"
        else:
            return "weak"
        
    strength = check_strength(generated_password)
        
    def encrypt_password(password):
        # Encrypt the password using the SHA256 algorithm.
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
    
    encrypted_password = encrypt_password(generated_password)
    
        
    
    
    return render(request, 'pages/password.html', {
        'password': generated_password,
        'strength': strength,
        'hash': encrypted_password
        })

