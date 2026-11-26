import json
from src.model import train_model
if __name__=="__main__": print(json.dumps(train_model(),indent=2))
