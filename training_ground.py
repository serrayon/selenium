class TrainingGroundPage(BasePage):
    url = 'https://techstepacademy.com/training-groung/'

    @property
    def button1(self):
        locator = (By.ID, 'bi')
        return BaseElement(
            driver = sefl.driver,
            by = locator[0]
            value = locator[1]
        )