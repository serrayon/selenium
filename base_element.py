from selenium.webdriver.suppor.wait import WebDriverWait
from selenium.webdriver.suppor import expected_conditions as EC

class BaseElement(object):
    def __init__(self,driver,value,by):
        self.driver = driver
        self.value = value 
        self.by = by 
        self.locator = (self.by,self.value)

        self.we_element = None 
        self.find()
    
    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibilitiy_of_element_located(locator=self.locator)
        )
        self.web_element = element 
        return None
    
    def input_text(self, txt):
        self.wewb_element_send_keys(txt)
        return None 
    
    def click(self):
        element = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(locator= self.locator)
        )