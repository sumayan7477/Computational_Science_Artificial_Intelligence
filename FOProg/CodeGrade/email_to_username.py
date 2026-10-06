def extract_one(email):
    norm_email = email.strip().lower()
    a_index = norm_email.find("@")
    username= norm_email[:a_index]
    return username


def extract_all(email_list):
    temp = []
    for elem in email_list:
        username = extract_one(elem)

        if username not in temp:
            temp.append(username)
    return temp
