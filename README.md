# Installation Instructions
1. Install Docker [here](https://docs.docker.com/get-docker/)
    - Windows: Ensure that you have the latest version of windows (2004) and download the stable version of docker
2. Run ` docker build -f Dockerfile -t <image-name> .`
3. Open powershell and run `docker run -it -p 8888:8888 -d -v $pwd/notebooks:/notebooks <image-name>:latest`


# Updating requirements.txt
* If you have installed a new libary, remember to update requirements.txt with the following code `pip freeze > requirements.txt`


