from datetime import datetime, timedelta
import requests
import os
import json


classification_mapping = {
    "Extreme Greed": "极度贪婪",
    "Greed": "贪婪",
    "Neutral": "中立",
    "Fear": "恐惧",
    "Extreme Fear": "极度恐惧"
}

def map_classification(classification):
    return classification_mapping.get(classification, "未知分类")

def fetch_fear_and_greed_index():
    url = "https://api.alternative.me/fng/"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            value = data["data"][0]["value"]
            classification = data["data"][0]["value_classification"]
            date = datetime.fromtimestamp(int(data["data"][0]["timestamp"])).strftime('%Y-%m-%d')

            return {
                "date": date,
                "value": value,
                "classification": classification
            }
        else:
            return {"error": f"HTTP Error: {response.status_code}"}
    except requests.RequestException as e:
        return {"error": "Network Error", "details": str(e)}

def save_fng_data(data, filename="./data/fear_and_greed.json"):
    latest_data = []

    if os.path.exists(filename):
        with open(filename, "r") as file:
            latest_data = json.load(file)

    latest_data = [record for record in latest_data if record["date"] != data["date"]]
    latest_data.append(data)
    latest_data = sorted(latest_data, key=lambda x: x["date"], reverse=True)[:2]

    with open(filename, "w") as file:
        json.dump(latest_data, file, indent=4)

def load_fng_data(filename="../data/fear_and_greed.json"):
    if not os.path.exists(filename):
        return None, None

    with open(filename, "r") as file:
        data = json.load(file)

    for record in data:
        if "classification" in record:
            record["classification"] = map_classification(record["classification"])

    today = data[0] if len(data) > 0 else None
    yesterday = data[1] if len(data) > 1 else None
    return today, yesterday

def load_stablecoin_data(filename="./data/stablecoin_data.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)

def save_stablecoin_data(data, filename="./data/stablecoin_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def get_yesterday_date():
    return (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

def update_stablecoin_data(new_data, filename="./data/stablecoin_data.json"):
    data = load_stablecoin_data(filename)

    existing_dates = [record["date"] for record in data]
    if new_data["date"] in existing_dates:
        for record in data:
            if record["date"] == new_data["date"]:
                record.update(new_data)
    else:
        data.append(new_data)

    data = sorted(data, key=lambda x: x["date"], reverse=True)[:2]
    save_stablecoin_data(data, filename)

