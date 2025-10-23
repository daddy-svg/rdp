import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
# Code By : @BesicCode
num = input("Enter Vehicle Number: ")

ua = generate_user_agent()
h = {
    "User-Agent": ua,
}
c = f"https://vahanx.in/rc-search/{num}"
r = requests.get(c, headers=h)
soup = BeautifulSoup(r.text, 'html.parser')
# Code By : @BesicCode
data = {
    "Owner Name": None,
    "Father's Name": None,
    "Owner Serial No": None,
    "Model Name": None,
    "Maker Model": None,
    "Vehicle Class": None,
    "Fuel Type": None,
    "Fuel Norms": None,
    "Registration Date": None,
    "Insurance Company": None,
    "Insurance No": None,
    "Insurance Expiry": None,
    "Insurance Upto": None,
    "Fitness Upto": None,
    "Tax Upto": None,
    "PUC No": None,
    "PUC Upto": None,
    "Financier Name": None,
    "Registered RTO": None,
    "Address": None,
    "City Name": None,
    "Phone": None
}
# Code By : @BesicCode
for label in data:
    div = soup.find("span", string=label)
    if div:
        parent_div = div.find_parent("div")
        if parent_div:
            p_tag = parent_div.find("p")
            if p_tag:
                data[label] = p_tag.get_text(strip=True)

for label, value in data.items():
    print(f"{label}: {value}")
