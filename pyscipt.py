import csv

# function which finds the average age in our dataset


def find_average(data):
    total_sum_of_age = 0
    total_number_of_people = 0
    average_age_in_dataset = 0
    for line in data:
        total_sum_of_age += int(line["age"])
        total_number_of_people += 1
    average_age_in_dataset = total_sum_of_age / total_number_of_people
    return round(average_age_in_dataset, 1)

# function that filters the charges of smokers and nosmokers in different lists and then print them to the console


def no_smoker_vs_smoker_prices(data):
    list1 = []
    no_smoker_prices = []
    smoker_prices = []
    for item in data:
        list1.append({"Smoker": item["smoker"], "Price": item["charges"]})

    for item in list1:
        if item["Smoker"] == "yes":
            smoker_prices.append(item["Price"])
        elif item["Smoker"] == "no":
            no_smoker_prices.append(item["Price"])

    print(smoker_prices)
    print(no_smoker_prices)

# function that finds the region with the most people in it


def majority_of_the_individuals(data):
    people_from_northwest = 0
    people_from_northeast = 0
    people_from_southwest = 0
    people_from_southeast = 0

    for item in data:
        if item["region"] == "northwest":
            people_from_northwest += 1
        elif item["region"] == "northeast":
            people_from_northeast += 1
        elif item["region"] == "southwest":
            people_from_southwest += 1
        elif item["region"] == "southeast":
            people_from_southeast += 1

    data_dictionary = [{"region": "northwest", "people": people_from_northwest},
                       {"region": "northeast", "people": people_from_northeast},
                       {"region": "southwest", "people": people_from_southwest},
                       {"region": "southeast", "people": people_from_southeast}
                       ]

    max_people = people_from_northwest
    region = "northwest"
    for item in data_dictionary:
        if item["people"] > max_people:
            max_people = item["people"]
            region = item["region"]
    print("The majority of the individuals are from {} with {} people".format(region, max_people))


def average_age_for_1_or_greater_child(data):
    total_sum_of_age = 0
    total_number_of_people = 0
    average_age_in_dataset = 0
    for item in data:
        if int(item["children"]) >= 1:
            total_sum_of_age += int(item["age"])
            total_number_of_people += 1

    average_age_in_dataset = total_sum_of_age / total_number_of_people
    return round(average_age_in_dataset, 1)


with open('insurance.csv') as insurance:
    dataset_information = csv.DictReader(insurance)
    print(find_average(dataset_information))


with open('insurance.csv') as insurance:
    dataset_information = csv.DictReader(insurance)
    no_smoker_vs_smoker_prices(dataset_information)

with open('insurance.csv') as insurance:
    dataset_information = csv.DictReader(insurance)
    majority_of_the_individuals(dataset_information)

with open('insurance.csv') as insurance:
    dataset_information = csv.DictReader(insurance)
    print(average_age_for_1_or_greater_child(dataset_information))






