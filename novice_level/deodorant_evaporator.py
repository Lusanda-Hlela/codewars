def evaporator(content, evap_per_day, threshold):
    th = (threshold / 100) * content
    count = 0
    while content >= th:
        epd = (evap_per_day / 100) * content
        content -= epd
        count += 1
    return count