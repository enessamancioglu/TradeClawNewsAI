import requests
import config

def post_to_square(content: str) -> str:
    url = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
    headers = {
        "X-Square-OpenAPI-Key": config.BINANCE_SQUARE_API_KEY,
        "Content-Type": "application/json",
        "clienttype": "binanceSkill"
    }
    data = {"bodyTextOnly": content}
    
    response = requests.post(url, headers=headers, json=data).json()
    
    if response.get("code") == "000000" and response.get("data", {}).get("id"):
        post_id = response["data"]["id"]
        return f"https://www.binance.com/square/post/{post_id}"
    return "Post failed or URL unavailable"
