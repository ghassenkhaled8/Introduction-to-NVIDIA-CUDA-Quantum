# Introduction-to-NVIDIA-CUDA-Quantum
In today's noisy intermediate-scale quantum (NISQ) era, quantum computers are still heavily affected by quantum noise. If we want to simulate their behaviour faithfully, we need a lot of computing power. NVIDIA CUDA Quantum software allows multiple CPUs or GPUs to be used for these simulations. This course will show how to program this software and how to use many of its features. Attention will be focused in particular on the simulation of quantum circuits with a larger number of qubits, the simulation of quantum noise and specific quantum circuit applications on multiple CPUs or GPUs. The final part of the course will focus on the possibilities of using specific quantum processors (QPUs) from quantum hardware manufacturers or their emulation.
Clusters Barbora and Karolina can only be accessed using the SSH protocol. You will need an SSH client, a private SSH key, and its passphrase to log in to the cluster. Below are links to our video tutorials, which will help you to set everything up:

TUTORIAL: Accessing to IT4I clusters - Windows training user - YouTube

TUTORIAL: Accessing to IT4I clusters - Linux training user - YouTube

 Python 3.10 is recommended for the current version of NVIDIA CUDA Quantum simulator. It is also recommended to use Conda to create a separate environment for this simulator. If you are not already using Conda, you can install a minimal version (miniconda) following the instructions here: https://docs.anaconda.com/miniconda/

Once you have Conda installed, you can create an environment with the required version of Python and other software using the command: 

conda create -y -n cuda-quantum python=3.10 pip notebook

You can then install the simulator itself using the command:

conda run -n cuda-quantum pip install cuda-quantum

You can then activate the created environment as follows:

conda activate cuda-quantum

Now you are ready to program the simulator using Python scripts or Jupyter notebooks. This procedure is for installation on your PC for testing smaller examples on local CPUs. For larger tasks on CPUs and especially on GPUs, you will use a ready-made environment on a supercomputer, to which you will connect remotely.
