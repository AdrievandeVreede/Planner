import datetime


def CreateTime(hour=0, minute=0, second=0):
    time = datetime.time(hour, minute, second)
    time = TimeFormat(
        time,
        hour=True if hour != 0 else False,
        minute=True if (minute != 0) or (second > 0) else False,
        second=True if second != 0 else False
    )
    return time


def TimeDifference(time, output="str", hour=True, minute=True, second=False):
    start = TimeFormat(time[0], time_format_output="intList", second=True)
    end = TimeFormat(time[1], time_format_output="intList", second=True)
    hour_difference = end[0] - start[0]
    minute_difference = end[1] - start[1]
    second_difference = end[2] - start[2]
    if second_difference < 0:
        minute_difference -= 1
        second_difference = 60 + second_difference
    if minute_difference < 0:
        hour_difference -= 1
        minute_difference = 60 + minute_difference

    if output == "str":
        time_difference = ""
        time_difference += str(hour_difference) if hour else ""
        time_difference += ":" if (time_difference != "") and minute else ""
        time_difference += str(minute_difference) if minute else ""
        time_difference += ":" if (time_difference != "") and second else ""
        time_difference += str(second_difference) if second else ""
        return time_difference
    elif output == "intList":
        time_difference = [hour_difference, minute_difference, second_difference]
        return time_difference
    elif output == "list":
        time_difference = [str(hour_difference), str(minute_difference), str(second_difference)]
        return time_difference


def TimeFormat(time, time_format_output="str", hour=True, minute=True, second=False):
    time_str = str(time)
    time_list = time_str.split(":")
    if len(time_list) < 3:
        length = len(time_list)
        needs = 3 - length
        for i in range(needs):
            time_list.append("0")
    hour_ = int(time_list[0])
    minute_ = int(time_list[1])
    second_ = int(time_list[2])
    if (hour_ >= 0) and not hour:
        for i in range(hour_):
            minute_ += 60
    if (minute_ >= 0) and not minute:
        for i in range(minute_):
            second_ += 60
    time_new = ""
    if hour and not minute and second:
        return "Failure 500\nCouldn't set hour and second only\nTry hour and minute or hour, minute and second"
    if hour:
        time_new += str(hour_)
    if minute:
        time_new += ":" if time_new != "" else ""
        time_new += str(minute_)
    if second:
        time_new += ":" if time_new != "" else ""
        time_new += str(second_) if len(str(second_)) == 2 else "0" + str(second_)
    if time_format_output == "str":
        return str(time_new)
    elif time_format_output == "list":
        return list(time_new.split(":"))
    elif time_format_output == "intList":
        time_new = time_new.split(":")
        time_new = [int(i) for i in time_new]
        return time_new
