def main():
    course_rooms = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
    course_instructors = {'CS101':'Hayes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    course_times = {'CS101':'8:00AM','CS102':'9:00AM','CS103':'10:00AM','NT110':'11:00AM','CM241':'1:00PM'}

    print_menu()
    user_input = input('Enter a course number from the above and I will give you information about it.')

    if(user_input in course_rooms):
        print('you have selected course: ' + user_input)
        print('room: ' + course_rooms[user_input])
        print('instructor: ' + course_instructors[user_input])
        print('time: ' + course_times[user_input])
def print_menu():
    courses = ['CS101','CS102','CS103','NT110','CM241']
    print('The following courses are: ', end=' ')
    for course in courses:
        print(course)
main()