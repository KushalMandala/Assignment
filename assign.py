from decimal import Decimal
from tabulate import tabulate


def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += Decimal(step)

#print(list(float_range(Decimal(18.5), 20, '0.01')))


def tableData(BMI):
	BMIcategory = ""
	HealthRisk = ""
	if BMI <= 18.4:
		BMIcategory = "Underweight"
		HealthRisk = "Malnutrition risk"

	if BMI in float_range(Decimal(18.5), 25, '0.01'):
		BMIcategory = "Normal weight"
		HealthRisk = "Low risk"

	if BMI in float_range(25, 30, '0.01'):
		BMIcategory = "Overweight"
		HealthRisk = "Enhanced risk"

	if BMI in float_range(30, 35, '0.01'):
		BMIcategory = "Moderately obese"
		HealthRisk = "Medium risk"

	if BMI in float_range(35, 40, '0.01'):
		BMIcategory = "Severely obese"
		HealthRisk = "High risk"

	if BMI >= 40:
		BMIcategory = "Very severely obese"
		HealthRisk = "Very high risk"

	return BMI, BMIcategory, HealthRisk


jsonlist = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
			{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
			{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
			{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
			{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
			{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]


finalData = []
headers = ["BMI", "BMIcategory", "HealthRisk"]
for items in jsonlist:
	HeightCm = items["HeightCm"]
	WeightKg = items["WeightKg"]

	CMtoM = HeightCm/100

	BMI = WeightKg/CMtoM**2
	BMI = round(BMI, 2)

	dictionary = dict(zip(headers, list(tableData(BMI))))
	new = {**items, **dictionary}
	finalData.append(new)


print(finalData)


for items in finalData:
	count = 0
	for key, res in items.items():
		if res == "Overweight":
			count+=1
print("Overweight people(s):",str(count))





	
