from database.supabase_client import supabase
def verify_exist_user(name):
    resp = supabase.table("usuarios").select("nombre").eq("nombre", name).execute()
    print("esta es la respuesta:", resp)
    if resp.count != 0:
        return True
    return False
