# OpenContractsMX-Backend

## Project Summary

OpenContractMX is a project developed by Platzi Master Students in order to catch more than 350,000 public contracts published by the Government of Mexico and show them in a easy way for reporters, researchers and similars so they can get great information about how the goverment spents in the different areas

## Description

This repository contains the backend code of the project, this includes all the endpoints, queries and different functions to send well-structured data.

If you want to check the Frontend repository, go [here](https://github.com/OpenContractMX/Frontend).
If you want to check the Data Science repository, go [here](https://github.com/OpenContractMX/DataScience).

## API

The API is compound by two main endpoints.

- /api/contracts
- /api/download

With the first one you can get all the contracts in a JSON format filtered by year, month or trimester within the following categories.

- Security
- Education
- Health
- Energy
- Economy
- Governance
- Environment
- Comunication and Mobility
- Social
- Investigation
- Work

With the second one you can get a csv file with the whole data that contains more specific fields that can be useful when making an investigation. You can use the same filters as the first endpoint as well as the same categories.

## Technologies/Stack

For the backend we used:

- FastAPI => For creating the main endpoints and the main business logic
- PostgreSQL => For persisting our clean and formatted data, we are using a instance deployed in AWS RDS
- Heroku => As our deployment platform

## Deployment

We deployed the backend application in heroku, you can find the link [here](https://opencontractsmx.herokuapp.com/).

If you want to see the Frontend deployment that it is using this backend, please go [here]().
