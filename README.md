# Bamboolib container

## Bamboolib

[Bamboolib](https://bamboolib.8080labs.com/) is a pandas GUI for data transformation, analysis, exploration ans visualization. The free community edition package is designed to be runned in a Jupyter notebook and can be installed as a common python library with pip.

Bamboolib documentation : [https://docs.bamboolib.8080labs.com/documentation/getting-started](https://docs.bamboolib.8080labs.com/documentation/getting-started)

## Custom Docker Image

### Source image

This image is a fork on [this repo](https://github.com/jupyter/docker-stacks/tree/master/base-notebook) which is a ready-to-use base image of the official [Jupyter docker-stacks](https://github.com/jupyter/docker-stacks) for Jupyter applications (the builded image for the official repo is locally pullable from the Docker Hub [https://hub.docker.com/r/jupyter/base-notebook/](https://hub.docker.com/r/jupyter/base-notebook/))

### Custom modifications

Some adjustments were made in this fork 
- The current user (with the right permissions) in the Debian OS of the container must be set at the build stage of the image with the --build-arg parameters (see below the build command example)
- To be noticed : 
  -  The HOME_DIR /home/username is also created and used as the workdir in the container.
  -  the default group of new created users is the "users" group
- With this configuration, you can customize as wanted the username/UID/GID in the container, especially by choosing a user which matches with yout host user for using volumes.
- And precisely in this repo, all the /app folder is exposed as volumes in the Dockerfile, to persist data files and custom notebooks storage by mapping the /home/*username*/app folder inside the container (see below). Feel free to change or not use this configuration

### Bamboolib Functionalities

- Load Packages
```
import pandas as pd
import bamboolib as bam
```

- Load local CSV and Excel files with native Bamboolib loader UI

```
bam
```

![bamboolib dataloader](/assets/main_notebook_screenshot.png)

### Other installed packages

#### PivotTableJS

See [https://github.com/nicolaskruchten/jupyter_pivottablejs](https://github.com/nicolaskruchten/jupyter_pivottablejs) and examples [here](https://towardsdatascience.com/introducing-pivotui-never-use-pandas-to-groupby-and-pivot-your-data-again-ed0fcf95b6ed)

```
from pivottablejs import pivot_ui
...
pivot_ui(df)
```
![PivotUI](/assets/pivot_ui.png)

#### Misc

beautifulsoup4

lxml

requests

SQLAlchemy

voila

### Find this image on Docker Hub

A ready-to-use image has been builded with a "docker" user (UID 1000) belonging to the "users" group (GUI 100), and pushed to the Docker Hub registry for a turnkey use of the container.

[https://hub.docker.com/r/azurscd/bamboolib-container](https://hub.docker.com/r/azurscd/bamboolib-container)

Use it (example) :

```
docker run --name bamboolib-container -d -p 8888:8888 -v <your_path>/app:/home/docker/app azurscd/bamboolib-container:latest
```

Open http://localhost:8888/bamboolib/?token=123456 to access the Jupyter environment with a prepared notebook with data loading functions or if you want to create your own notebook (or http://localhost:8888/bamboolib and manually fill the token form)

## Dev

1. Clone this repo
   
2. You can build your own image with a another user properties, add python packages to install in requirements.txt, etc...

```
docker build --build-arg NB_USER=<your_username> --build-arg NB_UID=<your_uid> --build-arg NB_GID=<your_gid> -t <your_image_name>:<your_tagname> .
```
The current path in the container will be the home directory /home/<your_username>

3. Run command

```
docker run --name <your_container_name> -d -p 8888:8888 -v <your_folder_path>/app:/home/<your_username>/app <your_image_name>:<your_tagname>
```