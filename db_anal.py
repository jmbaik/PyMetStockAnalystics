import pandas as pd
import cx_Oracle
from datetime import datetime


def connect_metstock():
    return cx_Oracle.connect("metstock", "man100", "192.168.0.6:1521/meteldb")


def query_metstock(q):
    conn = connect_metstock()
    result = pd.read_sql(q, conn)
    conn.close()
    return result


def get_met_anal_up(item_cd, ymd, cnt):
    q = """
            SELECT 
            A.ITEM_CD
            , A.YMD
            , A.LPRICE
            , A.SPRICE
            , A.EPRICE
            , A.HPRICE
            , A.VOLUMN
            , A.VAMT
        FROM MET_ITEM_DAY_K A, MET_ANAL_UP B
        WHERE A.ITEM_CD = B.ITEM_CD
        AND B.ITEM_CD ='{0}' AND b.YMD='{1}'
        AND A.YMD BETWEEN TO_DATE(B.YMD)-{2} AND  TO_DATE(B.YMD)+{2}
    """.format(item_cd, ymd, cnt)
    return query_metstock(q)
