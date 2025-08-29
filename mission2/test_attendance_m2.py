import pytest
import attendance_m2

WEEKDAY_TXT = "C:/Users/User/PycharmProjects/PythonProject/AttendanceManager_ChoYoungJun250829/mission2/attendance_weekday_500.txt"

@pytest.fixture
def attendance():
    attendance = attendance_m2.AttendanceData()
    return attendance


@pytest.fixture
def day():
    monday = attendance_m2.Monday()
    tuesday = attendance_m2.Tuesday()
    wednesday = attendance_m2.Wednesday()
    thursday = attendance_m2.Thursday()
    friday = attendance_m2.Friday()
    saturday = attendance_m2.Saturday()
    sunday = attendance_m2.Sunday()
    return [monday,tuesday,wednesday,thursday,friday,saturday,sunday]


@pytest.mark.parametrize("index,weekday,value",[(0,'monday',1),(1,'tuesday',1),(2,'wednesday',3),(3,'thursday',1),(4,'friday',1),(5,'saturday',2),(6,'sunday',2)])
def test_day_check(attendance, day,index,weekday,value):
    # print(index,weekday)
    attendance.dayindex_point(0, weekday)
    assert day[index].add_point() == value

def test_txt_to_data(attendance):
    result=attendance.txt_to_data("attendance_weekday_500.txt")
    assert result == None

def test_get_attendace_point(attendance):
    attendance.get_attendance_point('youngjun','monday')
    assert attendance.name_list[1]=='youngjun'
    assert attendance.name_playerID_dict['youngjun']==1

def test_input_file():
   result=attendance_m2.input_file("attendance_weekday_500.txt")
   assert result == None

def test_input_file_error():
   result=attendance_m2.input_file("attendance_weekday_501.txt")
   assert result == None

