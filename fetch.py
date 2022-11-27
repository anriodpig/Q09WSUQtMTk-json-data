import datetime
import requests

# https://2019ncov.chinacdc.cn/JKZX/yq_20200103.json
# The earliest acquirable data from China CDC official

cdc_url = "https://2019ncov.chinacdc.cn/JKZX/yq_"


def down_by_date(dn):
    try:
        ds = str(dn)
        rq = requests.get(cdc_url + ds + ".json")
        fp = open(ds + ".json", "wb")
        fsz = fp.write(rq.content)
        fp.close()
    finally:
        print("download_" + ds + " , HTTP " + str(rq.status_code) +" "+ str(fsz))
        # print(rq.content)


if __name__ == '__main__':

    begin = datetime.date(2020, 1, 3)
    end = datetime.date(2022, 11, 27)

    dt = begin
    delta = datetime.timedelta(days=1)

    while dt <= end:
        dn = dt.strftime("%Y%m%d")
        down_by_date(dn)
        # print(dn)
        dt += delta

    # down_by_date(20221126)
