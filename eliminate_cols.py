import pandas as pd
import subprocess


dfs = subprocess.Popen(['powershell.exe', "ls -n"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
dfs = dfs.stdout.read().decode().split("\n")
import datetime

for files in list(range(1)):
    print(files)
    #files = files[0:len(files)-1]
    try:
        df = pd.read_csv('idle.csv', index_col=0)
        print()
        node = pd.read_csv('idle.csv')
        node_exp = node.iloc[:, 1:]
        node_exp = node_exp.loc[:, (node_exp != 0).any(axis=0)]

        print(1)
        def time_changer2(time: str("2023-04-22 16:35:11")):
            format_date = ("%Y-%m-%d %H:%M:%S")
            dt = datetime.datetime.strptime(time, '%Y-%m-%d  %H:%M:%S')
            df_string = dt.strftime(format_date)
            return (datetime.datetime.strptime(df_string, format_date))


        # df['Date Time'] = pd.to_datetime(df['Date Time'])
        try:
            node_exp['time_stamp'] = node_exp.apply(lambda x: time_changer2(x['time_stamp']), axis=1)
        except:
            print(2)
        #pdu['time'] = pdu.apply(lambda x: time_changer2(x['time']), axis=1)
        try:
            node_exp = node_exp.rename(columns={'time_stamp': 'index'})
            node_exp = node_exp.set_index('index')
            print(3)
            #pdu = pdu.rename(columns={'time': 'index'})
            #pdu = pdu.set_index('index')
            df = node_exp
            cols = df.columns
        except:
            print("okey")

    except:
        print("puff")
        df = 1

    try:
        df.drop(columns=['Memory Pages Swapped out'], inplace=True)
    except:
        print("nothin") # done
    try:
        df.drop(columns=['Cpu Mode Nice Load'], inplace=True)
    except:
        print("nothin") # done

    try:
        df.drop(columns=['Cpu Mode IOwait Load'], inplace=True)
    except:
        print("nothin") # done

    try:
        df.drop(columns=['Processes Blocked'], inplace=True)
    except:
        print("nothin") # done

    try:
        df.drop(columns=['Read Wait Time Avg'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Write Wait Time Avg'], inplace=True)
    except:
        print("nothin")


    try:
        df.drop(columns=['Sockstat TCP Orphan'], inplace=True)
    except:
        print("nothin")


    try:
        df.drop(columns=['TCP Error Retrans'], inplace=True)
    except:
        print("nothin")


    try:
        df.drop(columns=['TCP Error Retransegs'], inplace=True)
    except:
        print("nothin")
    try:
        df.drop(columns=['TCP Out RST flag'], inplace=True)


    except:
        print("nothin")

    try:
        df.drop(columns=['Disk Reads Completed'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Disk Read Megabytes'], inplace=True)
    except:
        print("nothin")





    try:
        df.drop(columns=['I/O Utilization'], inplace=True)


    except:
        print("nothin")

    try:
        df.drop(columns=['Cpu Mode Nice Load'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Disk Reads Completed'], inplace=True)
    except:
        print("nothin")





    try:
        df.drop(columns=['Disk Read Megabytes'], inplace=True)


    except:
        print("nothin")

    try:
        df.drop(columns=['I/O Utilization'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Read Wait Time Avg'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Write Wait Time Avg'], inplace=True)
    except:
        print("nothin")


    try:
        df.drop(columns=['Average Queue Size'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Sockstat TCP Orphan'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['TCP Error Retrans'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['TCP Error Retransegs'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['TCP Out RST flag'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['UDP Noports'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Memory Swap Cache'], inplace=True)
    except:
        print("nothin")

    #######
    try:
        df.drop(columns=['Swap Space Used'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Swap Used Percentage'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Hardware Corrupted'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Cpu Mode IRQ load'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Memory Shemhugepages'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Memory Shempmd Mapped Pages'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Network Transmitted lo'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=[''], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Memory Swap Cache'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Memory Swap Cache'], inplace=True)
    except:
        print("nothin")

    try:
        df.drop(columns=['Memory Swap Cache'], inplace=True)
    except:
        print("nothin")
    ###
    try:
        df.to_csv("1.csv")
    except:
        print("cant save")
        pass
