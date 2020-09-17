# Installation Instructions (Windows)
1. Install Docker [here](https://docs.docker.com/get-docker/)
    - Windows: Ensure that you have the latest version of windows (2004) and download the stable version of docker
2. Open up powershell and `cd` to the directory containing the DockerFile
3. Run ` docker build -f DockerFile -t <image-name> .`
4. Open powershell and run `docker run -it -p 8889:8889 -d -v $pwd/notebooks:/notebooks -v $pwd/models:/models -v $pwd/data:/data -v $pwd/output:/output <image-name>:latest`
5. Run `git submodule update --init --recursive`


# Installation Instructions (Mac)
1. Install Docker [here](https://docs.docker.com/get-docker/)
2. Open up terminal and `cd` to the directory containing the DockerFile
3. Run `docker build -f DockerFile -t <image-name> .`
4. Run `pwd` and copy the result into your clipboard
5. Run `dir=<clipboard-ctrl-v>` <- basically just assign the variable dir to the copied result from pwd
6. Run "docker run -it -p 8889:8889 -d -v `$dir/notebooks`:`/notebooks` `$dir/models`:`/models` `$dir/data`:`/data` `$dir/output`:`/output` <image-name>"

# Updating requirements.txt
* If you have installed a new libary, remember to update requirements.txt with the following code `pip freeze > requirements.txt`

# Creating notebooks
1. Always append this to the top of your notebook to import the relevant code related to your repo
```
import sys 
sys.path.append('../')
```

# Make sure you complete this procedure right