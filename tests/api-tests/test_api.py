import pytest
import requests

class TestBibleApi:

    url = "https://bible-api.com/"

    @pytest.mark.parametrize("path,expected_content",
                             [("gen 1:1", b'{"reference":"Genesis 1:1","verses":[{"book_id":"GEN","book_name":"Genesis","chapter":1,"verse":1,"text":"In the beginning, God created the heavens and the earth.\\n"}],"text":"In the beginning, God created the heavens and the earth.\\n","translation_id":"web","translation_name":"World English Bible","translation_note":"Public Domain"}'),
                              ("genesis 1:1", b'{"reference":"Genesis 1:1","verses":[{"book_id":"GEN","book_name":"Genesis","chapter":1,"verse":1,"text":"In the beginning, God created the heavens and the earth.\\n"}],"text":"In the beginning, God created the heavens and the earth.\\n","translation_id":"web","translation_name":"World English Bible","translation_note":"Public Domain"}'),
                              ("gen 1:1?translation=darby", b'{"reference":"Genesis 1:1","verses":[{"book_id":"GEN","book_name":"Genesis","chapter":1,"verse":1,"text":"In the beginning God created the heavens and the earth."}],"text":"In the beginning God created the heavens and the earth.","translation_id":"darby","translation_name":"Darby Bible","translation_note":"Public Domain"}'),
                              ])
    def test_get_verse(self, path, expected_content):
        """ Makes a request and validates content of responses """
        response = requests.get(self.url + path)
        assert response.content == expected_content, f"Expected response content: {expected_content}, Received response content: {response.content}"

    @pytest.mark.parametrize("path,expected", [("gen 1:2-4,6", 4),
                                               ("gen 2", 25)])
    def test_get_chapter(self, path, expected):
        """ Makes a request and validates number of returned verses """
        response = requests.get(self.url + path)
        json = response.json()
        assert len(json["verses"]) == expected

    @pytest.mark.parametrize("path,expected_status_code",[("gen 404", 404),
                                                          ("asdf", 404)])
    def test_invalid_request(self, path, expected_status_code):
        """ Validates an error for an invalid path """
        response = requests.get(self.url + path)
        assert response.status_code == expected_status_code
