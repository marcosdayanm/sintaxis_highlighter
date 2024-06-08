import csv

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def calculate_average_age(data):
    total_age = 0
    for row in data:
        total_age += int(row['Age'])
    return total_age / len(data)

def filter_by_gender(data, gender):
    return [row for row in data if row['Gender'] == gender]

def main():
    file_path = 'data.csv'
    data = read_csv(file_path)
    average_age = calculate_average_age(data)
    males = filter_by_gender(data, 'Male')
    
    print("Average Age:", average_age)
    print("Number of Males:", len(males))

if __name__ == "__main__":
    main()
