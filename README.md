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
- And precisely in this repo, the /datasets and the /bamboolib-notebooks folders are exposed as volumes in the Dockerfile, to persist data files and custom notebooks storage by mapping the /home/*username*/datasets and /home/*username*/notebooks folders inside the container (see below). Feel free to change or not use this configuration

### Bamboolib integration

The bamboolib free Community Edition doesn't allow the development of custom additionnal data loaders plugins, so the repo is organized as follow :

1. Main file
- The main.ipynb notebook contains the native bamboolib UI dataloader for static CSV and Excel files (and a few example datasets), and is served as a standalone web page with the [Voila](https://voila.readthedocs.io/en/stable/index.html) extension.
- The dataloader opens a file explorer which starts directly at the /home folder and so gives access to the datasets folder.
- The Voila interactive application is listening on the  8866 port, ie http://localhost:8866/bamboolib-loader/, in the container (a subpath is also passed as parameter in the CMD command of the Dockerfile). See below the docker container running command to map this port to a port in the host.

![bamblib-native-dataloader](/assets/loader_native_gui.png)

1. Other custom notebooks

- You can add custom notebooks in the /bamboolib-notebooks folder, they will be avaiable at the http://localhost:8888/bamboolib-notebooks entrypoint (in the container and on the host server)
- A notebook called manual_dataloaders.ipynb is already proposed, and is ready-to-use with prepared functions to harvest remote data (or local Json files), and open the bamboolib UI.
- The main.ipynb notebook contains a file explorer of the /bamboolib-notebooks folder so that you can navigate with simple hyperlinks from the Voila application and the notebooks.

![bamblib-custom-dataloader](/assets/custom_dataloader.png)

### Find this image on Docker Hub

A ready-to-use image has been builded with a "docker" user (UID 1000) belonging to the "users" group (GUI 100), and pushed to the Docker Hub registry for a turnkey use of the container.

[https://hub.docker.com/r/azurscd/bamboolib-container](https://hub.docker.com/r/azurscd/bamboolib-container)

Use it (example) :

```
docker run --name bamboolib-container -d -p 8866:8866 -p 8888:8888 -v <your_path>/datasets:/home/docker/datasets -v <your_path>/bamboolib-notebooks:/home/docker/bamboolib-notebooks azurscd/bamboolib-container:latest
```
Open http://localhost:8866/bamboolib-loader/ for the Bamboolib native loader GUI on Voila

Open http://localhost:8888/bamboolib-notebooks to access the Jupyter environment with a prepared notebook with data loading functions or if you want to create your own notebook (if needed, the Jupyter token is 123456)

## Dev

1. Clone this repo
   
2. You can build your own image with a another user properties, add python packages to install in requirements.txt, etc...

```
docker build --build-arg NB_USER=<your_username> --build-arg NB_UID=<your_uid> --build-arg NB_GID=<your_gid> -t <your_image_name>:<your_tagname> .
```
The current path in the container will be the home directory /home/<your_username>

3. Run command

```
docker run --name <your_container_name> -d -p 8866:8866 -p 8888:8888 -v <your_folder_path>/datasets:/home/<your_username>/datasets -v <your_folder_path>/notebooks:/home/<your_username>/notebooks <your_image_name>:<your_tagname>
```