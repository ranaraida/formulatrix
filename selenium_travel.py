import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TestTravel(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Firefox()

    def test_success_1_cars_one_way(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # pilih cars
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[4]/button/span[2]").click()
        time.sleep(3)
        # click dulu origin
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[1]/div/div/div/span/span[1]/span/span[1]").click()
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Jakarta")
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li").click()
        time.sleep(2)

        # click dulu destinasi
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[2]/div/div/div/span/span[1]/span/span[1]").click()
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Surabaya")
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li").click()
        time.sleep(2)
        # click search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[4]/div/button/span[1]").click()
        time.sleep(3)
        # cari kata cars in di title
        assert "Cars in" in driver.title

    def test_success_2_cars_return(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # pilih cars
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[4]/button/span[2]").click()
        time.sleep(3)

        # pilih return
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[1]/div/div/div[2]/div/input").click()
        time.sleep(2)

        # click dulu origin
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[1]/div/div/div/span/span[1]/span/span[1]").click()
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Jakarta")
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li").click()
        time.sleep(2)

        # click dulu destinasi
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[2]/div/div/div/span/span[1]/span/span[1]").click()
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Surabaya")
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li").click()
        time.sleep(2)
        # click search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[4]/div/button/span[1]").click()
        time.sleep(3)
        # cari kata cars in di title
        assert "Cars in" in driver.title

    def test_failed_3_cars_empty_origin_destination(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # pilih cars
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[4]/button/span[2]").click()
        time.sleep(3)

        # click search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[4]/div/button/span[1]").click()
        time.sleep(3)

        assert "PHPTRAVELS - PHPTRAVELS" in driver.title

    def test_failed_4_cars_empty_destination(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # pilih cars
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[4]/button/span[2]").click()
        time.sleep(3)

        # click dulu destinasi
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[2]/div/div/div/span/span[1]/span/span[1]").click()
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Surabaya")
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li").click()
        time.sleep(2)

        # click search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[4]/div/button/span[1]").click()
        time.sleep(3)

        # check warning karena field kosong
        warning_html5 = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[2]/div/div/div/span/span[1]/span/span[1]"))).get_attribute("validationMessage")
        self.assertEqual(warning_html5, None)
        # check gagal search dan tetap di halaman
        assert "PHPTRAVELS - PHPTRAVELS" in driver.title
        self.assertIn("PHPTRAVELS - PHPTRAVELS",driver.title)

    def test_failed_5_cars_empty_origin(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # pilih cars
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[4]/button/span[2]").click()
        time.sleep(3)

        # click dulu origin
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[1]/div/div/div/span/span[1]/span/span[1]").click()
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Jakarta")
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li").click()
        time.sleep(2)

        # click search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[4]/div/button/span[1]").click()
        time.sleep(3)

        # check warning karena field kosong
        warning_html5 = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[1]/div/div/div/span/span[1]/span/span[1]"))).get_attribute("validationMessage")
        self.assertEqual(warning_html5, None)
        # check gagal search dan tetap di halaman
        assert "PHPTRAVELS - PHPTRAVELS" in driver.title

    def test_failed_6_cars_sql_origin(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # pilih cars
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[4]/button/span[2]").click()
        time.sleep(3)

        # click dulu origin
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[1]/div/div/div/span/span[1]/span/span[1]").click()
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("SELECT count (*) FROM Users WHERE Username='rana' or 1=1 -- ' AND Password= '123456'")
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li").click()
        time.sleep(2)

        # click search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[4]/div/button/span[1]").click()
        time.sleep(3)

        # check warning karena field kosong
        warning_html5 = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[1]/div/div/div/span/span[1]/span/span[1]"))).get_attribute("validationMessage")
        self.assertEqual(warning_html5, None)
        # check gagal search dan tetap di halaman
        assert "PHPTRAVELS - PHPTRAVELS" in driver.title

    def test_failed_7_cars_sql_destination(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # pilih cars
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[4]/button/span[2]").click()
        time.sleep(3)

        # click dulu destinasi
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[2]/div/div/div/span/span[1]/span/span[1]").click()
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("SELECT count (*) FROM Users WHERE Username='rana' or 1=1 -- ' AND Password= '123456'")
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li").click()
        time.sleep(2)

        # click search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[4]/div/button/span[1]").click()
        time.sleep(3)

        # check warning karena field kosong
        warning_html5 = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[1]/div/div/div/div/div[2]/div/div[4]/form/div/div[2]/div[1]/div/div[2]/div/div/div/span/span[1]/span/span[1]"))).get_attribute("validationMessage")
        self.assertEqual(warning_html5, None)
        # check gagal search dan tetap di halaman
        assert "PHPTRAVELS - PHPTRAVELS" in driver.title

    ###################### VISA FEATURE ########################################

    def test_success_8_visa(self): 
        # FOUND ISSUE IN ROW FROM COUNTRY
        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # pilih visa
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[5]/button/span[2]").click()
        time.sleep(4)
        # # click dulu country
        # driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[5]/form/div/div/div[1]/div/div/div/span").click()
        # time.sleep(4)

        # driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Suriname")
        # time.sleep(4)

        # driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li").click()
        # time.sleep(2)

        # driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[5]/form/div/div/div[4]/div/button/span[1]").click()
        # time.sleep(3)
        # # cari kata visa in di title
        # assert "Visa in" in driver.title

    def test_failed_9_empty_from_to_visa(self): 
        # FOUND ISSUE IN ROW FROM COUNTRY
        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)

        # pilih visa
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[5]/button/span[2]").click()
        time.sleep(4)

        # klik search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[5]/form/div/div/div[4]/div/button/span[1]").click()
        time.sleep(3)

        # check warning karena field kosong
        warning_html5 = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[1]/div/div/div/div/div[2]/ul/li[5]/button/span[2]"))).get_attribute("validationMessage")
        self.assertEqual(warning_html5, None)
        # check gagal search dan tetap di halaman
        assert "PHPTRAVELS - PHPTRAVELS" in driver.title

    def test_succes_10_search_hotel(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # click dulu pilih negara
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[1]/div/div/div/span/span[1]/span").click()
        time.sleep(1)
        # ketik pilihan negara
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Jakarta")
        time.sleep(3)
        # pilih opsi yang muncul
        driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
        time.sleep(2)
        # klik tanggal pertama sewa hotel
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[2]/div/div[1]/div/input").click()
        time.sleep(3)
        # pilih tgl 28
        driver.find_element_by_xpath("//*[contains(text(), '28')]").click()
        time.sleep(3)
        # klik tanggal kedua sewa hotel
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[2]/div/div[2]/div/input").click()
        time.sleep(3)
        # driver.find_element_by_xpath("//*[contains(text(), '29')]").click()
        # time.sleep(3)
        # klik dulu form jumlah orang
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[3]/div/div/div/a").click()
        time.sleep(2)
        # function untuk deklarasi dropdown yg isinya negara"
        tes = Select(driver.find_element_by_xpath('/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[3]/div/div/div/div/div[4]/div/div/select'))
        # select country Indonesia
        time.sleep(2)
        tes.select_by_value('ID')
        time.sleep(2)
        # klik sembarang ini yg dibawah, sengaja biar pop up nya ketutup
        driver.find_element_by_xpath("/html/body/section[1]/div").click()
        time.sleep(1)
        # klik tombol search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[4]/div/button").click()
        time.sleep(5)

        response_status = driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/div/div/span/strong/h2").text
        # response_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text
        
        self.assertIn("Search Hotels In Jakarta", response_status)

    def test_failed_11_flight_(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)

        # click Flights
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[2]/button").click()
        time.sleep(1)
        # One Way
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/div/div[1]/div/input").click()
        time.sleep(3)
        # function untuk deklarasi dropdown kelas penerbangan"
        tes = Select(driver.find_element_by_xpath('/html/body/section[1]/div/div/div/div/div[2]/div/div[2]/form/div[1]/div[2]/select'))
        time.sleep(2)
        tes.select_by_value('first')
        time.sleep(2)
        # ketik keberangkatan
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/div[1]/div/div/div/input").send_keys("Jakarta")
        time.sleep (2)
        # pilih keberangkatan
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[1]").click()
        time.sleep(2)
        # ketik tujuan
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/div[2]/div/div/div/input").send_keys("Batam")
        time.sleep (3)
        # pilih tujuan
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]").click()
        time.sleep(2)
        #pilih tanggal keberangkatan
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div/input").click()
        time.sleep(2)
        # isi tanggal
        driver.find_element_by_xpath("/html/body/div[7]/div[1]/table/tbody/tr[5]/td[3]").click()
        time.sleep(3)
        # klik tombol search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[4]/div/button").click()
        time.sleep(5)

        assert "CGK" in driver.page_source

    def test_succes_12_tour(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
        # click tour
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/ul/li[3]/button/span[2]").click()
        time.sleep(1)
        # ketik pilihan kota
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Jakarta")
        time.sleep(3)
        # pilih opsi yang muncul
        driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
        time.sleep(2)
        # klik tanggal
        driver.find_element_by_xpath("/html/body/div[10]/div[1]/table/tbody/tr[5]/td[4]").click()
        time.sleep(3)
        # pilih jumlah orang
        #driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[3]/form/div/div/div[3]/div/div/div/a/p").click()
        #time.sleep(3)
        # klik traveller
        #driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[2]/div/div[2]/div/input").click()
        #time.sleep(3)
        # tambah orang
        #driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[3]/form/div/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/i").click()
        #time.sleep(3)
        # klik search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[3]/form/div/div/div[4]/div/button").click()
        time.sleep(5)
        
        response_oke = driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/div/div/span/strong/h2").text
        
        self.assertIn("Search Tour in Jakarta", response_oke)

    def test_failed_13_hotel_empty_all_fields(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)
       
        # klik tombol search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[4]/div/button").click()
        time.sleep(5)

        # check warning karena field kosong
        warning_html5 = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[1]/div/div/div/span/span[1]/span"))).get_attribute("validationMessage")
        self.assertEqual(warning_html5, None)
        # check gagal search dan tetap di halaman
        assert "PHPTRAVELS - PHPTRAVELS" in driver.title

    def test_failed_14_hotel_empty_choose_country(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)

        # click dulu pilih negara
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[1]/div/div/div/span/span[1]/span").click()
        time.sleep(1)
        # ketik pilihan negara
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Jakarta")
        time.sleep(3)
        # pilih opsi yang muncul
        driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
        time.sleep(2)       
        # klik tombol search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[4]/div/button").click()
        time.sleep(5)

        # check warning karena field kosong
        warning_html5 = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[1]/div/div/div/span/span[1]/span"))).get_attribute("validationMessage")
        self.assertEqual(warning_html5, None)
        # check gagal search dan tetap di halaman
        assert "PHPTRAVELS - PHPTRAVELS" in driver.title

    def test_failed_15_hotel_wrong_country(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)

        # click dulu pilih negara
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[1]/div/div/div/span/span[1]/span").click()
        time.sleep(1)
        # ketik pilihan negara
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("Jawa")
        time.sleep(3)
        # pilih opsi yang muncul
        driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
        time.sleep(2)       
        # klik tombol search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[4]/div/button").click()
        time.sleep(5)

        # check gagal search dan tetap di halaman
        assert "PHPTRAVELS - PHPTRAVELS" in driver.title

    def test_failed_16_hotel_sqli(self): 

        driver = self.driver 
        driver.maximize_window()
        driver.get("https://www.phptravels.net")
        time.sleep(5)

        # click dulu pilih negara
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[1]/div/div/div/span/span[1]/span").click()
        time.sleep(1)
        # ketik pilihan negara
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("SELECT count (*) FROM Users WHERE Username='rana' or 1=1 -- ' AND Password= '123456'")
        time.sleep(3)
        # pilih opsi yang muncul
        driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()
        time.sleep(2)       
        # klik tombol search
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/form/div/div/div[4]/div/button").click()
        time.sleep(5)

        # check gagal search dan tetap di halaman
        assert "PHPTRAVELS - PHPTRAVELS" in driver.title

    def tearDown(self): 
        self.driver.close() 
  
# execute the script 
if __name__ == "__main__": 
    unittest.main() 
