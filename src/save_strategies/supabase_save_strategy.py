# from io import BytesIO
from tempfile import NamedTemporaryFile
from typing import Any
from storage3 import create_client, SyncStorageClient # pylint: disable=import-error
from .save_strategy import SaveStrategy

class SupabaseSaveStrategy(SaveStrategy):
    client: SyncStorageClient
    bucket: str

    def __init__(self, supabase_id: str, token: str, bucket):
        url = f"https://{supabase_id}.supabase.co/storage/v1"
        headers = {
            "apiKey": token,
            "Authorization": f"Bearer {token}"
        }
        self.client = create_client(url=url, headers=headers, is_async=False)
        self.bucket = bucket

    def save(self, name: str, plot: Any):
        temp_file = NamedTemporaryFile(suffix='.png')
        plot.savefig(temp_file.name, format='png')
        with open(temp_file.name, 'rb') as file:
            files = self.client.from_(self.bucket).list()
            file_exists = next(filter(lambda x: x['name'] == name, files), None) is not None
            action = 'update' if file_exists else 'upload'
            headers = { "content-type": "image/png" }
            getattr(self.client.from_(self.bucket), action)(name, file, headers)
            temp_file.close()
