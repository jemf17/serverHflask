from dotenv import load_dotenv
import os
from database.db_connection import DB
from fastapi import HTTPException
from botocore.exceptions import BotoCoreError, ClientError
load_dotenv()



def upload_image_to_s3(image, path: str):
    try:
        s3_client = DB().s3_connection()
        load_dotenv()
        file_location = f"{path}{image.filename}"
        s3_client.upload_fileobj(image.file, os.getenv('S3_BUCKET_NAME'), file_location)
        return {"path": f"https://{os.getenv('S3_BUCKET_NAME')}.s3.{os.getenv('S3_REGION_NAME')}.amazonaws.com/{file_location}"}
    except (BotoCoreError, ClientError) as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_img_to_s3(image, path:str , old_filename: str):
    try:
        s3_client = DB().s3_connection()
        load_dotenv()
        old_file_location = f"{path}{old_filename}"
        # Eliminar la imagen anterior
        s3_client.delete_object(Bucket=os.getenv('S3_BUCKET_NAME'), Key=old_file_location)
        # Subir la nueva imagen
        new_file_location = f"{path}{image.filename}"
        s3_client.upload_fileobj(image.file, os.getenv('S3_BUCKET_NAME'), new_file_location)
        return {"new_path": f"https://{os.getenv('S3_BUCKET_NAME')}.s3.{os.getenv('S3_REGION_NAME')}.amazonaws.com/{new_file_location}"}
    except (BotoCoreError, ClientError) as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_img_from_s3(path: str):
    try:
        s3_client = DB().s3_connection()
        load_dotenv()
        objects = s3_client.list_objects_v2(Bucket=os.getenv('S3_BUCKET_NAME'), Prefix=path)
        if "Contents" in objects:
            keys_to_delete = [{"Key": obj["Key"]} for obj in objects["Contents"]]
            s3_client.delete_objects(
                Bucket=os.getenv('S3_BUCKET_NAME'),
                Delete={"Objects": keys_to_delete},
            )
        return {"detail": f"Directory '{path}' deleted successfully."}
    except (BotoCoreError, ClientError) as e:
        raise HTTPException(status_code=500, detail=str(e))