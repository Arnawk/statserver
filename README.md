# StatServer

This project aims to solve the [assignment](https://www.notion.so/Assignment-Full-Stack-Engineer-II-5e93c7dc96ad42f4842a4686e21eebdf) given for Full Stack Developer role at charts.com

The goal of this project is to calculate the mean, median, variance and standard deviation of a list of 10 integers and aims to showcase a react stack, apache thrift and docker implementation for the same. 

You can view the live project [here](http://104.197.1.160:3000/).

## Getting Started

This project has three parts in total, categorized into two separate modules. The first one is SystemA, which has a frontend Client made in React and a backend Server in Express. SystemA talks to SystemB, a stateless server in Python, which presents its interface using Apache Thrift. Both systems run in their own Docker containers. 

### Prerequisites

Presence of the following modules with all dependencies sorted out :

Node
NPM
Express
React

Thrift

Python
Pip

Docker

```

### Installing

Please follow the following steps to get started :

* Clone the project from repo

* Navigate to SystemA and SystemB and run the following commands respectively to build the Docker images : 
    docker build -t systema .
    docker build -t systemb .

* Run the images using following commands : 
    docker run -t -p 9090:9090 systemb
    docker run -t -p 3000:3000 systema

* Point browser to IP :
    http://<localhost>:3000


```

## Built With

* Google Compute Engine - VPC Server
* React - UI Interface
* Express - SystemA Backend
* Python 2.7 - SystemB Backend
* Apache Thrift - RPC Interface
* Docker - Container Service 


## Authors

* **Akash Goswamy** - *Research and defining the problem statement* - [Charts.com](https://angel.co/chartshq-eng)

* **Arnaw** - *Development and Deploy* - [Arnaw.in](http://arnaw.in)


## License

This project is licensed under the MIT License

## Acknowledgments

* the amazing people over at stackoverflow!
