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

    def download_daftar_saham(self, output_name: str):
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
        download_file.save_as(output_name)

    def download_ringkasan_saham(self, output_dir: str, date_range: list):
        """
        Download Ringkasan Saham (excel)
        https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham/

        TODO: url var is hard-coded
        TODO: make a universal timeout values (e.g. short, long, etc)
        """
        url = (
            "https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham/"
        )
        self.page.goto(url, timeout=30_000)

        for date in date_range:
            # Date form
            form_date = self.page.locator("input[name='date']")
            form_date.wait_for()
            form_date.click()
            form_date.clear()
            form_date.type(date)
            form_date.press("Enter")

            # Data table
            stock_table = self.page.locator("#vgt-table")
            stock_table.wait_for()

            # Download button
            btn_download = self.page.locator('button:has-text("Unduh")')

            if not btn_download.is_disabled():
                with self.page.expect_download(timeout=30_000) as download_info:
                    btn_download.wait_for()
                    btn_download.click()

                download_file = download_info.value
                download_file.save_as(f"{output_dir}/{date}.xlsx")
