from helper.sb_help import *

def test_verify_user():
    assert verify_exist_user("juanprueba") == True
    assert verify_exist_user("juanprueba") != None

def test_get_name_user():
    assert get_name_user_sb_by_id(1) == "juanprueba"

