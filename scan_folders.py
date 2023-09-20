import logging

from apps.folder_crawler.services import FolderCrawler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Starting folder crawler')
    crawler = FolderCrawler()
    crawler.scan()
    logger.info('Folder crawler finished')
