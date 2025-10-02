import pandas as pd
import requests
import os
import json


FIGHTERS_URL = "https://boxing-data-api.p.rapidapi.com/v1/fighters/"
DIVISIONS_URL = 'https://boxing-data-api.p.rapidapi.com/v1/divisions'

HEADERS = {
        "x-rapidapi-key": f'{os.environ['RAPID_API_KEY']}'
	    #"x-rapidapi-host": "boxing-data-api.p.rapidapi.com"
    }

def fighters():
    endpoint_url = FIGHTERS_URL

    data = requests.get(endpoint_url, headers=HEADERS)

def divisions():
    endpoint_url = DIVISIONS_URL

    data = requests.get(endpoint_url, headers=HEADERS)

    file_path = "weight_class.json"
    with open(file_path, "w") as json_file:
        json.dump(data.json(), json_file, indent=4)

def read_weight_class():
    try:
        with open('weight_class.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: 'your_file.json' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'your_file.json'.")

def weight_class_boxers_to_json():

    """
    Create the json that will be used
    Done this way because of limit of 100 / Month Hard Limit of Requests for the API
    :return:
    """
    weight_classes: list[dict] = read_weight_class()
    endpoint_url = FIGHTERS_URL

    for weight_class in weight_classes:
        class_name = weight_class['name']
        class_id = weight_class['id']
        final_url = endpoint_url + class_id
        if class_name in ["Heavyweight", "Middleweight", "Lightweight"]:
            params = {
                'page_size': 100
            }
            data = requests.get(endpoint_url, headers=HEADERS, params=params)

            file_path = f"{class_name}.json"
            with open(file_path, "w") as json_file:
                json.dump(data.json(), json_file, indent=4)

def row_with_json(fighter_data):

    name = fighter_data['name']
    age = fighter_data['age']
    debut = fighter_data['debut']
    nationality = fighter_data['nationality']
    stance = fighter_data['stance']
    reach = fighter_data['reach']
    total_bouts = fighter_data['stats']['total_bouts']
    wins = fighter_data['stats']['wins']
    if wins > total_bouts:
        wins, total_bouts = total_bouts, wins

    winrate = round(wins / total_bouts * 100, 2)
    total_rounds = fighter_data['stats'].get('total_rounds')
    ko_wins = fighter_data['stats']['ko_wins']
    ko_percentage = fighter_data['stats'].get('ko_percentage')

    return [name, age, debut, nationality, stance, reach, total_bouts, wins, winrate, total_rounds, ko_wins, ko_percentage]

def json_to_final_csv():
    df = pd.DataFrame()
    data = []
    columns = ['Name', 'Age', 'Debut', 'Nationality', 'Stance', 'Reach', 'Total_Bouts', 'Wins', 'Winrate', 'Total_Rounds', 'Ko_Wins', 'Ko_Percentace']

    try:
        with open('Heavyweight.json', 'r') as f:
            heavyweight_data = json.load(f)
            for fighter_data in heavyweight_data:
                row = row_with_json(fighter_data)
                if row not in data:
                 data.append(row)
        with open('Lightweight.json', 'r') as f:
            lightweight_data = json.load(f)
            for fighter_data in lightweight_data:
                row = row_with_json(fighter_data)
                if row not in data:
                    data.append(row)
        with open('Middleweight.json', 'r') as f:
            middleweight_data = json.load(f)
            for fighter_data in middleweight_data:
                row = row_with_json(fighter_data)
                if row not in data:
                    data.append(row)
    except FileNotFoundError:
        print("Error: 'your_file.json' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'your_file.json'.")
    finally:
        df = pd.DataFrame(data, columns=columns)
        df.to_csv("fighters_data.csv", index= False)

def main():
    # fighters()
    # divisions()
    # weight_class_boxers_to_json()
    json_to_final_csv()


if __name__ == '__main__':
    main()