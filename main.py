import subprocess
import os
from subprocess import call
import pandas as pd
import datetime

"""#os.putenv('COMSPEC',r'C:\Windows\System32\WindowsPowe rShell\v1.0\powershell.exe')
p=subprocess.call(f'C:\Windows\System32\powershell.exe ls',stdout=subprocess.PIPE ,shell=True)
#p=subprocess.run(["ls"],stdout=subprocess.PIPE,shell=True)
#out = p.communicate()[0].decode('utf-8')
#out = p.stdout.decode('utf-8')
print(type(p))"""
#os.putenv('COMSPEC',    r'C:\Windows\System32\WindowsPowe rShell\v1.0\powershell.exe')
#output = subprocess.run(['powershell.exe', "cd C:\\Users\\ZENBOOK\\out"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = subprocess.Popen(['powershell.exe',"ls -n"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#print(type(output.stdout.read().decode()))
#print(output.stdout.read().decode().strip())


def merger(node_file, snmp_file):

    print(node_file)
    node = pd.read_csv(node_file)
    node_exp = node.iloc[:, 1:]
    node_exp = node_exp.loc[:, (node_exp != 0).any(axis=0)]

    print(snmp_file)
    pdu = pd.read_csv(snmp_file)
    pdu = pdu.loc[:, (pdu != 0).any(axis=0)]

    def time_changer2(time: str("2023-04-22 16:35:11")):
        format_date = ("%Y-%m-%d %H:%M:%S")
        dt = datetime.datetime.strptime(time, '%Y-%m-%d  %H:%M:%S')
        df_string = dt.strftime(format_date)
        return (datetime.datetime.strptime(df_string, format_date))

    # df['Date Time'] = pd.to_datetime(df['Date Time'])
    node_exp['time_stamp'] = node_exp.apply(lambda x: time_changer2(x['time_stamp']), axis=1)

    pdu['time'] = pdu.apply(lambda x: time_changer2(x['time']), axis=1)

    node_exp = node_exp.rename(columns={'time_stamp': 'index'})
    node_exp = node_exp.set_index('index')

    pdu = pdu.rename(columns={'time': 'index'})
    pdu = pdu.set_index('index')

    try:
        idle_pm = pd.merge(node_exp, pdu, left_index=True, right_index=True, how='inner')
    except:
        print("mergeleyemedim agam")

    print(idle_pm)
    return idle_pm


def merge_ilo(temp_file, power_file):

    print(temp_file, power_file)
    def time_changer(time: str("10-02-2023 05:23:43")):
        format_date = ("%Y-%m-%d %H:%M:%S")
        dt = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        df_string = dt.strftime(format_date)
        return (datetime.datetime.strptime(df_string, format_date))

    ilo_power = pd.read_csv(power_file)
    ilo_power = ilo_power.loc[:, (ilo_power != 0).any(axis=0)]

    ilo_temp = pd.read_csv(temp_file)
    ilo_temp = ilo_temp.loc[:, (ilo_temp != 0).any(axis=0)]

    ilo_power['Date Time'] = ilo_power.apply(lambda x: time_changer(x['Date Time']), axis=1)
    ilo_temp['Date Time'] = ilo_temp.apply(lambda x: time_changer(x['Date Time']), axis=1)

    ilo_power = ilo_power.rename(columns={'Date Time': 'index'})
    ilo_power = ilo_power.set_index('index')

    ilo_temp = ilo_temp.rename(columns={'Date Time': 'index'})
    ilo_temp = ilo_temp.set_index('index')

    ilo = pd.merge(ilo_power, ilo_temp, left_index=True, right_index=True, how='inner')
    print(ilo)
    return ilo

names_list = output.stdout.read().decode().split("\n")
#print(names_list)
file_list = []

aypos1 = []
aypos2 = []
aypos3 = []
aypos4 = []
aypos5 = []
compute2=[]

snmp = []
ILO_temp = []
ILO_power = []


for files in names_list:
    #print(files)
    leng = len(files)
    ct = 0
    hold_file = ""
    for letters in files:
        if ct >leng-2:
            break
        hold_file += letters
        ct += 1

    files = hold_file

    if files[0:6] == "aypos1":
        aypos1.append(files)

    elif files[0:6] == "aypos2":
        aypos2.append(files)
    elif files[0:6] == "aypos3":
        aypos3.append(files)
    elif files[0:6] == "aypos4":
        aypos4.append(files)
    elif files[0:6] == "aypos5":
        aypos5.append(files)
    elif files[0:8] == "compute2":
        compute2.append(files)

    elif files[0:4] == "snmp":
        snmp.append(files)

    elif files[0:13] == "ILO_metrics_t":
        ILO_temp.append(files)
    elif files[0:13] == "ILO_metrics_p":
        ILO_power.append(files)

#print(snmp)
#print(aypos1)

def extract_n_order():
    pass

sns_times = []

snmp_order_time = []
for sns in snmp:
    time = sns[16:30]
    holl = ""
    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        else:
            holl += letters

    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = holl
    sns_times.append(time)
    #print(time)

    snmp_order_time.append(time)

snmp_end_time = []
for sns in snmp:
    time = sns[40:54]
    holl = ""
    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        else:
            holl += letters

    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = holl
    #print(time)
    #sns_times.append(time)
    #print(time)

    snmp_end_time.append(time)

# power
# 29 ten 44 e
temp_times = []
for ILL in ILO_temp:
    time = ILL[28:42]
    holl = ""
    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        else:
            holl += letters
    hold = ""
    for letter in holl:
        if letter == "i":
            hold += " "
        else:
            hold+=letter
    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = hold

    temp_times.append(time)
    #print(time)

temp_end = []
for ILL in ILO_temp:
    time = ILL[52:66]
    holl = ""
    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        else:
            holl += letters
    hold = ""
    for letter in holl:
        if letter == "i":
            hold += " "
        else:
            hold+=letter
    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = hold
    #print(time)
    temp_end.append(time)
    #print(time)

times_power = []
for powe in ILO_power:
    time = powe[29:43]
    #print(time)
    holl = ""

    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        else:
            holl += letters
    hold = ""
    for letter in holl:
        if letter == "i":
            hold += " "
        else:
            hold+=letter
    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = hold

    times_power.append(time)
    #print(time)

power_end = []
for powe in ILO_power:
    time = powe[53:67]
    #print(time)
    holl = ""

    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        else:
            holl += letters
    hold = ""
    for letter in holl:
        if letter == "i":
            hold += " "
        else:
            hold+=letter
    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = hold

    power_end.append(time)


def opers():
    # rename
    # index

    pass

aypos1_time = []
for elems in aypos1:
    time = elems[15:29]
    #print(elems[15:29])
    holl = ""

    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        #elif letters ==
        else:
            holl += letters
    hold = ""
    for letter in holl:
        if letter == "i":
            hold += " "
        else:
            hold += letter
    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = hold
    #print(time)
    aypos1_time.append(time)

aypos1_end = []
for elems in aypos1:
    time = elems[45:59]
    #print(elems[15:29])
    holl = ""

    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        #elif letters ==
        else:
            holl += letters
    hold = ""
    for letter in holl:
        if letter == "i":
            hold += " "
        else:
            hold += letter
    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = hold

    #print(time)
    aypos1_end.append(time)

compute2_time = []
#print(compute2)
for elems in compute2:
    time = elems[20:34]
    #print(elems[15:29])
    holl = ""

    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        #elif letters ==
        else:
            holl += letters
    hold = ""
    for letter in holl:
        if letter == "i":
            hold += " "
        else:
            hold += letter
    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = hold
    #print(time)
    compute2_time.append(time)


compute2_end = []
#print(compute2)
for elems in compute2:
    time = elems[47:61]
    #print(elems[15:29])
    holl = ""

    for letters in time:
        if letters == "_":
            holl += " "
        elif letters == "T":
            holl += " "
        #elif letters ==
        else:
            holl += letters
    hold = ""
    for letter in holl:
        if letter == "i":
            hold += " "
        else:
            hold += letter
    # 1 2 are months and 4 5 are days, 7 8 are hour 10 11 are minutes 13 14 are seconds
    time = hold
    print(time)
    compute2_end.append(time)

# what matter is here
# node_exp and snmp
# ilo temp and ilo power
once = True

"""for i in range(len(temp_times)):
    try:
        for j in range(len(times_power)):
            if i == j:
                if once:
                    hold_ilo = merge_ilo(ILO_temp[i], ILO_power[i])
                    once = False
                else:
                    try:
                        hold_ilo = pd.concat((hold_ilo,merge_ilo(ILO_temp[i], ILO_power[i])), axis=0)
                    except:
                        print("no data in ilo")
    except:
        print("baban")

print(hold_ilo)"""

once = True

for i in range(len(compute2_time)):

    print(i, compute2_time[i][0:2],snmp_end_time[0][0:2], compute2_end[i][0:2])
    #print("04"<="04"<="04")

    for j in range(len(snmp_order_time)):
        print(((compute2_time[i][3:5] <= snmp_order_time[j][3:5] <= compute2_end[i][3:5]) or (
                compute2_time[i][3:5] <= snmp_end_time[j][3:5] <= compute2_end[i][3:5])))
        print(compute2_time[i][3:5], snmp_order_time[j][3:5], compute2_end[i][3:5])
        print(snmp_end_time[j][3:5])
        #print(999999999999999999999999)
        if (compute2_time[i][0:2]<snmp_order_time[j][0:2]<compute2_end[i][0:2]) or (compute2_time[i][0:2]<snmp_end_time[j][0:2]<compute2_end[i][0:2]):
#            print(compute2_time[i][2:0]<snmp_end_time[j][0:2]<compute2_end[i][0:2])
#            print(i, snmp_order_time[i], snmp[i])
#            print(compute2_time[i],compute2[i])
            print(compute2_time[i][0:2], snmp_end_time[j][0:2], compute2_end[i][0:2])

            #new = merger(snmp_file=snmp[j], node_file=compute2[i])

            if once:
                hold = merger(compute2[i], snmp[j])
                once = False
            else:
                hold = pd.concat((hold, merger(compute2[i], snmp[j])),axis=0)

        elif (compute2_time[i][0:2]<=snmp_order_time[j][0:2]<compute2_end[i][0:2]) or (compute2_time[i][0:2]<=snmp_end_time[j][0:2]<compute2_end[i][0:2]):
            if once:
                hold = merger(compute2[i], snmp[j])
                once = False
            else:
                hold = pd.concat((hold, merger(compute2[i], snmp[j])), axis=0)

        elif (compute2_time[i][0:2]<snmp_order_time[j][0:2]<=compute2_end[i][0:2]) or (compute2_time[i][0:2]<snmp_end_time[j][0:2]<=compute2_end[i][0:2]):
            if once:
                hold = merger(compute2[i], snmp[j])
                once = False
            else:
                hold = pd.concat((hold, merger(compute2[i], snmp[j])), axis=0)

        elif ((compute2_time[i][0:2]<=snmp_order_time[j][0:2]<=compute2_end[i][0:2]) or
              (compute2_time[i][0:2]<=snmp_end_time[j][0:2]<=compute2_end[i][0:2])) and \
                ((compute2_time[i][3:5] <= snmp_order_time[j][3:5] <= compute2_end[i][3:5]) or (
                compute2_time[i][3:5] <= snmp_end_time[j][3:5] <= compute2_end[i][3:5])):
           """# here will be another sub if < <
           if (compute2_time[i][4:6] < snmp_order_time[j][4:6] < compute2_end[i][4:6]) or (
                   compute2_time[i][4:6] < snmp_end_time[j][4:6] < compute2_end[i][4:6]):
           """
           print(i,2)
           if once:
               try:
                   hold = merger(compute2[i], snmp[j])
                   once = False
               except:
                   print("no pdu")
           else:
               try:
                    hold = pd.concat((hold, merger(compute2[i], snmp[j])), axis=0)
               except:
                   print("else kısmı")
        elif ((compute2_time[i][0:2]<=snmp_order_time[j][0:2]<=compute2_end[i][0:2]) or (compute2_time[i][0:2]<=snmp_end_time[j][0:2]<=compute2_end[i][0:2])) \
                and ((compute2_time[i][3:5]<=snmp_order_time[j][3:5]<=compute2_end[i][3:5]) or (compute2_time[i][3:5]<=snmp_end_time[j][3:5]<=compute2_end[i][3:5]))\
                and ((compute2_time[i][7:9]<snmp_order_time[j][7:9]<compute2_end[i][7:9]) or (compute2_time[i][7:9]<snmp_end_time[j][7:9]<compute2_end[i][7:9])):
            """if (compute2_time[i][4:6]<=snmp_order_time[j][4:6]<=compute2_end[i][4:6]) or (compute2_time[i][4:6]<=snmp_end_time[j][4:6]<=compute2_end[i][4:6]):
                if (compute2_time[i][7:9]<snmp_order_time[j][7:9]<compute2_end[i][7:9]) or (compute2_time[i][7:9]<snmp_end_time[j][7:9]<compute2_end[i][7:9]):"""
            print(3,snmp_order_time[j], ", ", snmp_end_time[j])
            print(compute2_time[i], ", ", compute2_end[i])
            if once:
                hold = merger(compute2[i], snmp[j])
                once = False
            else:
                hold = pd.concat((hold, merger(compute2[i], snmp[j])), axis=0)

        elif ((compute2_time[i][0:2]<=snmp_order_time[j][0:2]<=compute2_end[i][0:2]) or (compute2_time[i][0:2]<=snmp_end_time[j][0:2]<=compute2_end[i][0:2])) \
                and ((compute2_time[i][4:6]<=snmp_order_time[j][4:6]<=compute2_end[i][4:6]) or (compute2_time[i][4:6]<=snmp_end_time[j][4:6]<=compute2_end[i][4:6]))\
                and ((compute2_time[i][10:12] < snmp_order_time[j][10:12] < compute2_end[i][10:12]) or (
                            compute2_time[i][10:12] < snmp_end_time[j][10:12] < compute2_end[i][10:12])):
            """if (compute2_time[i][4:6]<=snmp_order_time[j][4:6]<=compute2_end[i][4:6]) or (compute2_time[i][4:6]<=snmp_end_time[j][4:6]<=compute2_end[i][4:6]):
                if (compute2_time[i][7:9]<=snmp_order_time[j][7:9]<=compute2_end[i][7:9]) or (compute2_time[i][7:9]<=snmp_end_time[j][7:9]<=compute2_end[i][7:9]):
                    if (compute2_time[i][10:12] < snmp_order_time[j][10:12] < compute2_end[i][10:12]) or (
                            compute2_time[i][10:12] < snmp_end_time[j][10:12] < compute2_end[i][10:12]):"""
            print(4,snmp_order_time[j], ", ", snmp_end_time[j])
            print(compute2_time[i], ", ", compute2_end[i])
            if once:
                hold = merger(compute2[i], snmp[j])
                once = False
            else:
                hold = pd.concat((hold, merger(compute2[i], snmp[j])), axis=0)

        elif ((compute2_time[i][0:2]<=snmp_order_time[j][0:2]<=compute2_end[i][0:2]) or (compute2_time[i][0:2]<=snmp_end_time[j][0:2]<=compute2_end[i][0:2]))\
                and ((compute2_time[i][4:6]<=snmp_order_time[j][4:6]<=compute2_end[i][4:6]) or (compute2_time[i][4:6]<=snmp_end_time[j][4:6]<=compute2_end[i][4:6]))\
                and ((compute2_time[i][7:9]<=snmp_order_time[j][7:9]<=compute2_end[i][7:9]) or (compute2_time[i][7:9]<=snmp_end_time[j][7:9]<=compute2_end[i][7:9]))\
                and ((compute2_time[i][10:12]<=snmp_order_time[j][10:12]<=compute2_end[i][10:12]) or (compute2_time[i][10:12]<=snmp_end_time[j][10:12]<=compute2_end[i][10:12]))\
                and ((compute2_time[i][13:15]<=snmp_order_time[j][13:15]<=compute2_end[i][13:15]) or (compute2_time[i][13:15]<=snmp_end_time[j][13:15]<=compute2_end[i][13:15])):
            """if (compute2_time[i][4:6]<=snmp_order_time[j][4:6]<=compute2_end[i][4:6]) or (compute2_time[i][4:6]<=snmp_end_time[j][4:6]<=compute2_end[i][4:6]):
                if (compute2_time[i][7:9]<=snmp_order_time[j][7:9]<=compute2_end[i][7:9]) or (compute2_time[i][7:9]<=snmp_end_time[j][7:9]<=compute2_end[i][7:9]):
                    if (compute2_time[i][10:12]<=snmp_order_time[j][10:12]<=compute2_end[i][10:12]) or (compute2_time[i][10:12]<=snmp_end_time[j][10:12]<=compute2_end[i][10:12]):
                        if (compute2_time[i][13:15]<=snmp_order_time[j][13:15]<=compute2_end[i][13:15]) or (compute2_time[i][13:15]<=snmp_end_time[j][13:15]<=compute2_end[i][13:15]):
"""
            print(5,snmp_order_time[j], ", ", snmp_end_time[j])
            print(compute2_time[i], ", ", compute2_end[i])
            if once:
                hold = merger(compute2[i], snmp[j])
                once = False
            else:
                hold = pd.concat((hold, merger(compute2[i], snmp[j])), axis=0)

        try:
            print(hold)
        except:
            print("no hold")
    else:
        print("wtf")
        #print(snmp_order_time[j], ", ", snmp_end_time[j])

    #print(compute2_time[i], ", ",compute2_end[i])

#idle = pd.merge(hold, hold_ilo, left_index=True, right_index=True, how='inner')
idle = hold
idle.to_csv("idle.csv")

"""for filess in names_list:
    leng = len(filess)
    hold_file = ""
    ct = 0
    for letters in filess:
        if ct >leng-2:
            break
        hold_file += letters
        ct += 1

    print(hold_file)
    file_list.append(hold_file)

for files in file_list:
    hold = ""

    count = 0
    for letter in files:
        if letter == "_":
            hold += " "
        elif letter == ":":
            hold += "T"
        elif letter == "-":
            hold += "_"
        elif letter == "\'":
            continue
        elif letter == "N":
            hold+="."
        elif letter == " ":
            hold += "_"
        else:
            hold += letter
    print(hold)
    # Get-ChildItem check.py  |Rename-Item -NewName checko.py
    #subprocess.run(['powershell.exe',"Get-ChildItem",file_list[count], "|","Rename-Item","-NewName",hold], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    subprocess.Popen(f"powershell.exe Get-ChildItem {file_list[count]}| Rename-Item -NewName {hold}")
    count += 1
"""
