def to_12(time):
    extracted_hr = int(time[:2])
    extracted_min = time[2:]
    if extracted_hr == 12:
        return f"{extracted_hr}:{extracted_min} PM"
    elif extracted_hr >=1 and extracted_hr <=11:
        return f"{extracted_hr}:{extracted_min} AM"
    elif extracted_hr > 12:
        extracted_hr -= 12
        return f"{extracted_hr}:{extracted_min} PM"
    elif extracted_hr == 0:
        extracted_hr += 12
        return f"{extracted_hr}:{extracted_min} AM"