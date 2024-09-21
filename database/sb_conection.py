import os
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv('LINK_SUPABASE')
key = os.getenv('KEY_SUPABASE')
supabase = create_client(url, key)
