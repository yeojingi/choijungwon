DEBUG = True
HOST = 'http://localhost:8000'
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'jwchoi'
    }
}
OAUTH2_PROVIDERS = {
    'GOOGLE': {
        'NAME': 'GOOGLE',
        'CLIENT_ID': '889625545499-v68fqnguq28bc6k2q3r0qam7j74vjqaj.apps.googleusercontent.com',
        'SECRET': 'n_81pa9htT4ap5DadOrNzI7g',
        'LOGIN_URI': 'https://accounts.google.com/o/oauth2/v2/auth?scope=openid+profile+email&response_type=code&client_id={0[CLIENT_ID]}&redirect_uri={0[CALLBACK_URI]}&state={1}',
        'TOKEN_URI': 'https://www.googleapis.com/oauth2/v4/token',
        'CALLBACK_URI': f'{HOST}/oauth2/google/callback/',
        'DROPOUT_URI': 'https://accounts.google.com/o/oauth2/revoke?token={0}',
        'API_KEY': 'AIzaSyBkh4ZHYaK8o_VEVWwRliyTBYwCmZgLS0M',
        'TRANSLATION_URI': 'https://www.googleapis.com/language/translate/v2?key={0[API_KEY]}'
    },
}
