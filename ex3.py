def ends_of_string(str):
    if len(str) < 2:
        return ''
    return str[0:6] + str[-2:]
print(ends_of_string('Sleepyisme'))