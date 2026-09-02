from console_logger import log
from page_downloader import download_page
from parsers.hhru import parse_hh_vacancies
def search_jobs(config, proxy_list):
    jobs = []
    pages = config["scraper"]["pages"]
    for url in pages:
        html = download_page(
            url=url,
            config=config,
            proxy_list=proxy_list
        )
        if html is None:
            log(f"Skipping page: {url}")
            continue
        page_jobs = parse_hh_vacancies(html)
        log(f"Found {len(page_jobs)} vacancies on {url}")
        jobs.extend(page_jobs)
    return jobs
