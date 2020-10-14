import json
import xml.etree.ElementTree as etree


class JsonElementExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def dataextraction_factory(filepath):
    if filepath.endswith("json"):
        extractor = JsonElementExtractor
    elif filepath.endswith("xml"):
        extractor = XMLDataExtractor
    else:
        raise ValueError(f"Cannot extract data from {filepath}")
    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    sqlite_factory = extract_data_from("data/dump.sq3")
    print()
    json_factory = extract_data_from("data/movies.json")
    json_data = json_factory.parsed_data
    print(f"Found: {len(json_data)} movies")
    for movie in json_data:
        print(f"Title: {movie['title']}")
        rank = movie["rank"]
        if rank:
            print(f"Rank: {rank}")
        movie_id = movie["id"]
        if movie_id:
            print(f"Movie ID: {movie_id}")
        print()
    xmlfactory = extract_data_from("data/person.xml")
    xmldata = xmlfactory.parsed_data
    liars = xmldata.findall(".//person[lastName='Liar']")
    print(f"Found: {len(liars)} persons")
    for liar in liars:
        first_name = liar.find("firstName").text
        print(f"First name: {first_name}")
        last_name = liar.find("lastName").text
        print(f"Last name: {last_name}")
        [print(f"phone number ({p.attrib['type']}):", p.text) for p in liar.find("phoneNumbers")]
        print()


if __name__ == "__main__":
    main()
