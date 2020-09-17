# Installation Instructions
1. Install Docker [here](https://docs.docker.com/get-docker/)
    - Windows: Ensure that you have the latest version of windows (2004) and download the stable version of docker
2. Open up powershell and `cd` to the directory containing the DockerFile
3. Run ` docker build -f Dockerfile -t <image-name> .`
4. Open powershell and run `docker run -it -p 8889:8889 -d -v $pwd/notebooks:/notebooks <image-name>:latest`
5. Run `git submodule update --init --recursive`


# Updating requirements.txt
* If you have installed a new libary, remember to update requirements.txt with the following code `pip freeze > requirements.txt`


