class Employee:
    def __init__(self, id, name, department, job_title):
        self.__id_number = id
        self.__name = name
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id_number = id

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, title):
        self.__job_title = title

    def __str__(self):
        return 'Name: ' + self.__name + \
            '\n' + 'ID: ' + str(self.__id_number) \
            + '\n' + 'Department: ' + self.__department \
            + '\n' + 'Job Title: ' + self.__job_title
