# Author: @Travis-Owens
# Date: 2020-01-25

from classes.database import data_handler

class request_logging(object):
    def process_request(self, req, resp):
        # This function will create a data-structure with details of the request, and add it to the database
        sql = "INSERT INTO `logging` (`log`) VALUES (%s)"

        data_handler().insert(sql, req)

        return
