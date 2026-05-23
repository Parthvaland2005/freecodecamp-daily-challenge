def is_rotation(issue, pr):

    a = str(issue)
    b = str(pr)

    max_len = max(len(a), len(b))

    a = a.zfill(max_len)
    b = b.zfill(max_len)

    if a == b:
        return False

    return b in (a + a)


def get_open_issues(issues, prs):

    open_issues = []

    for issue in issues:

        closed = False

        for pr in prs:

            if is_rotation(issue, pr):
                closed = True
                break

        if not closed:
            open_issues.append(issue)

    return open_issues

print(get_open_issues([123, 234], [231]))

print(get_open_issues([123, 345, 16], [345, 231]))

print(get_open_issues([456, 332, 12, 15], [201, 945, 180]))

print(get_open_issues([12, 115, 296, 170, 24], [17, 18, 19, 20, 21]))

print(get_open_issues(
    [19, 95, 422, 395, 754, 102, 296, 709, 237, 4400, 1802],
    [395, 440, 9001, 95, 242, 21, 287, 169, 14]
))