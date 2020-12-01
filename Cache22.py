import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable


class bcolors:
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CRED = '\33[31m'


InpDesc = {
    'DATE': 'A date value in YYYY-MM-DD format',
    'TIME': 'A time value in hh:mm:ss format',
    'DATETIME': 'A date and time value in YYYY-MM-DD hh:mm:ss format',
    'TEXT': 'A small non-binary string',
    'VARCHAR': 'A variable-length non-binary string',
    'INT': 'A standard integer'
}


def TakeInput(items: list = [], Type: list = []):
    inputs = {}
    for idx, item in enumerate(items):
        val = input('Please enter ' + item +
                    ' (' + InpDesc[Type[idx]] + '): ')
        inputs[item] = val
    return inputs

def FetchMaxPoints(Cid: int, ProblemName: str):
    query = "select Maxpoints FROM PROBLEM WHERE ContestId=%d AND ProblemName='%s'" % (int(Cid),ProblemName)
    cur.execute(query)
    rows = cur.fetchall()
    return rows[0]['Maxpoints']

def Addcontest():
    try:
        ContestParameters = TakeInput(['ContestID', 'Duration', 'StartTime'], [
                                      'INT', 'TIME', 'DATETIME'])
        query = "INSERT INTO CONTEST(ContestID,Duration,StartTime) VALUES(%d, '%s', '%s')"\
            % (int(ContestParameters['ContestID']), ContestParameters['Duration'], ContestParameters['StartTime'])
        cur.execute(query)
        num_of_languages = int(
            input('Enter number of languages allowed in the contest: '))

        if num_of_languages < 0:
            print("You entered a negative value, rolling back changes for this query")
            con.rollback()
            return

        for i in range(num_of_languages):
            language = input(
                'Enter Language Number ' + str(i+1) + ': ')
            query = "INSERT INTO CONTESTLANGUAGES(ContestID,AllowedLanguages) VALUES(%d,'%s')"\
                % (int(ContestParameters['ContestID']), language)
            cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to insert into database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def AddTeam():
    try:
        TeamParameters = TakeInput(['TNo', 'TName', 'CollegeName'], [
                                   'INT', 'VARCHAR', 'VARCHAR'])
        query = "INSERT INTO TEAM(TNo, TName, CollegeName) VALUES(%d, '%s', '%s')"\
            % (int(TeamParameters['TNo']), TeamParameters['TName'], TeamParameters['CollegeName'])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to insert into database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def Participates():
    try:
        ParticipatesParameters = TakeInput(
            ['TNo', 'ContestID'], ['INT', 'INT'])
        query = "INSERT INTO PARTICIPATES(TNo, ContestID) VALUES(%d, %d)"\
            % (int(ParticipatesParameters['TNo']), int(ParticipatesParameters['ContestID']))
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to insert into database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def AddProgrammer():
    try:
        Parameters = TakeInput(
            ['ProgrammerID', 'EmailID', 'Fname', 'Lname', 'Nationality', 'Age'], ['INT', 'VARCHAR', 'VARCHAR', 'VARCHAR', 'VARCHAR', 'INT', 'INT'])
        if Parameters['Age'] <= 0:
            print("You entered a wrong age. ")
            return
        isgraduate = int(
            input('Is the Programmer graduated? 1 for yes and 0 for no: '))
        if isgraduate == 0:
            Parameters['Is_graduate'] = 0
        elif isgraduate == 1:
            Parameters['Is_graduate'] = 1
        else:
            print("Invalid input")
            return
        query = "INSERT INTO PROGRAMMER(ProgrammerID, EmailID, Fname, Lname, Nationality, Age, Is_graduate) VALUES(%d, '%s', '%s', '%s', '%s', %d, %d)"\
            % (int(Parameters['ProgrammerID']), Parameters['EmailID'], Parameters['Fname'], Parameters['Lname'], Parameters['Nationality'], int(Parameters['Age']), int(Parameters['Is_graduate']))
        cur.execute(query)

        if isgraduate == 0:
            collegeyear = int(input('Enter college year of contestant: '))
            tno = int(input('Enter TNo for contestant: '))
            query = "INSERT INTO CONTESTANT(ProgrammerID, CollegeYear, TNo) VALUES(%d, %d, %d)"\
                % (int(Parameters['ProgrammerID']), collegeyear, tno)
            cur.execute(query)
        else:
            num = int(
                input('Enter number of problems that problem setter have written so far: '))
            exp = int(input(
                'Enter the number of years the programmer is working as a programmer setter: '))
            query = "INSERT INTO PROBLEMSETTER(ProgrammerID, Numofproblems, Experience) VALUES(%d, %d, %d)"\
                % (int(Parameters['ProgrammerID']), num, exp)
            cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to insert into database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def AddProblem():
    try:
        Parameters = TakeInput(['ProblemAuthorID', 'ContestID', 'ProblemName', 'Maxpoints',
                                'Pstatement', 'TestIO', 'SampleIO', 'Memory', 'Runtime', 'IOFormat'], ['INT', 'INT', 'VARCHAR', 'INT', 'TEXT', 'TEXT', 'TEXT', 'INT', 'TIME', 'VARCHAR'])
        num_of_tags = int(input('Enter number of problem tags: '))
        query = "INSERT INTO PROBLEM(ContestID, ProblemName, Maxpoints, Pstatement, TestIO, SampleIO, IOFormat, Memory, Runtime) VALUES( %d, '%s', %d, '%s', '%s', '%s', '%s', %d, '%s')"\
            % (int(Parameters['ContestID']), Parameters['ProblemName'], int(Parameters['Maxpoints']), Parameters['Pstatement'],
                Parameters['TestIO'], Parameters['SampleIO'], Parameters['IOFormat'], int(Parameters['Memory']), Parameters['Runtime'])
        cur.execute(query)
        query = "INSERT INTO PROBLEMAUTHOR(ProgrammerID, ContestID, ProblemName) VALUES(%d, %d, '%s')"\
            % (int(Parameters['ProblemAuthorID']), int(Parameters['ContestID']), Parameters['ProblemName'])
        cur.execute(query)
        for i in range(num_of_tags):
            Tag = input('Enter Tag number ' + str(i+1) + ': ')
            query = "INSERT INTO PROBLEMTAGS( ContestID, ProblemName, Tags) VALUES(%d, '%s', '%s')"\
                % (int(Parameters['ContestID']), Parameters['ProblemName'], Tag)
            cur.execute(query)
        issubproblem = input('Is this a subproblem? (yes/no): ')
        if issubproblem[0] == 'y' or issubproblem[0] == 'Y':
            parent = input('Enter Parent Problem Name: ')
            query = "INSERT INTO SUBPROBLEM(ContestID, ProblemName, ParentProblemName) VALUES(%d, '%s', '%s')"\
                % (int(Parameters['ContestID']), Parameters['ProblemName'], parent)
            cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to insert into database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def TakeVerdict():
    verdicts = ['AC', 'WA', 'RTE', 'MLE', 'TLE']
    Vid = int(
        input("Enter Verdict Number   0)AC    1)WA    2)RTE    3)MLE   4)TLE: "))
    if 0 <= Vid <= 4:
        return verdicts[Vid]
    else:
        return 'error'


def TakeLanguage(Cid: int):
    query = "SELECT * FROM CONTESTLANGUAGES WHERE ContestID=%d" % (Cid)
    cur.execute(query)
    rows = cur.fetchall()
    out = 'Enter Language: '
    tot = int(0)
    for idx, row in enumerate(rows):
        out += str(idx+1) + ')' + row['AllowedLanguages'] + ' '
        tot += 1
    Lid = int(input(out))
    if 1 <= Lid <= tot:
        return rows[Lid-1]['AllowedLanguages']
    else:
        return 'error'


def Addsubmission():
    try:
        Parameters = TakeInput(['TNo', 'ContestID', 'ProblemName',
                                'SubTime', 'MEMORY', 'RUNTIME'], ['INT', 'INT', 'VARCHAR', 'TIME', 'INT', 'INT'])
        Maxpoints = int(FetchMaxPoints(int(Parameters['ContestID']),Parameters['ProblemName']))
        Parameters['POINTS'] = int(input("Enter Points in range [0,%d]: "%(Maxpoints)))
        if Parameters['POINTS'] > Maxpoints:
            print("Invalid Points")
            return
        Parameters['VERDICT'] = TakeVerdict()
        if Parameters['VERDICT'] == 'error':
            print('You Entered Wrong Verdict Number ')
            return
        Parameters['Language'] = TakeLanguage(int(Parameters['ContestID']))
        if Parameters['Language'] == 'error':
            print('You Entered wrong Language choice. ')
            return
        query = "INSERT INTO SUBMISSION(Language, SubTime, VERDICT, POINTS, MEMORY, RUNTIME) VALUES( '%s', '%s', '%s', %d, %d, %d)"\
            % (Parameters['Language'], Parameters['SubTime'], Parameters['VERDICT'], int(Parameters['POINTS']), int(Parameters['MEMORY']), int(Parameters['RUNTIME']))
        cur.execute(query)
        query = "SELECT LAST_INSERT_ID()"
        cur.execute(query)
        rows = cur.fetchall()
        Parameters['SubID'] = int(rows[0]['LAST_INSERT_ID()'])
        query = "INSERT INTO SUBMITS(TNo, ContestID, ProblemName, SubID) VALUES( %d, %d, '%s', %d)"\
            % (int(Parameters['TNo']), int(Parameters['ContestID']), Parameters['ProblemName'], int(Parameters['SubID']))
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to insert into database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def RmContest():
    try:
        Cid = int(input('Enter ID of contest you want to delete: '))
        query = "DELETE FROM CONTEST WHERE ContestID = %d" % (Cid)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to remove from database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def RmTeam():
    try:
        Tid = int(input('Enter Team No of Team you want to delete: '))
        query = "DELETE FROM TEAM WHERE TNo = %d" % (Tid)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to remove from database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def RmProblem():
    try:
        Cid = int(input('Enter Contest ID of Problem you want to delete: '))
        PName = input('Enter Problem Name of Problem you want to delete: ')
        query = "DELETE FROM PROBLEM WHERE ContestID = %d AND ProblemName = '%s'" % (
            Cid, PName)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to remove from database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def UpdateSubmission():
    try:
        SubID = int(input('Enter SubID of Submission you want to update: '))
        cur.execute(
            "SELECT ContestID,ProblemName FROM SUBMITS WHERE SubID=%d" % (SubID))
        rows = cur.fetchall()
        Cid = int(rows[0]['ContestID'])
        ProblemName = rows[0]['ProblemName']
        print('Enter the updated fields for the Submission')

        Parameter = TakeInput(
            ['SubTime', 'MEMORY', 'RUNTIME'], ['TIME', 'INT', 'INT'])

        Maxpoints = int(FetchMaxPoints(int(Cid),ProblemName))
        Parameter['POINTS'] = int(input("Enter Points in range [0,%d]: "%(Maxpoints)))
        if Parameter['POINTS'] > Maxpoints:
            print("Invalid Points")
            return

        Parameter['VERDICT'] = TakeVerdict()

        if Parameter['VERDICT'] == 'error':
            print('You Entered Wrong Verdict Number ')
            return

        Parameter['Language'] = TakeLanguage(int(Cid))
        if Parameter['Language'] == 'error':
            print('You Entered wrong Language choice. ')
            return

        query = "UPDATE SUBMISSION SET Language = '%s', SubTime = '%s', VERDICT = '%s', POINTS = %d, MEMORY = %d, RUNTIME = %d WHERE SubID = %d" % (
            Parameter['Language'], Parameter['SubTime'], Parameter['VERDICT'], int(Parameter['POINTS']), int(Parameter['MEMORY']), int(Parameter['RUNTIME']), SubID)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to Update the database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def UpdateLeader():
    try:
        TNo = int(input('Please enter Team No: '))
        Lid = int(
            input('Plase enter ProgrammerId of a contestant who is the leader: '))
        query = "UPDATE TEAM SET LeaderID=%d WHERE TNo=%d" % (Lid, TNo)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to Update the database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def print_table(json_dump):
    x = PrettyTable()
    x.field_names = json_dump[0].keys()
    for row in json_dump:
        x.add_row(row.values())
    print(x)


def SelectTeam():
    try:
        Cid = int(input('Enter Contest ID: '))
        query = 'SELECT T.TNo AS TNo, TName, CollegeName FROM TEAM T INNER JOIN PARTICIPATES P ON T.TNo = P.TNo WHERE P.ContestID = %d' % (
            Cid)
        num = cur.execute(query)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
    except Exception as e:
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def ShowStandings():
    try:
        Cid = int(input('Enter Contest ID: '))
        query0 = "DROP VIEW IF EXISTS POINT_TABLE"
        cur.execute(query0)
        query1 = "CREATE VIEW POINT_TABLE AS SELECT TNo, ContestID, ProblemName, SubID, POINTS FROM SUBMITS NATURAL JOIN SUBMISSION WHERE VERDICT='AC' AND ContestID = %d" % (
            Cid)
        cur.execute(query1)
        query2 = "SELECT RANK() OVER (ORDER BY SUM(Points) DESC) RANKING, TNo, SUM(Points) AS TOTALSCORE FROM POINT_TABLE GROUP BY ContestID, TNo"
        num = cur.execute(query2)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
        query3 = "DROP VIEW IF EXISTS POINT_TABLE"
        cur.execute(query3)
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def AcSubs():
    try:
        Cid = int(input('Enter Contest ID: '))
        TNo = int(input('Enter Team No: '))
        query = "SELECT * FROM SUBMISSION NATURAL JOIN SUBMITS WHERE VERDICT='AC' AND ContestID = %d AND TNo = %d" % (
            Cid, TNo)
        num = cur.execute(query)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
    except Exception as e:
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def CtSubs():
    try:
        query0 = "DROP VIEW IF EXISTS SFTABLE"
        cur.execute(query0)
        query1 = "CREATE VIEW SFTABLE AS SELECT ContestID, TNo,  COUNT(CASE WHEN VERDICT='AC' THEN VERDICT ELSE NULL END) AS SUCCESS , COUNT(CASE WHEN VERDICT!='AC' THEN VERDICT ELSE NULL END) AS FAIL FROM SUBMITS NATURAL JOIN SUBMISSION GROUP BY ContestID, TNo"
        query2 = "SELECT *,(SUCCESS/(SUCCESS+FAIL))*100 AS ACCURACY FROM SFTABLE"
        query3 = "DROP VIEW  IF EXISTS SFTABLE"
        cur.execute(query1)
        num = cur.execute(query2)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
        cur.execute(query3)
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def FirstSolved():
    try:
        query0 = "DROP VIEW IF EXISTS V1"
        cur.execute(query0)
        query0 = "DROP VIEW IF EXISTS V2"
        cur.execute(query0)
        Cid = int(input('Enter ContestID: '))
        query1 = "CREATE VIEW V1 AS SELECT ProblemName, TNo,SubTime FROM SUBMISSION NATURAL JOIN SUBMITS WHERE VERDICT='AC' AND ContestID=%d" % (
            Cid)
        cur.execute(query1)
        query1 = "CREATE VIEW V2 AS SELECT ProblemName,MIN(SubTime) AS SubTime FROM SUBMISSION NATURAL JOIN SUBMITS WHERE VERDICT='AC' AND ContestID=%d GROUP BY ProblemName" % (
            Cid)
        cur.execute(query1)
        query1 = "SELECT TNo,TName,ProblemName,SubTime FROM V1 NATURAL JOIN V2 NATURAL JOIN TEAM ORDER BY ProblemName"
        num = cur.execute(query1)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
        query1 = "DROP VIEW IF EXISTS V1, V2"
        cur.execute(query1)
    except Exception as e:
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)

def SearchCt():
    try:
        Fname, Lname = '', ''
        try:
            Fname = input('Enter Fname: ')
            Fname = '%' + Fname + '%'
        except:
            Fname = '%%'
        try:
            Lname = input('Enter Lname: ')
            Lname = '%' + Lname + '%'
        except:
            Lname = '%%'
        query1 = "SELECT * FROM PROGRAMMER WHERE FName LIKE '%s' AND LName LIKE '%s'" % (
            Fname, Lname)
        num = cur.execute(query1)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())

    except Exception as e:
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def SearchTN():
    try:
        name = (input('Enter team name: '))
        query1 = "SELECT * FROM TEAM WHERE TName LIKE '%%%s%%'" % (name)
        num = cur.execute(query1)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
    except Exception as e:
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def Avgtime():
    try:
        Cid = int(input('Enter Contest ID: '))
        query1 = "SELECT ProblemName, SEC_TO_TIME(AVG(TIME_TO_SEC(SubTime))) AverageTime FROM SUBMITS NATURAL JOIN SUBMISSION WHERE VERDICT='AC' AND ContestID=%d GROUP BY ProblemName" % (
            Cid)
        num = cur.execute(query1)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
    except Exception as e:
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)


def ProbSet():
    try:
        query0 = "DROP VIEW IF EXISTS T1"
        cur.execute(query0)
        query0 = "DROP VIEW IF EXISTS T4"
        cur.execute(query0)
        query1 = "CREATE VIEW T1 AS SELECT ProgrammerID,FName,LName,NumofProblems,ContestID,ProblemName,SubID,VERDICT FROM SUBMITS NATURAL JOIN SUBMISSION NATURAL JOIN PROBLEMAUTHOR NATURAL JOIN PROGRAMMER NATURAL JOIN PROBLEMSETTER"
        query2 = "CREATE VIEW T4 AS SELECT ProgrammerID,FName,LName, COUNT(CASE WHEN VERDICT='AC' THEN 1 ELSE NULL END) CRR,COUNT(CASE WHEN VERDICT!='AC' THEN 0 ELSE NULL END) WRR FROM T1 GROUP BY ProgrammerID"
        query3 = "SELECT ProgrammerID,FName,LName,(CRR/(CRR+WRR)) AS SuccessRate FROM T4"
        cur.execute(query1)
        cur.execute(query2)
        num = cur.execute(query3)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
        query = "DROP VIEW IF EXISTS T1,T4"
        cur.execute(query)
    except Exception as e:
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)

def Team1000():
    try:
        query0 = "DROP VIEW IF EXISTS TEAM_RESULT"
        cur.execute(query0)
        query0 = "DROP VIEW IF EXISTS TEAM_PT"
        cur.execute(query0)
        query1 = "CREATE VIEW TEAM_RESULT AS SELECT TNo,ContestID,SUM(Points) TotalPoints FROM SUBMITS NATURAL JOIN SUBMISSION WHERE VERDICT='AC' GROUP BY TNo,ContestID"
        cur.execute(query1)
        query2 = "CREATE VIEW TEAM_PT AS SELECT RANK() OVER (ORDER BY SUM(TotalPoints) DESC) RANKING,TNo,SUM(TotalPoints) Points FROM TEAM_RESULT GROUP BY TNo HAVING SUM(TotalPoints)>1000"
        cur.execute(query2)
        query3 = "SELECT RANKING, TNo,TName,CollegeName,Points FROM TEAM_PT NATURAL JOIN TEAM ORDER BY RANKING"
        num = cur.execute(query3)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
        query = "DROP VIEW IF EXISTS TEAM_RESULT, TEAM_PT"
        cur.execute(query)
    except Exception as e:
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)

def Showtables():
    try:
        query = "SHOW TABLES"
        cur.execute(query)
        print_table(cur.fetchall())
        Tablename = input('Please enter Table name to be displayed: ')
        query = "SELECT * FROM %s" %(Tablename.upper())
        num = cur.execute(query)
        if num == 0:
            print("There are no results for this query")
        else:
            print_table(cur.fetchall())
    except Exception as e:
        print(bcolors.CRED + bcolors.CBOLD + "Failed to Select" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND) 

def UpdateProgrammer():
    try:
        rows = TakeInput(['ProgrammerID', 'EmailID', 'Fname', 'Lname', 'Nationality', 'Age','Is_graduate'], ['INT', 'VARCHAR', 'VARCHAR', 'VARCHAR', 'VARCHAR', 'INT', 'INT'])
        query = "UPDATE PROGRAMMER SET EmailID='%s', Fname='%s', Lname='%s', Nationality='%s', Age=%d, \
            Is_graduate=%d WHERE ProgrammerID=%d" % (rows['EmailID'],\
            rows['Fname'],rows['Lname'],rows['Nationality'],int(rows['Age']),int(rows['Is_graduate']),int(rows['ProgrammerID']))
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to Update the database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)

def UpdateContest():
    try:
        rows = TakeInput(['ContestID','StartTime','Duration'],['INT','DATETIME','TIME'])
        query = "UPDATE CONTEST SET StartTime='%s', Duration='%s' WHERE ContestID=%d" % (rows['StartTime'],rows['Duration'],int(rows['ContestID']))
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print(bcolors.CRED + bcolors.CBOLD +
              "Failed to Update the database" + bcolors.CEND)
        print(bcolors.CRED + bcolors.CBOLD + ">>>>>>>>>>>>>", e, bcolors.CEND)

def dispatch(ch):
    """ 
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        Addcontest()
    elif(ch == 2):
        AddTeam()
    elif(ch == 3):
        Participates()
    elif(ch == 4):
        AddProgrammer()
    elif(ch == 5):
        AddProblem()
    elif(ch == 6):
        Addsubmission()
    elif(ch == 7):
        RmContest()
    elif(ch == 8):
        RmTeam()
    elif(ch == 9):
        RmProblem()
    elif(ch == 10):
        UpdateSubmission()
    elif(ch == 11):
        UpdateLeader()
    elif(ch == 12):
        UpdateProgrammer()
    elif(ch == 13):
        UpdateContest()
    elif(ch == 14):
        SelectTeam()
    elif(ch == 15):
        ShowStandings()
    elif(ch == 16):
        AcSubs()
    elif(ch == 17):
        CtSubs()
    elif(ch == 18):
        FirstSolved()
    elif(ch == 19):
        Team1000()
    elif(ch == 20):
        SearchCt()
    elif(ch == 21):
        SearchTN()
    elif(ch == 22):
        Avgtime()
    elif(ch == 23):
        ProbSet()
    elif(ch == 24):
        Showtables()
    else:
        print(bcolors.CRED + bcolors.CBOLD +
              "Error: Invalid Option" + bcolors.CEND)


# Global
while(1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")
    port = int(input("Enter Port number: "))
    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='CPTOURNAMENT',
                              port=port,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print(bcolors.CRED + bcolors.CBOLD +
                  "Failed to connect" + bcolors.CEND)
    except:
        tmp = sp.call('clear', shell=True)

        print(bcolors.CRED + bcolors.CBOLD +
              "Connection Refused: Either username or password is incorrect or user doesn't have access to database" + bcolors.CEND)
        tmp = input("Enter any key to CONTINUE> ")
        continue

    tmp = input("Enter any key to CONTINUE> ")

    with con.cursor() as cur:
        while(1):
            tmp = sp.call('clear', shell=True)
            # CHANGED.
            # Here taking example of Employee Mini-world
            print("""
            1.  Add a Contest
            2.  Add a Team
            3.  Add participation of team in a contest.
            4.  Add a Programmer
            5.  Add a Problem
            6.  Add a Submission
            7.  Remove Contest
            8.  Remove Team
            9.  Remove Problem 
            10. Update Submission
            11. Update Leader of a Team
            12. Update Programmer details
            13. Update Contest details
            14. See all Teams in a Contest
            15. Show the contest standings
            16. List all successful submission of team in a contest
            17. Show the count of successful and unsuccessful submissions of a team
            18. List the first team to solve each problem
            19. List the highest scoring teams across all contests with more than 1000 points
            20. Search for contestant name
            21. Search for team name
            22. Show the average time spent on each problem
            23. Show the toughest problemsetters (successful submission rate on his/her/its problems)
            24. Display any table
            25. Logout of Database
            """)
            try:
                ch = int(input("Enter choice> "))
            except:
                continue
            tmp = sp.call('clear', shell=True)
            if ch == 25:
                break
            else:
                dispatch(ch)
                tmp = input("Enter any key to CONTINUE> ")
