import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://qa.makerble.com/users/sign_up")

## Creating a account
driver.find_element(By.ID,"user_first_name").send_keys("Sarala")
driver.find_element(By.ID,"user_last_name").send_keys("Gunasekaran")
driver.find_element(By.ID,"user_email").send_keys("142cd@gmail.com")
driver.find_element(By.ID,"user_email_confirmation").send_keys("142cd@gmail.com")
driver.find_element(By.ID,"user_password").send_keys("Ab@12345")
driver.find_element(By.ID,"user_password_confirmation").send_keys("Ab@12345")
time.sleep(5)
driver.find_element(By.ID,"user_avatar").send_keys("C:\\Users\\saral\\OneDrive\\Desktop\\IMG.jpg")
time.sleep(5)
iframe=driver.find_element(By.XPATH,"//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH,'//span//div[@class="recaptcha-checkbox-border"]').click()
time.sleep(5)
driver.switch_to.default_content()
time.sleep(10)
time.sleep(5)
driver.find_element(By.ID,"signUpBtn").click()
time.sleep(5)
driver.find_element(By.ID,"termsConditionsCheckbox").click()
time.sleep(5)
driver.find_element(By.ID,"two-fa-enable-checkbox").click()
time.sleep(2)
driver.find_element(By.ID,"phone").send_keys("8585858585")
time.sleep(3)
driver.find_element(By.XPATH,'//input[ @value="Save"]').click()
alert = Alert(driver)
time.sleep(3)
alert.accept()



##Organisation
driver.find_element(By.LINK_TEXT,"Home").click()
time.sleep(5)
driver.find_element(By.XPATH,'//select/option[@value="organisation"]').click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Create your first organisation").click()
driver.find_element(By.ID,"charity_name").send_keys("Hostel of Care")
sel=Select(driver.find_element(By.ID,"charity_country_id"))
sel.select_by_value("82")
sel1=Select(driver.find_element(By.ID,"charity_charity_type_id"))
sel1.select_by_value("5")
driver.find_element(By.ID,"charity_terms_checkbox").click()
driver.find_element(By.XPATH,"//input[@value='Make New Organisation >']").click()
time.sleep(7)
alert.accept()


### creation of project

driver.find_element(By.LINK_TEXT,"Create a programme (project)").click()
#sel2=Select(driver.find_element(By.NAME,"project[project_category_id"))
#time.sleep(2)
#sel2.select_by_visible_text("Project")
time.sleep(5)
driver.find_element(By.XPATH,'//div/input[@id="project_headline"]').send_keys("Counselling")
driver.find_element(By.ID,"s2id_project_reporter_ids2").click()
time.sleep(5)
driver.find_element(By.XPATH,'//div[contains(text(),"Aadil Salam")]').click()
#sel3=Select(driver.find_element(By.ID,"project_reporter_ids2"))
#sel3.select_by_value("846")
#time.sleep(5)
#sel3.select_by_value("808")
driver.find_element(By.ID,"s2id_project_observer_ids2").click()
time.sleep(5)
driver.find_element(By.XPATH,'//div[contains(text(),"A RAVINDAR")]').click()
#sel4=Select(driver.find_element(By.ID,"project_observer_ids2"))
#sel4.select_by_value("753")
#sel4.select_by_value("718")
driver.find_element(By.XPATH,'//div//button[contains(text(),"Save Changes")]').click()


##Contact forms

driver.find_element(By.XPATH,'//div[@id="s2id_contact-forms-select3"]').click()
driver.find_element(By.XPATH,"//div[contains(text(),'Participant')]").click()
time.sleep(3)
driver.find_element(By.XPATH,'//td[contains(text(),"Organisation Admin")]/following-sibling::td[1]/input[@type="checkbox"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//td[contains(text(),"Project Managers")]/following-sibling::td[2]/input[@type="checkbox"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//td[contains(text(),"Project Observers")]/following-sibling::td[3]/input[@type="checkbox"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//td[contains(text(),"Reporters")]/following-sibling::td[4]/input[@type="checkbox"]').click()
time.sleep(3)
sel6=Select(driver.find_element(By.XPATH,'//div//select[@id="enrolled-state-contact-form-select"]'))
sel6.select_by_value("856")
driver.find_element(By.ID,"enable-enrolled-state-baseline-survey-checkbox").click()
driver.find_element(By.ID,"s2id_enrolled-state-baseline-surveys-select2").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Counselling - Update')]").click()
driver.find_element(By.ID,"enable-waiting-list-state-checkbox").click()
driver.find_element(By.ID,"enable-waiting-list-state-contact-form-checkbox").click()
driver.find_element(By.ID,"enable-waiting-list-state-baseline-survey-checkbox").click()
driver.find_element(By.ID,"enable-declined-state-checkbox").click()
driver.find_element(By.ID,"enable-declined-state-contact-form-checkbox").click()
sel7=Select(driver.find_element(By.ID,"declined-state-contact-form-select"))
sel7.select_by_value("880")
driver.find_element(By.ID,"enable-declined-state-baseline-survey-checkbox").click()
driver.find_element(By.ID,"s2id_declined-state-baseline-surveys-select2").click()
driver.find_element(By.ID,"enable-alumni-state-checkbox").click()
driver.find_element(By.ID,"enable-alumni-state-contact-form-checkbox").click()
sel8=Select(driver.find_element(By.ID,"alumni-state-contact-form-select"))
sel8.select_by_value("880")
driver.find_element(By.ID,"enable-alumni-state-baseline-survey-checkbox").click()
driver.find_element(By.ID,"s2id_alumni-state-baseline-surveys-select2").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Counselling - Update)]").click()
driver.find_element(By.ID,"event-enable-checkbox").click()
driver.find_element(By.ID,"s2id_event-creators-select2").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Aadil Salam)]").click()
driver.find_element(By.ID,"s2id_case-creators-select2").click()
driver.find_element(By.ID,"case-enable-checkbox").click()
driver.find_element(By.ID,"launch_create_page").click()
driver.find_element(By.ID,"case-story-category-checkbox").click()
driver.find_element(By.ID,"project_hide_anonymous_participants_section").click()
sel7=Select(driver.find_element(By.ID,"story_privacy_select"))
sel7.select_by_visible_text("Only project colleagues")
driver.find_element(By.ID,"project_prevent_project_reporters_changing_story_privacy").click()
driver.find_element(By.ID,"project_prevent_project_reporters_changing_story_privacy").click()
driver.find_element(By.ID,"project_automate_following_between_beneficiary").click()
driver.find_element(By.ID,"project_enable_financial_value").click()
driver.find_element(By.ID,"project_is_creation_of_timesheets_required").click()
driver.find_element(By.ID,"preferences-save-btn").click()


##Add Patients

driver.find_element(By.XPATH,"//span[contains(text(),'Contacts')]").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Make A Contact')]").click()
driver.find_element(By.ID,"select2-project_select-container").click()
driver.find_element(By.XPATH,"//span[contains(text(),'Counselling')]").click()
sel8=Select(driver.find_element(By.ID,"beneficiary_category_select"))
sel8.select_by_value("880")
driver.find_element(By.ID,"beneficiary_submit_and_add_btn").click()
driver.find_element(By.LINK_TEXT,"Customize this form?").click()
driver.find_element(By.LINK_TEXT,"+ Create a field or question").click()
driver.find_element(By.NAME,"custom_field[field_name]").send_keys("Reason For Joining")
driver.find_element(By.XPATH,"//button[contains(text(),'Save')]").click()
driver.find_element(By.NAME,"custom_field[current_field_name]").send_keys("Please Tell Us Why You Are Joining This Programmee")
driver.find_element(By.ID,"save_btn").click()
driver.find_element(By.LINK_TEXT,"Edit").click()

##Add the Mental Health Assessment

driver.find_element(By.LINK_TEXT,"Surveys").click()
driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("Mental Health Assessment")
driver.find_element(By.LINK_TEXT,"+ Add to Project").click()
driver.find_element(By.ID,"project_ids_").click()
driver.find_element(By.XPATH,"//a[contains(text(),'Save')]").click()

##Create a Referral Form

driver.find_element(By.XPATH,"//span[contains(text(),'Contacts')]").click()
driver.find_element(By.LINK_TEXT,"More Options ▾").click()
driver.find_element(By.LINK_TEXT,"Design your forms").click()
driver.find_element(By.LINK_TEXT,"New Contact Form").click()
driver.find_element(By.ID,"beneficiary_category_name").send_keys("Potential Patients")
driver.find_element(By.ID,"save_btn").click()













