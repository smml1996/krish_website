import time
import json
from collections import deque
from utils import get_remedies


chapter_name = "HEARING"
f = open(f"data/chapter_{chapter_name}.json", "r")
symptoms = json.loads(f.read())
f.close()

remedies = []
for symptom in symptoms["data"]:
    if symptom["RemediesCount"] > 0:
        try:
            remedies_ = get_remedies(symptom["ParentSymptomId"], symptom["SymptomId"])
            if remedies_ is not None:
                remedies_["symptom_"] = symptom
                remedies.append(remedies_)
            if (len(remedies) % 20 == 0) and (len(remedies) > 0):
                data = {"data": remedies}
                f = open(f"data/remedies/chapter_{chapter_name}.json", "w")
                f.write(json.dumps(data))
                f.close()
            time.sleep(1)
        except Exception as e:
            print(e)
            break

data = {"data": remedies}
f = open(f"data/remedies/chapter_{chapter_name}.json", "w")
f.write(json.dumps(data))
f.close()
    
    