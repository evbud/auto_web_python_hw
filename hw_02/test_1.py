import time

import yaml
from module import Site
from os import getcwd

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata['address'])

# css_selector = 'span.mdc-text-field__ripple'
# print(site.get_element_property('css', css_selector, 'height'))
#
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property('xpath', xpath, 'color'))


def test_step1(x_selector_1, x_selector_2, btn_login, x_selector_3, expected_result_1):
    input1 = site.find_element('xpath', x_selector_1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector_2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_login)
    btn.click()
    error_label = site.find_element('xpath', x_selector_3)
    result = error_label.text
    assert result == expected_result_1, 'test1 failed'


def test_step2(x_selector_1, x_selector_2, btn_login, expected_result_1, x_selector_4, expected_result_2):
    input1 = site.find_element('xpath', x_selector_1)
    input1.clear()
    input1.send_keys(testdata['username'])
    input2 = site.find_element('xpath', x_selector_2)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', btn_login)
    btn.click()
    link1 = site.find_element('xpath', x_selector_4)
    result = link1.text
    assert result == expected_result_2, 'test2 failed'


def test_step3(btn_create, selector_title, selector_description, selector_content, selector_img, btn_save,
               c_selector_title):
    btn_cr = site.find_element('id', btn_create)
    time.sleep(1)
    btn_cr.click()
    input_title = site.find_element('xpath', selector_title)
    input_title.click()
    input_title.send_keys(testdata['test_title'])
    input_description = site.find_element('xpath', selector_description)
    input_description.click()
    input_description.send_keys(testdata['test_description'])
    input_content = site.find_element('xpath', selector_content)
    input_content.click()
    input_content.send_keys(testdata['test_content'])
    upload_img = site.find_element('xpath', selector_img)
    upload_img.send_keys(getcwd()+'/test_img.jpeg')
    btn_sv = site.find_element('xpath', btn_save)
    btn_sv.click()
    time.sleep(2)
    c_selector_1 = site.find_element('css', c_selector_title)
    result = c_selector_1.text
    site.close()
    assert result == testdata['test_title'], 'test3 failed'
