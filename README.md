## Emerging Disentanglement in Auto-Encoder Based Unsupervised Image Content Transfer
--------------

PyTorch implementation of "Emerging Disentanglement in Auto-Encoder Based Unsupervised Image Content Transfer" ([arxiv](https://arxiv.org/abs/1706.00826)). The implementation is based on the architecture of [Fader Networks](https://github.com/facebookresearch/FaderNetworks).
Some of the code is also based on the implementations of [MUNIT](https://github.com/NVlabs/MUNIT) and [DRIT](https://github.com/HsinYingLee/DRIT).

Male to Female (First row is input and Second row is output):

<img src="images/gls_mat.jpg" width="600px">
### Prerequisites
- Python 2.7
- Pytorch 0.4

### Download and Prepare the Data
You can download CelebA from [here](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

Download the dataset. Your data directory should have the following format:
'''
data/
     trainA/
     trainB/
     testA/
     testB/
'''
Contrary to the paper, A is the larger set, for example, A is people with glasses and B is people without.
You can use the provided script '''preprocess_celeba.py''' to split celebA into the above format (with A and B based on the attribute of your choosing).

### To Train
Run '''train.py'''. You can use the following example to run
'''python
python train.py --dataroot './glasses_data' --out './glasses_experiment' --sep 25 --disc-weight 0.001
'''

### To Evaluate
Run '''eval.py'''. You can use the following example to run
'''python
python eval.py --dataroot './glasses_data' --out './glasses_eval' --sep 25 --num_display 10
'''

