numberList = []
numberList = list()
numberList.append(10)
numberList.append("가")
numberList.append([1, 2, 3, True])
print(numberList)

nameDict = {}
nameDict = dict()
nameDict["name1"] = "권민창"
nameDict = {"name1": "권민창", "name2": "권민"}
print(nameDict["name1"])
print(nameDict.get("name1"))
print(nameDict.keys())
print(nameDict.values())
print(nameDict.items())

nameList = ["권민창", "권민"]
nameTuple = ("권민창", "권민")
for name in nameList:
    print(name)
for name in nameTuple:
    print(name)

nameList2 = nameList + list(nameTuple)      # 새로운 변수 사용 (주소값이 다름)
nameList.extend(nameTuple)      # 기존 변수 사용(주소값이 같음)
print(nameList2)
