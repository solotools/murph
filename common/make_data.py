from faker import Faker

"""
    print('name:', faker.job())
    print('address:', faker.address())
    print('text:', faker.mac_address())
"""


def data_create(data_type):
    """

    :param data_type:1 == address ,other == name
    :return:address or name
    """
    faker = Faker(locale='zh_CN')
    if data_type == 1:

        return '- address：' + faker.address() + '  '
    else:
        return faker.name()

# print(data_create(2))
