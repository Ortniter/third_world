import os
from collections import defaultdict

from sqlalchemy.orm import Session

from config import settings as app_settings
from config.db import SessionLocal
from apps.users import models as user_models
from apps.telegram import bot as telegram_bot
from apps.folder_crawler.models import Folder, File


class Notifier:

    def __init__(self, new_files: dict):
        self.db: Session = SessionLocal()
        self.new_files: dict = new_files

    def __del__(self):
        self.db.close()

    def notify(self):
        users = self.db.query(user_models.User).all()
        for user in users:
            telegram_bot.send_message(
                chat_id=user.telegram_id,
                text=self.prepare_message(user)
            )

    def prepare_message(self, user: user_models.User) -> str:
        message = f'Hi, {user.first_name}!\n'
        for folder_name, files in self.new_files.items():
            message += f'New files in {folder_name}:\n'
            for file in files:
                message += f'{file.name}\n'
            message += '\n'
        return message


class FolderCrawler:

    def __init__(self, folder_path: str = app_settings.SHARED_FOLDER_PATH):
        self.root: str = folder_path
        self.db: Session = SessionLocal()
        self.new_files: dict = defaultdict(list)

    def __del__(self):
        self.db.close()

    @property
    def dirs(self) -> list:
        return [
            folder for folder in os.listdir(self.root)
            if os.path.isdir(os.path.join(self.root, folder))
        ]

    def scan(self, send_notification: bool = True):
        for folder in self.scan_folders():
            self.scan_files(folder)

        if self.new_files and send_notification:
            notifier = Notifier(self.new_files)
            notifier.notify()

    def scan_folders(self) -> iter:
        for dir_name in self.dirs:
            folder_path = os.path.join(self.root, dir_name)
            folder = self.db.query(Folder).filter(Folder.path == folder_path).first()
            if not folder:
                folder = Folder(
                    name=dir_name,
                    path=folder_path
                )
                self.db.add(folder)
                self.db.commit()
                self.db.refresh(folder)
            yield folder

    def scan_files(self, folder: Folder):
        for file_name in os.listdir(folder.path):
            file_path = os.path.join(folder.path, file_name)
            file = self.db.query(File).filter(File.path == file_path).first()
            if not file:
                file = File(
                    name=str(file_name),
                    path=str(file_path),
                    folder_id=folder.id
                )
                self.db.add(file)
                self.db.commit()
                self.db.refresh(file)
                self.new_files[folder.name].append(file)
