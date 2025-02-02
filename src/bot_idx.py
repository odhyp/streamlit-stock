import time

from playwright.sync_api import sync_playwright


class IDXBot:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
        self.playwright = None

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=False, args=["--start-maximized"]
        )
        self.context = self.browser.new_context(no_viewport=True)
        self.page = self.context.new_page()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def download_daftar_saham(self, file_name: str):
        """
        Download Daftar Saham (excel)
        https://www.idx.co.id/id/data-pasar/data-saham/daftar-saham/

        TODO: url var is hard-coded
        TODO: make a universal timeout values (e.g. short, long, etc)
        """
        url = "https://www.idx.co.id/id/data-pasar/data-saham/daftar-saham/"
        self.page.goto(url, timeout=30_000)

        with self.page.expect_download(timeout=30_000) as download_info:
            btn_download = self.page.locator('button:has-text("Unduh")')
            btn_download.wait_for()
            btn_download.click()

        download_file = download_info.value
        download_file.save_as(file_name)
