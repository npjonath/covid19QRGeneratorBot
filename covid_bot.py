from selenium import webdriver
import json
import time

print('''
Covid French Certificate Generator - MIT License - Copyright (c) 2020 NP

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''')

class CovidFrenchCertificateBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def generate(self):
        with open('config.json') as f:
            data = json.load(f)

        self.driver.get('https://media.interieur.gouv.fr/deplacement-covid-19/')
        
        firstname = self.driver.find_element_by_xpath('//*[@id="field-firstname"]')
        firstname.send_keys(data['firstname'])
        
        lastname = self.driver.find_element_by_xpath('//*[@id="field-lastname"]')
        lastname.send_keys(data['lastname'])
        
        birthday = self.driver.find_element_by_xpath('//*[@id="field-birthday"]')
        birthday.send_keys(data['birthDay'])
        
        birthplace = self.driver.find_element_by_xpath('//*[@id="field-lieunaissance"]')
        birthplace.send_keys(data['birthPlace'])
        
        address = self.driver.find_element_by_xpath('//*[@id="field-address"]')
        address.send_keys(data['address'])

        town = self.driver.find_element_by_xpath('//*[@id="field-town"]')
        town.send_keys(data['town'])
        
        zipCode = self.driver.find_element_by_xpath('//*[@id="field-zipcode"]')
        zipCode.send_keys(data['postCode'])

        if data['workCheckBox']:
            workCheckBox = self.driver.find_element_by_xpath('//*[@id="checkbox-travail"]')
            workCheckBox.click();

        if data['shoppingCheckBox']:
            shoppingCheckBox = self.driver.find_element_by_xpath('//*[@id="checkbox-courses"]')
            shoppingCheckBox.click();

        if data['healthCheckBox']:
            healthCheckBox = self.driver.find_element_by_xpath('//*[@id="checkbox-sante"]')
            healthCheckBox.click();

        if data['famillyCheckBox']:
            famillyCheckBox = self.driver.find_element_by_xpath('//*[@id="checkbox-famille"]')
            famillyCheckBox.click();

        if data['sportCheckBox']:
            sportCheckBox = self.driver.find_element_by_xpath('//*[@id="checkbox-sport"]')
            sportCheckBox.click();

        if data['legalCheckBox']:
            legalCheckBox = self.driver.find_element_by_xpath('//*[@id="checkbox-judiciaire"]')
            legalCheckBox.click();

        if data['missionsCheckBox']:
            missionsCheckBox = self.driver.find_element_by_xpath('//*[@id="checkbox-missions"]')
            missionsCheckBox.click();

        confirmBtn = self.driver.find_element_by_xpath('//*[@id="form-profile"]/p/button')
        confirmBtn.click()
        time.sleep(2.4)
        self.driver.quit()

bot = CovidFrenchCertificateBot()
bot.generate()