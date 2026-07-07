from database.DB_connect import DBConnect
from model.album import Album
from model.arco import Arco


class DAO():

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT a.* , SUM(t.AlbumId) AS NumBrani
                FROM Album a , Track t  
                WHERE t.AlbumId  = a.AlbumId 
                GROUP BY a.AlbumId 
                ORDER BY NumBrani ASC
                """

        cursor.execute(query)

        for row in cursor:
            results.append(Album(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT t1.AlbumId as e1, t2.AlbumId as e2
                FROM (SELECT t.AlbumId, t.GenreId
                FROM Track t) as t1,
                (SELECT t.AlbumId, t.GenreId
                FROM Track t) as t2
                WHERE t1.GenreId = t2.GenreId
                and t1.AlbumId < t2.AlbumId
                GROUP BY t1.AlbumId , t2.AlbumId
                """

        cursor.execute(query)

        for row in cursor:
            results.append(Arco(idMap[row["e1"]], idMap[row["e2"]]))

        cursor.close()
        conn.close()
        return results

