import pytest
from pages.materi_page import MateriPage


class TestMateriVisual:

    def test_open_visual_material(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/visual/1")

        page = MateriPage(driver)
        page.visual_page_loaded()
        page.sidebar_visible()

        assert "materi/visual" in driver.current_url

    def test_visual_has_image(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/visual/1")

        page = MateriPage(driver)
        page.visual_page_loaded()

        assert page.driver.find_element(*page.VISUAL_IMAGE).is_displayed()

    def test_navigate_visual_to_auditory(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/visual/1")

        page = MateriPage(driver)
        page.go_to_auditory()
        page.auditory_page_loaded()

        assert "materi/auditory" in driver.current_url

    #@pytest.mark.xfail(reason="Belum ada validasi sebelum meninggalkan halaman materi")
    def test_navigation_requires_confirmation(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/visual/1")

        page = MateriPage(driver)
        page.go_to_auditory()

        # Expected behavior (yang benar secara requirement)
        assert "materi/visual" in driver.current_url
