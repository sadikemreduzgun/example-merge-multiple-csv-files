# written by loyalone
# eliminate empty columns

# import pandas as pd
import subprocess
import datetime


def drop_cols(df, type="phy"):
    drop_list = ['Memory Pages Swapped out', 'Cpu Mode Nice Load', 'Cpu Mode IOwait Load', 'Write Wait Time Avg',
                 'Sockstat TCP Orphan','TCP Error Retrans', 'TCP Error Retransegs', 'TCP Out RST flag',
                 'Disk Reads Completed', 'Disk Read Megabytes', 'Cpu Mode Nice Load', 'I/O Utilization',
                 'Disk Reads Completed', 'Disk Read Megabytes', 'I/O Utilization', 'Read Wait Time Avg',
                 'Average Queue Size', 'Write Wait Time Avg', 'Sockstat TCP Orphan', 'TCP Error Retrans',
                 'Memory Swap Cache','TCP Error Retransegs', 'TCP Out RST flag','UDP Noports', 'Swap Space Used',
                 'Swap Used Percentage', 'Hardware Corrupted', 'Cpu Mode IRQ load', 'Memory Shemhugepages',
                 'Memory Shempmd Mapped Pages', 'Network Transmitted lo',  'Memory Swap Cache', 'Memory Swap Cache',
                 'Memory Swap Cache']


    def eliminate_securely(df, col_name):
        try:
            df.drop(columns=[col_name], inplace=True)
        except:
            print("couln't find") # done

        return df


    dfs = subprocess.Popen(['powershell.exe', "ls -n"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    dfs = dfs.stdout.read().decode().split("\n")


    for files in list(range(1)):
        print(files)
        #files = files[0:len(files)-1]
        try:
            #df = pd.read_csv('sanal.csv', index_col=0)
            print()
            #node = pd.read_csv('sanal.csv')
            node = df
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

        for i in drop_list:
            eliminate_securely(df, i)
        ###
        try:
            if type=="phy":
                df.to_csv("fiziksel.csv")

                return df

            elif type=="vir":
                df.to_csv("sanal.csv")

                return df

        except:
            print("cant save")
            pass
