def format(seconds):
    hours = seconds//3600
    minutes = (seconds%3600) // 60
    left_over = seconds % 60
    if hours>0:
        return f"{hours}:{minutes:02d}:{left_over:02d}"
    else:
        return f"{minutes}:{left_over:02d}"


print(format(500))
print(format(4000))
print(format(1))
print(format(5555))
print(format(99999))