import pytest

from application import create_app


class TestApplicationBase():

    @pytest.fixture
    def app(self):
        self.flask_app = create_app()
        self.flask_app.config.update({
            "TESTING": True,
        })
        yield self.flask_app

    @pytest.fixture
    def client(self, app):
        return self.flask_app.test_client()

    def runner(self, app):
        return self.flask_app.test_cli_runner()


class TestAppViews(TestApplicationBase):

    def test_root_url(self, client):
        response = client.get('/')
        assert response.status_code == 404
