# %%
import csv
import matplotlib.pyplot as plt

# %%
location = 'C:\\Users\\yg\\Box\\Guang Yue uiuc research box folder\\data\\Drew\\20230703 GS05 copyed 07-21\\book2\\'

# %%
ifile = open(location + "book2_IV.dat", 'r')
datafile = csv.reader(ifile, delimiter='\t')
data = list(datafile)
data1 = []  # reduced data with some smooth
data2 = []  # derivative
data3 = []  # Ic index vs field based on derivative
data4 = []  # Ic vs field based on derivative
data5 = []  # Ic index vs field based on voltage threshold
data6 = []  # Ic vs field based on voltage threshold

# %%
wresis = 0  # wire resistance
dbegin = 1000
dend = 1990
threshold = 0.00001
tr1 = 0.0000247

for i in range(int(len(data) / 2)):
    data1.append([])
    data1.append([])
    for j in range(0, int((dend - dbegin + 1) / 10)):
        px = 0.0
        for k in range(0, 10):
            px = px + float(data[i * 2][dbegin + j * 10 + k])

        px = px / 10
        data1[i * 2].append(px)
        py = 0.0
        for k in range(0, 10):
            py = py + float(data[i * 2 + 1][dbegin + j * 10 + k])

        py = py / 10 - wresis * px / 1000000  # wire resistance calibrication
        data1[i * 2 + 1].append(py)

for i in range(int(len(data1) / 2)):
    data2.append([])
    for j in range(len(data1[0]) - 1):
        data2[i].append((data1[i * 2 + 1][j + 1] - data1[i * 2 + 1][j]) / (data1[i * 2][j + 1] - data1[i * 2][j]))

for i in range(int(len(data1) / 2)):
    data3.append(0)
    data5.append(0)
    for j in range(0, len(data2[0])):
        if data2[i][j] > threshold:
            data3[i] = j
            break
    for j in range(0, len(data1[0])):
        if data1[i * 2 + 1][j] > tr1:
            data5[i] = j
            break

for i in range(len(data3)):
    data4.append([])
    data6.append([])
    data4[i] = data1[i * 2][data3[i]]
    data6[i] = data1[i * 2][data5[i]]

# %%
ofile1 = open(location + 'current uA.dat', 'w')
ofile2 = open(location + 'derivate.dat', 'w')
ofile3 = open(location + 'contour.dat', 'w')
output1 = csv.writer(ofile1, delimiter="\t")
output2 = csv.writer(ofile2, delimiter="\t")
output3 = csv.writer(ofile3, delimiter="\t")

output1.writerow(data1[0])

for row in data2:
    output2.writerow(row)

output3.writerow(data4)
# output2.writerow(data2)
ifile.close()
ofile1.close()
ofile2.close()
ofile3.close()
# import matplotlib.pyplot as plt
# %%
plt.ylim(0, 0.01)
plt.plot(data2[500])
plt.show()