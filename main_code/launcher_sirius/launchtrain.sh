#!/bin/bash
#SBATCH --time=70:59:00 	# job time limit
#SBATCH -J prod_train 	# job name
#SBATCH -N 1 		# number of nodes
#SBATCH --gpus 4
#SBATCH --ntasks=32
#SBATCH --mail-type=END
#SBATCH --mail-user=fraa@kth.se
#SBATCH -p gpu 	# partition to use
#SBATCH --exclusive 	# exclusive acces to nodes
#SBATCH -e /home/serhocal@upvnet.upv.es/output/SHAP125_83pi_prod.%j.err
#SBATCH -o /home/serhocal@upvnet.upv.es/output/SHAP125_83pi_prod.%j.out



# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/serhocal@upvnet.upv.es/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/serhocal@upvnet.upv.es/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/serhocal@upvnet.upv.es/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/serhocal@upvnet.upv.es/anaconda3/bin:$PATH"

    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# source $HOME/.bashrc

echo '----------------------------------------------------------------'

conda activate CONDA_ENV_tf2_11

 

echo '----------------------------------------------------------------'


echo "hola"

nvidia-smi


cd /home/serhocal@upvnet.upv.es/SHAP/XAITB_uu/main_code


python3 main_CNN.py

