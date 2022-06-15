from connectors import JSONConnector, XMLConnector, ConnectorsFactory


def connect_to_xml():
    xml_factory = ConnectorsFactory().get_connector("data/persons.xml")
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='{'Liar'}']")
    print(f"Found {len(liars)} persons")
    for liar in liars:
        print("First name: ", liar.find("firstName").text)
        print("Last name: ", liar.find("lastName").text)
        [print(f"{p.attrib['type']}: {p.text}") for p in liar.find("phoneNumbers")]


def connect_to_json():
    json_factory = ConnectorsFactory().get_connector("data/movies.json")
    json_data = json_factory.parsed_data
    print(f"Find {len(json_data)} movies")
    for movie in json_data:
        print()
        for tag in movie:
            print(f"{tag}: {movie[tag]}")


def main():
    connect_to_xml()
    print("--------------------")
    connect_to_json()


if __name__ == "__main__":
    main()
