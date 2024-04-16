# Movie Database API Testing

This repository contains a suite of automated tests for The Movie Database (TMDb) API. It includes tests for fetching top-rated movies and posting movie ratings, encapsulated in a containerized environment using Docker. Additionally, it provides a basic load test suite for the "get top-rated movies" endpoint using Locust.

## Getting Started

These instructions will guide you through setting up and running the tests on your local machine for development and testing purposes.

### Prerequisites

To run these tests, you will need:

- Docker installed on your local machine. See the [Docker documentation](https://docs.docker.com/get-docker/) for installation instructions.
- An API key from The Movie Database (TMDb), which you can obtain by signing up for a developer account on their [website](https://www.themoviedb.org/documentation/api).

### Installing

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Build the Docker image:
bash
Copy code
docker build -t pytest-bdd-container .
Running the tests
Run the Docker container to execute the tests:

bash
Copy code
docker run --env-file .env --name my_pytest_container pytest-bdd-container
After the tests have completed, you can retrieve the HTML report from the container:

bash
Copy code
docker cp my_pytest_container:/app/report.html .
The report.html file will be copied to your current directory, where you can open it with any web browser to view the test results.

Test Scenarios
The tests cover the following scenarios:

Fetching top-rated movies with both valid and invalid API keys.
Rating a specific movie with valid authorization and checking for successful acknowledgment.
Attempting to rate a movie without authorization and expecting an unauthorized (401) response.
Rating a movie with invalid input and expecting a bad request (400) response.
Each scenario is documented in the BDD-style feature file test_movies_api.feature.

Built With
Pytest - The testing framework used.
Requests - The library used to make HTTP requests.
Pytest-BDD - BDD library for the Pytest framework.
Docker - Container platform used to encapsulate the testing environment.
Authors
Your Name - Initial work - YourUsername
License
This project is licensed under the MIT License - see the LICENSE.md file for details.
```
