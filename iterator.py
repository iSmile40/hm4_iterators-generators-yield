import json

class CountriesIterate:

    def __init__(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            self.json_data = json.load(f)

    def __iter__(self):
        self.countries = []
        for country in self.json_data:
            self.countries.append(country['name']['common'])
        self.countries = iter(self.countries)
        return self

    def __next__(self):
        if not self.countries:
            raise StopIteration
        country = next(self.countries)
        link = 'https://en.wikipedia.org/wiki/' + country
        return f'{country} - {link} \n'

with open('countries_wiki.txt', 'w', encoding='utf-8') as d:
    for name in CountriesIterate("countries.txt"):
        d.write(name + '\n')
