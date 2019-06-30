import re

with open('phonebook.csv', encoding='utf8') as book:
    data = []

    for line in book:
        lastname = ''
        firstname = ''
        surname = ''
        organization = ''
        position = ''
        phone = ''
        email = ''
        count = -1
        line = line.split(',')
        if not line[2]:
            name = line[0].split(' ')
            secondname = line[1].split(' ')
            lastname = name[0]
            try:
                firstname = name[1]
                try:
                    surname = name[2]
                except:
                    surname = secondname[0]
            except:
                firstname = secondname[0]
                surname = secondname[1]
        else:
            lastname = line[0]
            firstname = line[1]
            surname = line[2]
        organization = line[3]
        position = line[4]





        phone_raw = line[5].replace(' ','').replace('-', '').replace('+', '').replace('(', '').replace(')', '')

        phone_zero = "(8|\+7)?(\s)*(\(\d+\))(\s)*(\d+)([-\s])(\d+)([-\s])(\d+)"
        phone_two = re.findall(phone_zero, phone_raw)
        phone_raw = re.sub(phone_zero, r"+7\3\5-\7-\9", phone_raw)

        if 'до' in phone_raw:
            phone = '+7(' + phone_raw[1:4] + ')' + phone_raw[4:7] + '-' + phone_raw[7:9] + '-' + phone_raw[9:11] + ' доб.' + phone_raw[-4:-1] + phone_raw[-1]
        elif phone_raw == 'phone':
            phone = 'phone'
        elif not phone_raw:
            phone = ''
        else:
            phone = '+7(' + phone_raw[1:4] + ')' + phone_raw[4:7] + '-' + phone_raw[7:9] + '-' + phone_raw[9:11]
        email = line[6]
        true_line = lastname + ',' + firstname + ',' + surname + ',' + organization + ',' + position + ',' + phone + ',' + email.replace('\n', '')
        line_for_assert = true_line.split(',')
        if not data:
            data.append(true_line)
        else:
            for contact in data:
                count += 1
                double = False
                contact = contact.split(',')
                if contact[1] == line_for_assert[1] and contact[3] == line_for_assert[3]:
                    double = True

                    if not contact[0]:
                        lastname = line_for_assert[0]
                    elif not line_for_assert[0]:
                        lastname = contact[0]
                    if not contact[1]:
                        firstname = line_for_assert[1]
                    elif not line_for_assert[1]:
                        firstname = contact[1]
                    if not contact[2]:
                        surname = line_for_assert[2]
                    elif not line_for_assert[2]:
                        surname = contact[2]
                    if not contact[3]:
                        organization = line_for_assert[3]
                    elif not line_for_assert[3]:
                        organization = contact[3]
                    if not contact[4]:
                        position = line_for_assert[4]
                    elif not line_for_assert[4]:
                        position = contact[4]
                    if not contact[5]:
                        phone = line_for_assert[5]
                    elif not line_for_assert[5]:
                        phone = contact[5]
                    if not contact[6]:
                        email = line_for_assert[6]
                    elif not line_for_assert[6]:
                        email = contact[6]
                    true_line = lastname + ',' + firstname + ',' + surname + ',' + organization + ',' + position + ',' + phone + ',' + email.replace(
                        '\n', '')
                    data.pop(count)
                    data.append(true_line)

            if not double:
                data.append(true_line)

with open('test.txt', 'w', encoding='cp1251') as lin:
    for line in data:
        lin.write(line)
        lin.write('\n')



