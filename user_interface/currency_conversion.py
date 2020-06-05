import requests
import json
from user_interface.models import Unit, UpdateCurrency


DATAURL = 'https://currencyapi.net/api/v1/rates?key=Vq8ah6d63jYVhatHWDJB8u0h18yMD4xKH2ts&base=USD&limit=AED,GBP'

def update_current_exchange_rates():
    file = requests.get(DATAURL)
    try:
        decoded = file.content.decode("utf-8")
        dict = json.loads(decoded)
        print(dict)
        if dict['valid']:
            rates = dict['rates']
            for currency in rates.keys():
                record = Unit.objects.get(unit__contains=currency)
                record.to_base_multiplier = 1/rates[currency]
                record.save()
        timestamp_record = UpdateCurrency.objects.get(id=1)
        timestamp_record.timestamp = dict['updated']
        timestamp_record.save()
        return dict['updated']
    except:
        timestamp_record = UpdateCurrency.objects.get(id=1)
        return timestamp_record.timestamp
