from decouple import config, Csv

TOKEN = config('TOKEN')

SECRET_KEY = config('SECRET_KEY')

URL_ML='https://api.mercadolibre.com/sites/MLB/search'

URL_APPLICATION = config('URL_APPLICATION')