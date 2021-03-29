def main():
    START = b"[01/Jul/1995:00:10:"
    END = b"[01/Jul/1995:00:20:"
    KEEP_PHRASE = b"NASA"
    is_needed_time = False
    line_counter = 0
    
    with open("access_log_Jul95", 'rb') as a:
        f = a.readlines()

    for line in f:
        if END in line:
            is_needed_time = False
            break
        if START in line:
            is_needed_time = True
        if is_needed_time and KEEP_PHRASE in line:
            line_counter = line_counter + 1

    print(line_counter)


if __name__ == '__main__':
    main()
