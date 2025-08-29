from abc import ABC, abstractmethod

class AttendanceData:
    def __init__(self):
        self.name_playerID_dict = {}
        self.data_playerID_day = [[0] * 100 for _ in range(100)]
        self.playerID_score_grade_list = [[0, 0] for _ in range(100)]
        self.name_list = [''] * 100

    def txt_to_data(self, txt):
        with open(txt, encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line: break
                if len(line.strip().split()) == 2:
                    self.get_attendance_point(line.strip().split()[0], line.strip().split()[1])
        return

    def get_attendance_point(self, name: str, weekday: str) -> None:
        self.name_enrollment(name)
        self.dayindex_point(self.name_playerID_dict[name], weekday)

    def name_enrollment(self, name: str):
        if name not in self.name_playerID_dict:
            self.name_playerID_dict[name] = len(self.name_playerID_dict) + 1
            self.name_list[len(self.name_playerID_dict)] = name

    def dayindex_point(self, playerID: int, weekday: str):
        if weekday == "monday":
            day: Weekday = Monday()
        elif weekday == "tuesday":
            day: Weekday = Tuesday()
        elif weekday == "wednesday":
            day: Weekday = Wednesday()
        elif weekday == "thursday":
            day: Weekday = Thursday()
        elif weekday == "friday":
            day: Weekday = Friday()
        elif weekday == "saturday":
            day: Weekday = Saturday()
        elif weekday == "sunday":
            day: Weekday = Sunday()
        self.data_playerID_day[playerID][day.dayindex()] += 1
        self.playerID_score_grade_list[playerID][0] += day.add_point()


class Weekday(ABC):
    def __init__(self):
        self._dayindex = 0
        self._add_point = 0

    @abstractmethod
    def dayindex(self):
        pass

    @abstractmethod
    def add_point(self):
        pass


class Monday(Weekday):
    def dayindex(self):
        self._dayindex = 0
        return self._dayindex

    def add_point(self):
        self._add_point = 1
        return self._add_point


class Tuesday(Weekday):
    def dayindex(self):
        self._dayindex = 1
        return self._dayindex

    def add_point(self):
        self._add_point = 1
        return self._add_point


class Wednesday(Weekday):
    def dayindex(self):
        self._dayindex = 2
        return self._dayindex

    def add_point(self):
        self._add_point = 3
        return self._add_point


class Thursday(Weekday):
    def dayindex(self):
        self._dayindex = 3
        return self._dayindex

    def add_point(self):
        self._add_point = 1
        return self._add_point


class Friday(Weekday):
    def dayindex(self):
        self._dayindex = 4
        return self._dayindex

    def add_point(self):
        self._add_point = 1
        return self._add_point


class Saturday(Weekday):
    def dayindex(self):
        self._dayindex = 5
        return self._dayindex

    def add_point(self):
        self._add_point = 2
        return self._add_point


class Sunday(Weekday):
    def dayindex(self):
        self._dayindex = 6
        return self._dayindex

    def add_point(self):
        self._add_point = 2
        return self._add_point


def input_file(txt:str):
    try:
        attendancedata = AttendanceData()
        attendancedata.txt_to_data(txt)

        print_name_point_grade(attendancedata)
        print_removed_player(attendancedata)


    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def print_removed_player(attendancedata):
    print("\nRemoved player")
    print("==============")
    for player_index in range(1, len(attendancedata.name_playerID_dict) + 1):
        if (attendancedata.playerID_score_grade_list[player_index][1] not in (1, 2)
                and attendancedata.data_playerID_day[player_index][2] == 0
                and sum(attendancedata.data_playerID_day[player_index][5:]) == 0):
            print(attendancedata.name_list[player_index])


def print_name_point_grade(attendancedata):
    for player_index in range(1, len(attendancedata.name_playerID_dict) + 1):
        bonus_score(attendancedata, player_index)
        determine_grade(attendancedata, player_index)
        print(
            f"NAME : {attendancedata.name_list[player_index]}, POINT : {attendancedata.playerID_score_grade_list[player_index][0]}, GRADE : ",
            end="")
        if attendancedata.playerID_score_grade_list[player_index][1] == 1:
            print("GOLD")
        elif attendancedata.playerID_score_grade_list[player_index][1] == 2:
            print("SILVER")
        else:
            print("NORMAL")


def bonus_score(attendancedata: AttendanceData, player_index: int):
    if attendancedata.data_playerID_day[player_index][2] > 9:
        attendancedata.playerID_score_grade_list[player_index][0] += 10
    if attendancedata.data_playerID_day[player_index][5] + attendancedata.data_playerID_day[player_index][6] > 9:
        attendancedata.playerID_score_grade_list[player_index][0] += 10


def determine_grade(attendancedata: AttendanceData, player_index: int):
    if attendancedata.playerID_score_grade_list[player_index][0] >= 50:
        attendancedata.playerID_score_grade_list[player_index][1] = 1
    elif attendancedata.playerID_score_grade_list[player_index][0] >= 30:
        attendancedata.playerID_score_grade_list[player_index][1] = 2
    else:
        attendancedata.playerID_score_grade_list[player_index][1] = 0


if __name__ == "__main__":
    input_file("attendance_weekday_500.txt")
