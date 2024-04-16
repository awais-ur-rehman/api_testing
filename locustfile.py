from locust import HttpUser, task, between

class MovieDBUser(HttpUser):
    wait_time = between(1, 5) 

    @task
    def get_top_rated_movies(self):
        self.client.get("/movie/top_rated?api_key=ce2c351a2bd26662a98594d87c683aab")
