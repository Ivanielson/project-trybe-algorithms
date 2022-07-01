def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if not target_time:
        return None
    count = 0
    for start, end in permanence_period:
        if not isinstance(start, int) or not isinstance(end, int):
            return None
        if target_time >= start and target_time <= end:
            count += 1
    return count
