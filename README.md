* Python environment should be installed before the following steps.
To run the project:
1. Download and install VSCode
2. Download the project from github
3. Run the following command in project's terminal (could be done in VSCode terminal window):
for Windows: **pip install -r requirements.txt**
for Mac: **pip3 install -r requirements.txt**
4. This should install all needed libraries.
5. Open test explorer on VSCode
6. Click on the run icon on the explorer
or
run the following in the terminal:
"pytest tests/features"


--
Examples of Test Cases/Scenarios to be added:

**People Endpoint:**
* Retrieve Luke Skywalker’s Information:
* Send a GET request to the people endpoint: https://swapi.dev/api/people/1/.
* Verify that the response contains the expected data (name, height, mass, etc.).
Verify Films and Vehicles:
* Check if Luke Skywalker appears in the specified films and vehicles.
* Validate the film URLs and vehicle URLs.

**Planets Endpoint:**
* Retrieve Yavin IV’s Information:
* Send a GET request to the planets endpoint: https://swapi.dev/api/planets/3/.
Verify that the response contains the expected data (name, rotation period, climate, etc.).
* Check Films and Residents:
* Confirm that Yavin IV appears in the specified film.
Validate the film URL and the absence of residents.

**Starships Endpoint:**
* Retrieve Death Star’s Information:
* Send a GET request to the starships endpoint: https://swapi.dev/api/starships/9/.
* Verify that the response contains the expected data (name, model, crew, etc.).
Validate Hyperdrive Rating:
* Ensure that the hyperdrive rating is within the expected range (e.g., between 0 and 5).
