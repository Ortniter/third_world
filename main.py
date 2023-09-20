from apps.folder_crawler.services import FolderCrawler
from apps.telegram import bot

if __name__ == '__main__':
    crawler = FolderCrawler()
    crawler.scan()
    bot.start()
