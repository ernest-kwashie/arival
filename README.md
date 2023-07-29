# node-js-getting-started

A barebones Node.js app using [Express 4](http://expressjs.com/).

This application supports the [Getting Started on Heroku with Node.js](https://devcenter.heroku.com/articles/getting-started-with-nodejs) article - check it out.

## Running Locally

Make sure you have [Node.js](http://nodejs.org/) and the [Heroku CLI](https://cli.heroku.com/) installed.

```sh
$ git clone https://github.com/heroku/node-js-getting-started.git # or clone your own fork
$ cd node-js-getting-started
$ npm install
$ npm start
```

Your app should now be running on [localhost:5001](http://localhost:5001/).

### Using Dockerfile
The base image for this application is built on node:14-slim. This eanbles us to have a ligtweight version of the application and to deploy faster and easier. Port 5001 was exposed, as our nodejs-app listens for traffic on that port. 
![Dockerfile](images\Dockerfile.png)

To build the Dockerfile, run command `docker build -t arvial .`

### Using Docker-compose file
This is a combination of both Loki, Grafana, and Promtail. To visualize with Grafana, there has to be some configurations that would enable our docker-compose file to be up. 
![Loki-config](images\Loki-config.png)

Our Promtail was used to scrape configs from our nodejs-app
![Promtail-config](images\Promtail-config.png)

Overall, these processes enabled us to receive logs from our application, scraping the targets and visualizing it with Grafana. To use the docker-compose file, you simply run command: `docker-compose up -d`
![Docker-compose](images\Docker-compose.png)

### Number to Word
For this, I wrote a Python script that prints the numbers from 0 to 100, converting every tenth number to a wordy version
![numbers-word](images\numbers-word.png)
The script will print numbers from 0 to 100, converting every tenth number (e.g., 10, 20, 30, ..., 100) to its wordy version. For other numbers, it will print the number as is.