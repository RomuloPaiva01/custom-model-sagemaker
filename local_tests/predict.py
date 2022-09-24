from io import StringIO
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
import requests

# test data
iris = datasets.load_iris()
x = iris.data
y = iris.target
_, X_test, _, _ = train_test_split(x, y, test_size=0.3, random_state=0)

X_test = pd.DataFrame(data=X_test, columns=['var1', 'var2', 'var3', 'var4']).head(3)

csv_buffer = StringIO()
X_test.to_csv(csv_buffer, index=False)
body = csv_buffer.getvalue()

# check if container is working
ping_status = requests.get("http://localhost:8080/ping")

print(ping_status)

# request inference from docker
r = requests.post("http://localhost:8080/invocations", data=body)

print(r.text)
print(r)