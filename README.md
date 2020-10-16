

# Cloudant Airport Searcher

Cloudant Airport Searcher is a Python application for finding airports by providing geographic coordinates and distance (latitude, longitude, radius).


## Prerequisites
- Python 3.5.3 or above
- [Cloudant Python SDK](https://github.com/IBM/cloudant-python-sdk)

##Installation
To install Cloudant Python SDK, use ```pip``` or ```easy_install```:
```
pip install --upgrade "ibmcloudant>=0.0.26"
```
or
```
easy_install --upgrade "ibmcloudant>=0.0.26"
```
## Usage

###Setting the environment variables
First, you need to extend your environment variables with the authentication type 
to use 'NOAUTH' authentication while reaching the 'airportdb' database.
This step is necessary for the SDK to know that it doesn't have to use any authenticating.

Set the environment variable on Linux and OSX systems with:
```
export AIRPORTS_AUTH_TYPE=NOAUTH
```
on Windows: 
```
SET AIRPORTS_AUTH_TYPE=NOAUTH
```

### Using the application
By running the application with:
```
python3 airport_searcher.py
```

the application should prompt you for the search parameters.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.