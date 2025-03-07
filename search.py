import json

def load_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def search_json(data, key, value):
    return [item for item in data if item.get(key) == value and item.get("Synonyms") is not None]

def main():
    file_name = 'dic-bible.json'
    data = load_json(file_name)
    
    # Example search by Name
    result = search_json(data, "Name", "Aaron")
    print("Search by Name 'Aaron':")
    print(json.dumps(result, indent=2))
    
    # Example search by Synonyms
    result = search_json(data, "Synonyms", "Aharon")
    print("\nSearch by Synonyms 'Aharon':")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()