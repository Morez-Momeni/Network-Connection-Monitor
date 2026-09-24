import json 
import matplotlib.pyplot as plt



log_file = "logs/connections_for_dashboard.json"

with open(log_file,'r',encoding="utf-8") as file :
    logs = json.load(file)

def extrect_data():
    connections_id = []
    connection_duration = []
    for connection in logs:
        connections_id.append(connection["id"])
        connection_duration.append(connection["duration"])

    result = list(zip(connections_id,connection_duration))
    return result


data = extrect_data()

plt.figure(figsize=(10, 6))

for i, j in data:
    plt.bar(f"Connection {i}", j)
    plt.text(f"Connection {i}", j, f"{j:.2f}s", ha="center") # type: ignore


plt.xlabel("Connection ID")
plt.ylabel("Duration (seconds)")
plt.title("Connection Duration")

plt.grid(axis="y")

plt.show()