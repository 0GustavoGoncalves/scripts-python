def add_time(start, duration, day = None):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    start_hour, start_min, start_period = int(start.split()[0].split(':')[0]),int(start.split()[0].split(':')[1]), start.split()[1]
    start_to_min = (start_hour*60) + start_min + ((12*60) if start_period == 'PM' else 0)
    duration_to_min = (int(duration.split(':')[0])*60) + int(duration.split(':')[1])    
    sum_time = start_to_min + duration_to_min
    day_count = sum_time // 1440
    min_to_calc = sum_time % 1440
    end_hour, end_min = min_to_calc // 60, min_to_calc % 60
    end_period = 'PM' if end_hour > 12 or (end_hour == 12 and end_min > 0) else 'AM'
    if end_hour > 12:
        end_hour -= 12
    if end_hour == 0:
        end_hour = 12
    if end_min < 10:
        end_min = f'0{end_min}'
    new_time = f'{end_hour}:{end_min} {end_period}'
    if day != None:
        day = day.capitalize()
        day_index = (days.index(day) + day_count) % len(days)
        new_time += ', ' + days[day_index]
    if day_count == 1:
        new_time += ' (next day)'
    elif day_count > 1:
        new_time += f' ({day_count} days later)'
    return new_time

