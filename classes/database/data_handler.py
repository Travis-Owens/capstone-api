# Author: @Travis Owens
# Date: 2020-02-20
# Description: Misc data retreival functions

import pymysql
import config

class data_handler(object):
    def __init__(self):

        self.defined_queries = {
            'discord_channels_by_twitch_user_id':'SELECT DISTINCT `discord_channel_id` FROM `twitch` WHERE `twitch_user_id`=%s',
            'unique_twitch_notification':'SELECT * FROM `twitch` WHERE `twitch_username` = %s  AND `discord_channel_id` = %s',
            'add_twitch_notification':'INSERT INTO `twitch` VALUES(null,%s,%s,%s)',
            'delete_twitch_notification':'DELETE FROM `twitch` WHERE `twitch_username`=%s AND `twitch_user_id`=%s AND `discord_channel_id`=%s'
        }


    def get_connection(self):
        return(pymysql.connect(host=config.db_host,
                                     user=config.db_user,
                                     password=config.db_password,
                                     db=config.db_name,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor))


    def defined_select(self, key, input, values_only=False):
        # key = dict key for query in self.defined_queries.
        # input = Values to insert into the defined query.
        # values_only = strip the values from the cursor.fetchall(),
        #   ex: list of discord_channel_ids; instead of list of dicts

        conn = self.get_connection()

        with conn.cursor() as cursor:
            cursor.execute(self.defined_queries[key], input)

        if(values_only == True):
            data = cursor.fetchall()
            output = list()

            for x in data:
                output.append(x['discord_channel_id'])

            return output

        return(cursor.fetchall())

    def defined_insert(self, key, input):

        try:
            conn = self.get_connection()

            with conn.cursor() as cursor:
                cursor.execute(self.defined_queries[key], input)

            conn.commit()
            conn.close()

            return(True)

        except Exception as e:
            return(False)

    def defined_delete(self, key, input):

        try:
            conn = self.get_connection()

            with conn.cursor() as cursor:
                cursor.execute(self.defined_queries[key], input)

            conn.commit()
            conn.close()

            return(True)

        except Exception as e:
            return(False)


    def select(self, sql, input, values_only=False):
        conn = self.get_connection()

        # String escape SQL
        sql = conn.escape(sql)

        with conn.cursor() as cursor:
            cursor.execute(sql, input)

        # if(values_only == True):
        #     data = cursor.fetchall()
        #     return(list(map(lambda x : x['discord_channel_id'], data)))

        return(cursor.fetchall())

    def insert(self, sql, input):

        try:
            conn = self.get_connection()

            # String escape SQL
            sql = conn.escape(sql)

            with conn.cursor() as cursor:
                cursor.execute(sql, input)

            conn.commit()
            conn.close()

            return(True)
        except Exception as e:
            print(e)
            return(False)

    def update(self, sql, input):

        try:
            conn = self.get_connection()

            # String escape SQL
            sql = conn.escape(sql)

            with conn.cursor() as cursor:
                cursor.execute(sql, input)

            conn.commit()
            conn.close()

            return(True)
        except Exception as e:
            print(e)
            return(False)
