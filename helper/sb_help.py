from database.sb_conection import supabase
"""
def verify_exist_user(name):
    resp = supabase.table("usuarios").select("nombre").eq("nombre", name).execute()
    print("esta es la respuesta:", resp, len(resp.data))
    if len(resp.data) == 1:
        return True
    return False

def get_name_user_sb_by_id(id):
    resp = supabase.table("usuarios").select("nombre").eq("id", id).execute()
    #print("data:", resp.data)
    return resp.data[0]["nombre"]
"""

def get_role_user(uuid):
    resp = supabase.table("roles").select('id_type_user').eq("id_user", uuid).execute()
    print(resp.data)
    return resp.data[0]['id_type_user']