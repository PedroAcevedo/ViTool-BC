# ViTool-BC

#### *A software built on top of Cooja, which allows the creation of different energy estimation models and also to visualize in real time the behavior of WSN topology construction.*

---
### Some information

If you use ViTool-BC, don't forget to use the following bibtex entry to cite our paper.

```
@Article{app11167665,
AUTHOR = {Jabba, Daladier and Acevedo, Pedro},
TITLE = {ViTool-BC: Visualization Tool Based on Cooja Simulator for WSN},
JOURNAL = {Applied Sciences},
VOLUME = {11},
YEAR = {2021},
NUMBER = {16},
ARTICLE-NUMBER = {7665},
URL = {https://www.mdpi.com/2076-3417/11/16/7665},
ISSN = {2076-3417},
DOI = {10.3390/app11167665}
}
```

Citation for non-latex users:

```
Jabba D, Acevedo P. ViTool-BC: Visualization Tool Based on Cooja Simulator for WSN. Applied Sciences. 2021; 11(16):7665. https://doi.org/10.3390/app11167665
```

---
### Get Started

<b>Step 1) </b> 

Download Instant Contiki

https://sourceforge.net/projects/contiki/files/Instant%20Contiki/

<b>Step 2) </b> 

Run a Contiki Cooja project, do a simulations and save two mains files from that simulations:

* The CSC file that describe the topology design on the view window.
* The Log file generated after the simulation. There are some commands that need to be printed to can be readed by the tool. Follow the example formats on the files in the example folder. 

<b>Step 3) </b> 

Export those two files, and run the ViTool-BC code with this command:

```
python launch.py
```

There you can create a new project, with the two files mentioned before. Configure according the parameters setup on the Cooja simulator. 

![image](https://user-images.githubusercontent.com/25890069/155926429-de182a51-5a1a-4a7d-a498-71686eee03af.png)

After it you can emulate the simulation with some log outputs about the topology construction or the package loss. 

![image](https://user-images.githubusercontent.com/25890069/155926476-b431c993-f2c1-4008-a575-647d78db8863.png)

Also there are some files that can be useful for Contiki research related, such as "generate_figures.py" and "classes/simulation.py". Any suggestion or changes are welcome. 



