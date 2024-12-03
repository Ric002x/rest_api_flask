import pytest

from application import create_app


class TestApplicationBase():

    @pytest.fixture
    def app(self):
        self.flask_app = create_app("test")
        self.flask_app.config.update({
            "TESTING": True,
        })
        yield self.flask_app

    @pytest.fixture
    def client(self, app):
        return self.flask_app.test_client()

    def runner(self, app):
        return self.flask_app.test_cli_runner()


class TestUserAPI(TestApplicationBase):

    def user_data(self):
        return {
            "first_name": "Bob",
            "last_name": "Smith",
            "email": "bob@email.com",
            "cpf": "000.000.000-00",
            "birth_date": "2024-06-26"
        }

    def test_root_url(self, client):
        response = client.get('/')
        assert response.status_code == 404

    def test_user_create_post(self, client):
        user_data = self.user_data()
        response = client.post('/user', json=user_data)
        assert b"successfully created" in response.data

    def test_user_cpf_is_unique(self, client):
        user_data = self.user_data()
        client.post('/user', json=user_data)
        response = client.post('/user', json=user_data)
        assert b"already exist" in response.data

    def test_get_user(self, client):
        user_data = self.user_data()
        client.post('/user', json=user_data)

        response = client.get('/user/000.000.000-00')
        assert response.status_code == 200

    def test_get_user_return_404_if_does_not_exist(self, client):
        response = client.get('/user/000.000.000-00')
        assert response.status_code == 404

    def test_get_all_users_return_list_of_users(self, client):
        user_data = self.user_data()
        client.post('/user', json=user_data)

        user_data['cpf'] = '000.000.000-01'
        client.post('/user', json=user_data)

        response = client.get('/user')
        assert b"000.000.000-00" in response.data
        assert b"000.000.000-01" in response.data
