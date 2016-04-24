import sqlite3


class PreferencesFetcher():

    def __init__(self, db_connection):
        self.cursor = sqlite3.connect(db_connection).cursor()

    def fetch_time_preference(self, user_id):
        """
        user_id is an integer
        """
        query = "SELECT time FROM preferences_userpreferences WHERE user_id = '%s'" % user_id
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def fetch_sub_preference(self, user_id):
        sub_list = []
        query = "SELECT id FROM preferences_userpreferences WHERE user_id='%s';" % user_id
        self.cursor.execute(query)
        user_pref_id = (self.cursor.fetchone()[0],)
        query = "SELECT subchoice_id FROM preferences_userpreferences_sub WHERE userpreferences_id='%s';" % user_pref_id
        self.cursor.execute(query)
        subs = self.cursor.fetchall()
        for sub in subs:
            query = "SELECT name FROM preferences_subchoice WHERE id='%s'" % sub[
                0]
            self.cursor.execute(query)
            name = self.cursor.fetchone()
            sub_list.append(name[0])
        return sub_list


class UserFetcher():

    def __init__(self, db_connection):
        self.cursor = sqlite3.connect(db_connection).cursor()

    def fetch_auth_users(self):
        query = "SELECT user_id FROM socialaccount_socialaccount"
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def fetch_auth_token(self, user_id):
        query = "SELECT id FROM socialaccount_socialaccount WHERE user_id='%s';" % user_id
        self.cursor.execute(query)
        account_id = self.cursor.fetchone()
        query = "SELECT token FROM socialaccount_socialtoken WHERE account_id='%s';" % account_id
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
