from Practice_16_7_1 import Cat
import json
import urllib.request


with urllib.request.urlopen("http://130.193.37.179/api/pet/?page=1&page_size=6&species__name=%D0%BA%D0%BE%D1%88%D0%BA%D0%B0") as url:
    pets = json.load(url)
    all_cats = pets['results']


for cat in all_cats:
    cat_obj = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age=cat.get("age"))

    print(cat_obj.get_card_cat())