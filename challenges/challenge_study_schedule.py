def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None

    count = 0

    for period in permanence_period:
        entry_time, exit_time = period

        if type(entry_time) != int or type(exit_time) != int:
            return None

        if entry_time <= target_time and exit_time >= target_time:
            count += 1

    return count

    

# permanence_period = [{12,16}, {10,14}, {11,15}, {9,13}]
