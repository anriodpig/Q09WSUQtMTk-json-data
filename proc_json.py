import datetime
import json


def process_by_date(dn):
    ds = str(dn)
    try:
        fp = open(ds + '.json', 'rb')
        jb = fp.read()
        if len(jb) < 20000:
            return
        fp.close()
        js = json.loads(jb)
        # print(js)
        fp = open(ds + '_min.txt', 'w', encoding='utf-8')

        for i in js['features']:
            # print(i)
            # print(i['id'])
            val = i['properties']
            # print(val)
            dt = json.dumps(val, ensure_ascii=False)
            fp.write(dt + '\n')
        fp.close()
        print(ds + ' OK')
        # container.append(i['properties'])

        # print(js['features'])


    except FileNotFoundError:
        pass
    # print(len(jb))


if __name__ == '__main__':
    begin = datetime.date(2020, 1, 3)
    end = datetime.date(2022, 11, 27)

    dt = begin
    delta = datetime.timedelta(days=1)

    while dt <= end:
        dn = dt.strftime("%Y%m%d")
        process_by_date(dn)
        # print(dn)
        dt += delta

    # container = []

    # process_by_date(20221126)

    # for i in container:
    #     # i attributes:
    #     # OBJECTID adcode name OBJECTID1 编码 省份 新增疑似 累计疑似 新增确诊 累计确诊 新增死亡 累计死亡
    #
    #     # print(i['name'])
