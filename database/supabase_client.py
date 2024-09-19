import os
from supabase import create_client, Client # type: ignore
from dotenv import load_dotenv
load_dotenv()
url: str = os.getenv('LINK_SUPABASE')
key: str = os.getenv('KEY_SUPABASE')
supabase: Client = create_client(url, key)
