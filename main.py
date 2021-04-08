import data
import Controllers as func

monday = data.day_scheme[0]
diff = func.TimeDifference(monday[1])

print(diff)
