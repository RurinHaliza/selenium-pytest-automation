from pages.materi_page import MateriPage


class TestMateriAuditory:

    def test_open_auditory_material(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/auditory/1")

        page = MateriPage(driver)
        page.auditory_page_loaded()
        page.sidebar_visible()

        assert "materi/auditory" in driver.current_url

    def test_auditory_has_audio_player(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/auditory/1")

        page = MateriPage(driver)
        page.auditory_page_loaded()

        audio = page.driver.find_element(*page.AUDIO_PLAYER)
        assert audio.is_displayed()
        assert audio.get_attribute("controls") is not None

    def test_navigate_auditory_to_visual(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/auditory/1")

        page = MateriPage(driver)
        page.go_to_visual()
        page.visual_page_loaded()

        assert "materi/visual" in driver.current_url
