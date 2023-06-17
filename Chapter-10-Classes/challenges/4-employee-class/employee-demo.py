import employee


def main():
    employee1 = employee.Employee(234, 'lmao', 'yeet', 'edgelord')
    employee1.set_id(12345)
    employee1.set_name('Susan Meyers')
    employee1.set_job_title('Legend')
    employee1.set_department('Vice President')

    print(employee1)


main()
