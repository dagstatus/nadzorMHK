import hashlib
import pickle
from nadzor_base import CONFIG_NADZOR


class UserAccess:
    def __init__(self):
        self.result = False

    def create_user(self, new_user_name, new_user_pass: str):
        pass_str = str(new_user_pass)
        hash_pass = hashlib.sha1(pass_str.encode('utf-8'))
        pass_hex = hash_pass.hexdigest()
        file = open(CONFIG_NADZOR.user_db_file, 'wb')
        pickle.dump({new_user_name: pass_hex}, file)
        file.close()

        return True

    def check_user(self, user_name, password):
        login_flag = False
        pass_to_hex = hashlib.sha1(str(password).encode('utf-8')).hexdigest()
        with open(CONFIG_NADZOR.user_db_file, 'rb') as user_file:
            dict_users = pickle.load(user_file)

        if user_name in dict_users:
            # print(f'{user_name} is in file')

            pass_user_db = dict_users.get(user_name)
            # print(pass_user_db)
            if pass_user_db == pass_to_hex:
                print('PASS GOOD')
                login_flag = True
            else:
                print('PASS BAD')
        else:
            print(f'No user {user_name}')

        return login_flag



    def change_pass(self):
        pass

    def get_users_test(self):
        file = open(CONFIG_NADZOR.user_db_file, 'rb')
        usr_pass = pickle.load(file)
        file.close()
        print(usr_pass)
        print(hashlib.sha1('213517283612'.encode('utf-8')).hexdigest())

if __name__ == '__main__':
    Test = UserAccess()
    # Test.create_user('Tima', 213517283612)

    # Test.check_user('Tima', 213517283612)
    # Test.check_user('Tima', 'sadas')
    # Test.create_user('admin', 'admin')

