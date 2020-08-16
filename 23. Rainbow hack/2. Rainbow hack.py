import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    dic = {}
    for i in range(1000,10000):
        code = str(i)
        code_hash = hashlib.sha256(code.encode()).hexdigest()
        dic[code_hash] = code
    with open(input_file_name)as f:
        rows = csv.reader(f)
        ans = []
        for i in rows:
            hash_name = i[0]
            hash_req = i[1:]
            ans.append([hash_name, hash_req[0]])
        for i in ans:
            i[1] = dic[i[1]]
        khoruji = ''
        for i in ans:
            khoruji += i[0] + ',' + i[1] + '\n'
    with open(output_file_name, 'w') as f:
        f.write(khoruji)



hash_password_hack('sample_input_data.csv', 'sample_output_data.csv')
