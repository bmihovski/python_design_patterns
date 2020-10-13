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
        print(f"Title: {movie.title}")
