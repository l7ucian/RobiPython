import csv
input = open('Global_Msg_List.csv')

list_of_ids = []
def main():
    # read file
    from os import path
    file_path = path.abspath("D:\RobiPython\\WarningDispatchers.xml")
    file = open(file_path, "r")
    out  = open("workfile.txt", 'w')
    lines = file.readlines()
    file.close()

    sub = 'WarningName="'
    sub1 = '" Type="HMI'

    length = len(sub)
    lentgth1 = len(sub1)

    for line in lines:
        while sub in line:
                begin = line.find(sub) + length
                end = line.find(sub1,begin)

                #print(line[begin:end])
                list_of_ids.append(line[begin:end])

                line = line[0:begin-length] + line[begin:]
                end = end - length
                line = line[0:end] + line[end+lentgth1:]
    #print(list_of_ids)

main()
def make():
    print("Aici incepe smenul")
    with open('something_else.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(next(csv.reader(input)))
    #for row in csv.reader(input):
        for row in list_of_ids:
            input.seek(0)
            for row1 in csv.reader(input):
                if row1[0]==row :
                    print(row1)
                    writer.writerow(row1)
            #print(row[0])
        #   if row[0] in list_of_ids or row[0]=='ID':
         #       writer.writerow(row)
make()
