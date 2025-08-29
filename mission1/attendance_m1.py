WEEKDAY_TXT = "attendance_weekday_500.txt"

name_playerID_dict = {}
playerID_cnt = 0
data_playerID_day = [[0] * 100 for _ in range(100)]
playerID_score_list = [0] * 100
playerID_grade_list = [0] * 100
name_list = [''] * 100

def get_attendance_point(name:str, weekday:str)->None:
    name_enrollment(name)
    playerID = name_playerID_dict[name]

    add_point, dayindex = dayindex_point(weekday)

    data_playerID_day[playerID][dayindex] += 1
    playerID_score_list[playerID] += add_point


def dayindex_point(weekday):
    if weekday == "monday":
        dayindex = 0
        add_point = 1
    elif weekday == "tuesday":
        dayindex = 1
        add_point = 1
    elif weekday == "wednesday":
        dayindex = 2
        add_point = 3
    elif weekday == "thursday":
        dayindex = 3
        add_point = 1
    elif weekday == "friday":
        dayindex = 4
        add_point = 1
    elif weekday == "saturday":
        dayindex = 5
        add_point = 2
    elif weekday == "sunday":
        dayindex = 6
        add_point = 2
    return add_point, dayindex


def name_enrollment(name):
    global playerID_cnt
    if name not in name_playerID_dict:
        playerID_cnt += 1
        name_playerID_dict[name] = playerID_cnt
        name_list[playerID_cnt] = name


def input_file():
    try:
        txt_to_data(WEEKDAY_TXT)

        for player_index in range(1, playerID_cnt + 1):
            bonus_score(player_index)
            determine_grade(player_index)
            print(f"NAME : {name_list[player_index]}, POINT : {playerID_score_list[player_index]}, GRADE : ", end="")
            if playerID_grade_list[player_index] == 1:
                print("GOLD")
            elif playerID_grade_list[player_index] == 2:
                print("SILVER")
            else:
                print("NORMAL")

        print("\nRemoved player")
        print("==============")
        for player_index in range(1, playerID_cnt + 1):
            if playerID_grade_list[player_index] not in (1, 2) and data_playerID_day[player_index][2] == 0 and sum(data_playerID_day[player_index][5:]) == 0:
                print(name_list[player_index])

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def bonus_score(player_index):
    if data_playerID_day[player_index][2] > 9:
        playerID_score_list[player_index] += 10
    if data_playerID_day[player_index][5] + data_playerID_day[player_index][6] > 9:
        playerID_score_list[player_index] += 10


def determine_grade(player_index):
    if playerID_score_list[player_index] >= 50:
        playerID_grade_list[player_index] = 1
    elif playerID_score_list[player_index] >= 30:
        playerID_grade_list[player_index] = 2
    else:
        playerID_grade_list[player_index] = 0


def txt_to_data(txt):
    with open(txt, encoding='utf-8') as f:
        for _ in range(500):
            line = f.readline()
            if not line:break
            if len(line.strip().split()) == 2:
                get_attendance_point(line.strip().split()[0], line.strip().split()[1])


if __name__ == "__main__":
    input_file()
