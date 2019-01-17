import csv
from yattag import Doc


def read_user_info(filename):
    file = open(filename, mode="r")
    lines = list(csv.reader(file))
    keys = lines[0]
    user_info = {}
    for index in range(0, len(keys) - 1):
        user_info[keys[index].lstrip().rstrip()] = lines[1][index]
    file.close()
    return user_info


def build_html(user_info):
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.stag('meta', charset='utf-8')
            with tag('title'):
                text('user_info')
            doc.stag('link', rel='stylesheet', href='style.css', type='text/css')
        with tag('body'):
            with tag('h1'):
                text('Visit card')
            doc.stag('img', src=user_info['photo'], alt='user_photo', width=200, height=200)
            with tag('p'):
                with tag('strong'):
                    text('First name:\t')
                text(user_info['first_name'])
            with tag('p'):
                with tag('strong'):
                    text('Last name:\t')
                text(user_info['last_name'])
            with tag('p'):
                with tag('strong'):
                    text('Age:\t')
                text(str(user_info['age']) + ' years')
            with tag('p'):
                with tag('strong'):
                    text('Gender:\t')
                text(user_info['gender'])
            with tag('p'):
                with tag('strong'):
                    text('Education:\t')
                text(user_info['education'])
            with tag('p'):
                with tag('strong'):
                    text('Hobby:\t')
                text(user_info['hobby'])
            with tag('p'):
                with tag('strong'):
                    text('Email:\t')
                text(user_info['email'])
    return doc.getvalue()


def save_file(filename, data_to_write):
    file = open(filename, mode='w')
    file.write(data_to_write)
    file.close()


user = read_user_info('user.csv')
print(user)
html = build_html(user)
print(html)
save_file('index.html', html)

