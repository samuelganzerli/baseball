from database.DB_connect import DBConnect
from model.team import Team


class DAO():

    @staticmethod
    def getAllYears():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select distinct (t.year) from teams t where t.year >= "1980" """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTeamsOfYear(year):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select * 
                    from teams t 
                    where t.year = %s """

        cursor.execute(query, (year,) )

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSalariesTeam(year, idMapTeams):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select t.id, t. teamcode, sum(s.salary) as totsalary
                    from salaries s, teams t, appearances a
                    where t.`year` = s.`year`and a.`year` = t.`year` and a.`year` = %s
                    and t.ID = a.teamID and a.playerID = s.playerID 
                    group by t.ID , t.teamCode"""

        cursor.execute(query, (year, ))

        mapSalary = {}

        for row in cursor:
            #result.append( (idMapTeams(row["ID"]), row["totSalary"]))
            mapSalary[idMapTeams[row["id"]]] = row["totsalary"]
        cursor.close()
        conn.close()
        return mapSalary

