import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    params = {"sort": "downloads", "direction": -1, "limit": 10}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        models = response.json()
        return models
    else:
        print("Failed to fetch data")
        return []

def generate_report(models):
    report = "Top 10 Downloaded Models on Hugging Face\n\n"
    for idx, model in enumerate(models, start=1):
        report += f"{idx}. {model['modelId']} - {model['downloads']} downloads\n"
    return report

def main():
    models = fetch_top_models()
    if models:
        report = generate_report(models)
        with open(r".\report.txt", "w") as file:
            file.write(report)
        print("Report generated successfully.")
    else:
        print("No data to generate report.")

if __name__ == "__main__":
    main()