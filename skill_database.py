import sqlite3

class SkillDatabase:
    def __init__(self):
        pass

    def getData(self, job_role, skill_type):
    
        try:
            #Connecting to sqlite
            conn = sqlite3.connect('career_map.db')

            #Creating a cursor object using the cursor() method
            cursor = conn.cursor()
            
            #Query to select data with following condition
            if skill_type=='soft skill':
                cursor.execute("SELECT * FROM SOFTSKILLS WHERE JOB_ROLE IS '%s' COLLATE NOCASE ORDER BY FREQUENCY DESC;" %job_role)
            else:
                cursor.execute("SELECT * FROM HARDSKILLS WHERE JOB_ROLE IS '%s' COLLATE NOCASE ORDER BY FREQUENCY DESC;" %job_role)
            #statement to fetch data
            data = cursor.fetchall()

            # Commit your changes in the database
            conn.commit()

            #Closing the connection
            conn.close()

            return data
        except Exception as e:
            print("Error:",e)
            return []