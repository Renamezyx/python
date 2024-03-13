def generate_control_xy():
    start_x = 50
    start_y = 100
    while True:
        yield (start_x, start_y)
        if start_x + 120 >= 800:
            start_y += 70
            start_x = 50
        else:
            start_x += 170


if __name__ == '__main__':
    gen = generate_control_xy()
    for _ in range(5):
        print(next(gen))
