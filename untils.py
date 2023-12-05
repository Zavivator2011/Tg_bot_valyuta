import requests


async def get_current_data():
    r = requests.get("https://nbu.uz/uz/exchange-rates/json/")
    if r.status_code == 200:
        return  r.json()
    
    
    
async def check_btn_text(data, selected_btn):
    for item in data:
        if selected_btn == item['code']:
            return True
        
    return False
    
async def make_data_context(data, text):
    for item in data:
        if text == item['code']:
            context = (f"{item['title']}\n\n"
                       f"1 {item['code']} == {item['cb_price']} so`m\n"
                       f"Sana: {item['date']}")
            return context
    
