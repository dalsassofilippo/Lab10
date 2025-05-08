from database.DB_connect import DBConnect
from model.country import Country
from model.edge import Edge


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodes(anno:int):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""select  DISTINCT(c.CCode), c.StateAbb, c.StateNme
                 from country c, contiguity co
                 where c.CCode=co.state1no and co.year<=%s
                 group by c.CCode
                 order by c.StateNme"""
        cursor.execute(query,(anno,))

        result=[]
        for row in cursor.fetchall():
            result.append(Country(**row))

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getAllEdges(anno):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""select  c.state1no as c1, c.state2no as c2
                 from contiguity c
                 where c.year<=%s and c.conttype=1
                 group by c1,c2"""
        cursor.execute(query,(anno,))

        result=[]
        for row in cursor.fetchall():
            result.append(Edge(**row))

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getAllCountry():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from country c"""
        cursor.execute(query)

        result = []
        for row in cursor.fetchall():
            result.append(Country(**row))

        cursor.close()
        cnx.close()
        return result


if __name__=="__main__":
    dao=DAO()
    print(dao.getAllNodes(2000))
    print(dao.getAllEdges(2000))