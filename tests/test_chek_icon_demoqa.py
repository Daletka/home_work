from pages.demoqa import DemoQa
import time


def test_check_icon(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    demo_qa_page.icon.clck()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()