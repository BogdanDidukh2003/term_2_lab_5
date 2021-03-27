def main():
    START = b"[01/Jul/1995:00:10"
    END = b"[01/Jul/1995:20:"
    KEEP_PHRASE = b"NASA"
    needed_time_lines = []
    contains_phrase = []
    is_needed_time = False
    line_counter = 0
    with open("access_log_Jul95", 'rb') as a:
        f = a.readlines()

    for line in f:
        if START in line:
            is_needed_time = True
        if is_needed_time:
            needed_time_lines.append(line)
        if END in line:
            is_needed_time = False
            break

    for line in needed_time_lines:
        if KEEP_PHRASE in line:
            line_counter = line_counter + 1 
            contains_phrase.append(line)

    print(line_counter)


if __name__ == '__main__':
    main()
