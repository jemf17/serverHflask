#from database.sb_conection import supabase
from database.db_connection import DB
from uuid import UUID


def get_role_user(uuid: UUID):
    supa = DB().supabase_connection()
    resp = supa.table("roles").select('id_type_user').eq("id_user", uuid).execute()
    print(resp.data)
    return resp.data[0]['id_type_user']

def user_exist(uuid: UUID):
    supa = DB().supabase_connection()
    resp = supa.table("profiles").select('id').eq('id', uuid).execute()
    if resp.data[0]['id'] == uuid:
        return True
    return False
