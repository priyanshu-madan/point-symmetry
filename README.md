# Line of symmetry detection

Create and implement an algorithm that, when given a set of points on an infinite plane, will return the complete set of lines of symmetry for those points.

A line of symmetry is defined to be a line such that every point in the input set, when reflected across the line, finds another point in the input set. And we would like the code to find for us the guaranteed-complete set of these lines.

## Installation process

### 1) Running via Docker Hub

#### Step 1. Download and install Docker for desktop: https://www.docker.com/products/docker-desktop

Installation video: https://www.youtube.com/watch?v=LtooWDUL1Js&ab_channel=NRDYTech

#### Step 2. Create a folder on desktop

#### Step 3. Open terminal / command-prompt and change current working directory to that folder:

Folder name is test in my case. This is where the graphs will be saved after we run the script

```cmd
cd Desktop/test
```

#### Step 4. Running the script

Open terminal / command-prompt and type in the following command:

```cmd
docker pull pmadan3/point-symmetry
```

Next, we want to run the pulled docker container. Type in the following command:

```cmd
docker run -it --mount src=`pwd`,target=/output,type=bind pmadan3/point-symmetry
```
Select the option you want to run. 

When the command is successful, The graph (graph.png) will be saved in the folder we created.


##### Docker Repository link: https://hub.docker.com/repository/docker/pmadan3/point-symmetry

### 2) Running via GitHub clone

Open Terminal in a directory (I am opening mine in a Pycharm project).

In the terminal type the following commands one by one:

```cmd
git clone https://github.com/priyanshu-madan/point-symmetry.git
cd point-symmetry
pip install -r requirements.txt
python main.py
```

When the run is successful, the terminal will display the lines generated and the generated graph will be saved in the directory as "graphs.png"
