import datetime
import pandas as pd
# import subprocess as sp


def vir_parse(sanal_node):

    sanal_node = sanal_node.iloc[:, 1:]
    sanal_node = sanal_node.loc[:, (sanal_node != 0).any(axis=0)]

    phy_mac = pd.read_csv('fiziksel.csv')
    #phy_mac = phy_mac.iloc[:, 1:]
    #phy_mac = phy_mac.loc[:, (phy_mac != 0).any(axis=0)]


    def time_changer2(time: str("2023-04-22 16:35:11")):
        format_date = ("%Y-%m-%d %H:%M:%S")
        dt = datetime.datetime.strptime(time, '%Y-%m-%d  %H:%M:%S')
        df_string = dt.strftime(format_date)
        return (datetime.datetime.strptime(df_string, format_date))


    # random forest mlp xgboost
    sanal_node['time_stamp'] = sanal_node.apply(lambda x: time_changer2(x['time_stamp']), axis=1)

    # phy_mac = phy_mac.set_index('index')
    sanal_node = sanal_node.rename(columns={'time_stamp': 'index'})
    sanal_node = sanal_node.set_index('index')
    sanal_node.to_csv('new.csv')

    sanal_node = pd.read_csv('new.csv')
    #print(sanal_node.index)
    # print(type(phy_mac.index.to_series()))
    #print(phy_mac.index.to_series())
    # sanal_node.set_index()
    # times_vir = sanal_node.iloc[:,0]

    #times_phy = phy_mac.iloc[:, 0]
    #print(times_phy)
    ##series = phy_mac.index.to_series()
    print(type(phy_mac))
    print(phy_mac.iloc[:, 0])
    print(sanal_node)
    print(phy_mac)

    phy_mac = phy_mac.rename(columns={"Memory Usage Percentage": "new", "Memory Apps": "new2"})
    print(phy_mac.iloc[:,0:1])
    print(phy_mac[["new", "new2"]])
    idle_pm = pd.merge(sanal_node, phy_mac['new'], left_index=True, right_index=True, how="inner")
    print(idle_pm)
    # print(sanal_node)
    idle_pm = idle_pm.drop('new', axis=1)
    idle_pm.to_csv('sanal.csv')
    # sp.run(["python.exe", "eliminate_cols.py"])
