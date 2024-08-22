# list all Tags in the dataset
import pandas as pd

data = pd.read_csv('training.csv')

tags = set()
for tag in data['Tag']:
    tags.add(tag)

print(tags)