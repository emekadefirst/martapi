from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def custom_validation(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()

    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError('Choose another email')

    if not password or len(password) < 8:
        raise ValidationError('Choose another password, minimum 8 characters')

    if not username:
        raise ValidationError('Choose another username')

    return data

def validate_firstname(data):
    firstname = data.get('firstname', '').strip()
    if not firstname:
        raise ValidationError('First name is required')
    return True

def validate_lastname(data):
    lastname = data.get('lastname', '').strip()
    if not lastname:
        raise ValidationError('Last name is required')
    return True

def validate_number(data):
    number = data.get('number', '').strip()
    if not number:
        raise ValidationError('Number is required')
    return True

def validate_street(data):
    street = data.get('street', '').strip()
    if not street:
        raise ValidationError('Street is required')
    return True

def validate_landmark(data):
    landmark = data.get('landmark', '').strip()
    if not landmark:
        raise ValidationError('Landmark is required')
    return True

def validate_lga(data):
    lga = data.get('lga', '').strip()
    if not lga:
        raise ValidationError('LGA is required')
    return True

def validate_state(data):
    state = data.get('state', '').strip()
    if not state:
        raise ValidationError('State is required')
    return True
