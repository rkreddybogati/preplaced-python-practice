# Python Full Throttle By Paul Deitel


## Opening Notes:
https://on24static.akamaized.net/event/45/17/49/2/rt/1/documents/resourceList1713971859345/pythonftopeningnotes.pdf  


I am looking forward to presenting today's live training on a beautiful spring day just outside of Boston, MA, USA!

I'll present most of today's content in Jupyter Notebooks using the JupyterLab interface in my web browser. You can learn more about JupyterLab at https://jupyterlab.readthedocs.io/en/latest/


For a zero-install JupyterLab environment in which you can run most of today’s code (MyBinder does not currently support Python 3.12), go to the following link: https://mybinder.org/v2/gh/pdeitel/PythonFullThrottle/HEAD?urlpath=lab

MyBinder environments are temporary. If you do not interact with them for a while, you might need to revisit the link above to start a new cloud environment.

So keep the link handy.


## Anaconda:
I'll use a local installation of the Anaconda Python distribution from https://www.anaconda.com/download

They provide installers for Windows, macOS and Linux. Anaconda installs everything you need to run the code for today’s presentation.

Anaconda defaults to Python 3.11, so if you want a Python 3.12 environment, from the root folder of my content you can run the following commands at your command line to create an environment named py3_12 then activate it.

### Commanda for installing Anaconda: 

conda env create --file environment.3.12.yml

conda activate py3_12


## Docker
Docker users can run a docker container. You can install Docker Desktop from https://www.docker.com/products/docker-desktop/.

Then open a command prompt, Terminal window or shell (depending on your operating system), cd to the folder with the code examples on your local machine and execute the following command without pressing Enter until you’ve input the entire command:

docker run --rm -p 8888:8888 -it --user root -v .:/home/jovyan/work jupyter/scipy-notebook start.sh jupyter lab

This will attach the current folder (.) to the docker container's folder named /home/jovyan/work.

You can then access the Jupyter notebooks from your local machine at https://localhost:8888/lab (the full URL with a security key will be displayed in the command line)

Welcome everyone! Strap yourselves in, we have a TON of information to cover today

The session has started, you should all be hearing Paul now.

We now have closed captioning available in our live events! You can enable closed captioning in the Media Player: hover your mouse over the bottom right corner and you’ll see CC–click that to enable closed captioning.

The audio and video should be good for all. If you are having any issues, please be sure you are not connected to a VPN and refresh your browser to see if it helps. Thank you and enjoy the course!

## Useful Links:
https://deitel.com/LearnWithDeitel

https://www.oreilly.com/library/view/c20-fundamentals/9780136875185/

https://github.com/pdeitel/PythonFullThrottle

https://www.anaconda.com/download

https://mybinder.org/v2/gh/pdeitel/PythonFullThrottle/HEAD?urlpath=lab

https://colab.research.google.com/?utm_source=scs-index


