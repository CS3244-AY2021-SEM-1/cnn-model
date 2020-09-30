# Installation Instructions (Windows)
1. Install Docker [here](https://docs.docker.com/get-docker/)
    - Windows: Ensure that you have the latest version of windows (2004) and download the stable version of docker
2. Open up powershell and `cd` to the directory containing the DockerFile
3. Run ` docker build -f DockerFile -t <image-name> .`
4. Open powershell and run `docker run -it -p 8889:8889 -d -v $pwd/notebooks:/src/notebooks -v $pwd/models:/src/models -v $pwd/data:/src/data -v $pwd/output:/src/output <image-name>:latest`
5. Run `git submodule update --init --recursive`


# Installation Instructions (Mac)
1. Install Docker [here](https://docs.docker.com/get-docker/)
2. Open up terminal and `cd` to the directory containing the DockerFile
3. Run `docker build -f DockerFile -t <image-name> .`
4. Run `pwd` and copy the result into your clipboard
5. Run `dir=<clipboard-ctrl-v>` <- basically just assign the variable dir to the copied result from pwd
6. Run `docker run -it -p 8889:8889 -d -v $dir/notebooks:/src/notebooks -v $dir/models:/src/models -v $dir/data:/src/data -v $dir/output:/src/output <image-name>`

# Updating requirements.txt
* If you have installed a new libary, remember to update requirements.txt with the following code `pip freeze > requirements.txt`

# Creating notebooks
1. Always append this to the top of your notebook to import the relevant code related to your repo
```
import sys 
sys.path.append('../')
```

# Make sure you complete this procedure right


# SSH into AWS EC2 Instances
1. `cd` into the directory containing the downloaded private key for the instance you want to SSH into
2. Run the command associated with the EC2 instance private key sent on slack
3. If you need to save your output to git or update the code, just do the same commands you on your local and key in your username and password for github when prompted.