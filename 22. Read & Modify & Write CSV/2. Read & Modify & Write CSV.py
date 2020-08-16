import csv
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        mohtaviat_khat_n = csv.reader(f)
        list_esm_listNomarat = []
        for num_nomarat in mohtaviat_khat_n:
            num = num_nomarat[0]
            nomarat_int = []
            for nomre in num_nomarat[1:]:
                nomarat_int.append(float(nomre))
            list_esm_listNomarat.append((num.lower(), mean(nomarat_int)))
        khoruji = ''
        for i in list_esm_listNomarat:
            khoruji += i[0] + ',' + str(i[1]) + '\n'
    with open(output_file_name, 'w') as f:
        f.write(khoruji)


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        mohtaviat_khat_n = csv.reader(f)
        list_esm_listNomarat = []
        for num_nomarat in mohtaviat_khat_n:
            num = num_nomarat[0]
            nomarat_float = []
            for nomre in num_nomarat[1:]:
                nomarat_float.append(float(nomre))
            list_esm_listNomarat.append((mean(nomarat_float), num.lower()))
        list_esm_listNomarat.sort()
        list_esm_listNomarat_sort = []
        for i in list_esm_listNomarat:
            list_esm_listNomarat_sort.append((i[1], i[0]))
        khoruji = ''
        for i in list_esm_listNomarat_sort:
            khoruji += i[0] + ',' + str(i[1]) + '\n'
    with open(output_file_name, 'w') as f:
        f.write(khoruji)


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as f:
        mohtaviat_khat_n = csv.reader(f)
        list_esm_listNomarat = []
        for num_nomarat in mohtaviat_khat_n:
            num = num_nomarat[0]
            nomarat_float = []
            for nomre in num_nomarat[1:]:
                nomarat_float.append(float(nomre))
            list_esm_listNomarat.append((mean(nomarat_float), num.lower()))
        list_esm_listNomarat.sort(reverse=True)
        list_esm_listNomarat = list_esm_listNomarat[:3]
        AAA = []
        for i in list_esm_listNomarat:
            AAA.append((i[1], i[0]))
        BBB = []
        BBB_temp_1 = []
        if AAA[0][1] == AAA[1][1]:
            BBB.append(AAA[0])
            BBB.append(AAA[1])
            BBB.sort()
            if AAA[1][1] == AAA[2][1]:
                BBB.append(AAA[2])
                BBB.sort()
            else:
                BBB.append(AAA[2])
        elif AAA[1][1] == AAA[2][1]:
            BBB.append(AAA[0])
            BBB_temp_1.append(AAA[1])
            BBB_temp_1.append(AAA[2])
            BBB_temp_1.sort()
            BBB += BBB_temp_1
        else:
            BBB = AAA
        khoruji = ''
        for i in BBB:
            khoruji += i[0] + ',' + str(i[1]) + '\n'
    with open(output_file_name, 'w') as f:
        f.write(khoruji)


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as f:
        mohtaviat_khat_n = csv.reader(f)
        list_esm_listNomarat = []
        for num_nomarat in mohtaviat_khat_n:
            num = num_nomarat[0]
            nomarat_float = []
            for nomre in num_nomarat[1:]:
                nomarat_float.append(float(nomre))
            list_esm_listNomarat.append((mean(nomarat_float), num.lower()))
        list_esm_listNomarat.sort()
        list_esm_listNomarat = list_esm_listNomarat[:3]
        AAA = []
        for i in list_esm_listNomarat:
            AAA.append((i[1], i[0]))
        BBB = []
        BBB_temp_1 = []
        if AAA[0][1] == AAA[1][1]:
            BBB.append(AAA[0])
            BBB.append(AAA[1])
            BBB.sort()
            if AAA[1][1] == AAA[2][1]:
                BBB.append(AAA[2])
                BBB.sort()
            else:
                BBB.append(AAA[2])
        elif AAA[1][1] == AAA[2][1]:
            BBB.append(AAA[0])
            BBB_temp_1.append(AAA[1])
            BBB_temp_1.append(AAA[2])
            BBB_temp_1.sort()
            BBB += BBB_temp_1
        else:
            BBB = AAA
        khoruji = ''
        for i in BBB:
            khoruji += str(i[1]) + '\n'
    with open(output_file_name, 'w') as f:
        f.write(khoruji)


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        mohtaviat_khat_n = csv.reader(f)
        list_esm_listNomarat = []
        for num_nomarat in mohtaviat_khat_n:
            num = num_nomarat[0]
            nomarat_int = []
            for nomre in num_nomarat[1:]:
                nomarat_int.append(float(nomre))
            list_esm_listNomarat.append((num.lower(), mean(nomarat_int)))
        sum = []
        for i in list_esm_listNomarat:
            sum.append(i[1])
        avg = mean(sum)
    with open(output_file_name, 'w') as f:
        f.write(str(avg))



input_file_name = 'sample_input_data.csv'
calculate_averages(input_file_name, 'output_file_name_1.csv')
calculate_sorted_averages(input_file_name, 'output_file_name_2.csv')
calculate_three_best(input_file_name, 'output_file_name_3.csv')
calculate_three_worst(input_file_name, 'output_file_name_4.csv')
calculate_average_of_averages(input_file_name, 'output_file_name_5.csv')

