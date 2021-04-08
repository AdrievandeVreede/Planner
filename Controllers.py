def TimeDifference(time, output="str", hour=True, minute=True, second=False):
    start = TimeFormat(time[0], time_format_output="intList")
    end = TimeFormat(time[1], time_format_output="intList")
    hour_difference = end[0] - start[0] if hour else 0
    minute_difference = end[1] - start[1] if minute else 0
    second_difference = end[2] - start[2] if second else 0
    if second_difference < 0:
        minute_difference -= 1
        second_difference = 60 + second_difference
    if minute_difference < 0:
        hour_difference -= 1
        minute_difference = 60 + minute_difference

    if output == "str":
        time_difference = ""
        time_difference += str(hour_difference) if hour else ""
        time_difference += ":" if time_difference != "" else ""
        time_difference += str(minute_difference) if minute else ""
        time_difference += ":" if (time_difference != "") and (second_difference > 0) else ""
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
    time_new = ""
    if hour:
        time_new += str(time_list[0])
    if minute:
        time_new += ":" if time_new != "" else None
        time_new += str(time_list[1])
    if second:
        time_new += ":" if time_new != "" else None
        time_new += str(time_list[2])
    if time_format_output == "str":
        return str(time_new)
    elif time_format_output == "list":
        return list(time_new.split(":"))
    elif time_format_output == "intList":
        time_new = time_new.split(":")
        time_new = [int(i) for i in time_new]
        return time_new
