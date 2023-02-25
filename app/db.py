from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = { 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zerodb',
        'USER': 'zero_adm',
        'PASSWORD': 'Z3r0.4dm*',
        'HOST': 'postgresql.zero.com',
        'PORT': '5432'
    }
}