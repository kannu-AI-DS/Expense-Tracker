import json, sys
from pathlib import Path

FILE = Path("expenses.json")

def load():
    return json.load(open(FILE)) if FILE.exists() else []

def save(data):
    json.dump(data, open(FILE, "w"), indent=2)

if len(sys.argv) < 2:
    print("Usage: python expenses.py [add|list]")
    exit()

cmd = sys.argv[1]
data = load()

if cmd == "add":
    item, amount = sys.argv[2], float(sys.argv[3])
    data.append({"item": item, "amount": amount})
    save(data)
    print(f"➕ Added {item} - ${amount}")
elif cmd == "list":
    total = sum(e["amount"] for e in data)
    for e in data:
        print(f"{e['item']}: ${e['amount']}")
    print(f"💰 Total: ${total}")
