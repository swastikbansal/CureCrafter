with open('Text\Datasets\disease_symptoms.csv', 'r') as f:
    print("Symptoms: ")
    data = f.readlines()
    # print(data)
    for line in data:
        if 'malaria' == line.split(',')[0].lower():
            for word in line.split(',')[1:]:
                if word != '':
                    print(word)   
                