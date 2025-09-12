# DermaMamba: A Dual-Branch Vision Mamba Architecture with Linear Complexity for Efficient Skin Lesion Classification<br>
<img width="65" height="15" alt="image" src="https://github.com/user-attachments/assets/544033e7-5869-4c8b-8728-aee683c8b475" />
<img width="75" height="15" alt="image" src="https://github.com/user-attachments/assets/4c2a6d4e-036b-4925-82fb-a617b67fe6f9" />
<img width="62" height="15" alt="image" src="https://github.com/user-attachments/assets/21aceae9-7a63-4253-82c3-99035691e76b" />

# 🔬 Abstract <br>
DermaMamba introduces a novel dual-branch fusion architecture that synergistically combines CNN-based local feature extraction with Vision Mamba (VMamba) for efficient skin lesion classification. Our approach achieves 92.1% accuracy on the ISIC dataset with linear complexity O(n), representing a 2.0% improvement over state-of-the-art methods while delivering 2.3× inference speedup and 40% memory reduction. <br>
# ✨ Key Features <br>
🚀 Linear Complexity: VMamba-based global context modeling with O(n) complexity vs O(n²) for transformers <br>
🔄 Dual-Branch Architecture: Synergistic fusion of CNN local features and VMamba global context <br>
🏥 Medical Domain Integration: ABCDE rule features and clinical examination-inspired scanning patterns <br>
⚡ High Efficiency: 2.3× faster inference and 40% memory reduction compared to Vision Transformers <br>
🎯 Superior Performance: 92.1% accuracy with balanced precision (91.7%) and recall (91.3%) <br>
🔍 Clinical Interpretability: Attention visualization aligned with dermatological diagnostic practices <br>
🏗️ Architecture Overview <br>
<img width="416" height="230" alt="image" src="https://github.com/user-attachments/assets/89b1a31a-75f2-42e9-85de-30dbe5610611" />
<br>
 
DermaMamba consists of four main components: <br>
Input Processing: Medical-aware preprocessing with ABCDE rule integration <br>
CNN Branch: ResNet50 backbone with dual attention (spatial + channel) <br>
VMamba Branch: Multi-directional scanning with selective state space models <br>
State Space Fusion: Adaptive weighting mechanism for optimal feature integration <br>
Multi-Directional Scanning Strategies <br>
Spiral Scanning: Mimics clinical examination patterns <br>
Radial Scanning: Captures center-to-periphery relationships <br>
Boundary-Aware Scanning: Focuses on lesion contours <br>
Raster Scanning: Traditional sequential processing <br>
<br>
📊 Performance Results
Main Results on ISIC Dataset <br>
| Method  |  Accuracy (%) | Precision (%)   |Recall (%)|Macro-F1 (%)|Speedup|Memory|
|   :----:  |  :----:   |    :----:   |    :----:   |    :----:   | :----:   | :----:   |
|ResNet50|	86.7|	86.2	|86.1|	86.1|	1.0×	|100%|
|EfficientNet-B0	|88.1	|87.8	|87.5	|87.6	|0.8×	|120%|
|ViT-Base	|87.4	|87.1	|86.9	|87.0	|0.3×	|180%|
|Med-ViT	|90.1	|89.7	|90.5	|90.1|	0.4×	|165%|
|DermaMamba	|92.1	|91.7	|91.3	|91.5	|2.3×	|60%|
<br>
Statistical Significance<br>
All improvements are statistically significant (p < 0.001)<br>
Large effect sizes (Cohen's d > 0.8) across all metrics<br>
95% confidence intervals through bootstrap analysis<br>
<br>

# 🚀 Quick Start <br>
## Installation <br>
## Clone the repository <br>
git clone https://github.com/your-username/DermaMamba.git <br>
cd DermaMamba <br>
## Create conda environment  <br>
conda create -n dermamamba python=3.8  <br>
conda activate dermamamba  <br>
## Install dependencies

pip install -r requirements.txt

## Install VMamba selective scan kernel

cd selective_scan && pip install.

### Dependencies

torch>=2.0.1

torchvision>=0.15.1

numpy>=1.21.0

opencv-python>=4.5.0

albumentations>=1.3.0

timm>=0.9.0

einops>=0.6.0

scikit-learn>=1.0.0

matplotlib>=3.5.0

seaborn>=0.11.0

tqdm>=4.64.0

# Dataset Preparation<br>
### Download ISIC dataset<br>
python scripts/download_isic.py --output_dir data/

### Preprocess data <br>
python scripts/preprocess_data.py \
 &nbsp; &nbsp;&nbsp; &nbsp;   --data_dir data/ISIC \
 &nbsp; &nbsp;&nbsp; &nbsp;   --output_dir data/processed \
 &nbsp; &nbsp;&nbsp; &nbsp;   --image_size 224
### Training
### Train DermaMamba
python train.py \
&nbsp; &nbsp;&nbsp; &nbsp;    --config configs/dermamamba.yaml \
&nbsp; &nbsp;&nbsp; &nbsp;    --data_dir data/processed \
&nbsp; &nbsp;&nbsp; &nbsp;   --output_dir experiments/dermamamba \
&nbsp; &nbsp;&nbsp; &nbsp;    --gpus 0,1,2,3

### Resume training from checkpoint
python train.py \
&nbsp; &nbsp;&nbsp; &nbsp;     --config configs/dermamamba.yaml \
&nbsp; &nbsp;&nbsp; &nbsp;     --resume experiments/dermamamba/checkpoints/best.pth

### Inference
# Single image inference
python inference.py \
&nbsp; &nbsp;&nbsp; &nbsp;     --model_path experiments/dermamamba/checkpoints/best.pth \
&nbsp; &nbsp;&nbsp; &nbsp;     --image_path test_images/lesion.jpg \
&nbsp; &nbsp;&nbsp; &nbsp;    --output_dir results/

### Batch inference
python inference.py \
&nbsp; &nbsp;&nbsp; &nbsp;     --model_path experiments/dermamamba/checkpoints/best.pth \
&nbsp; &nbsp;&nbsp; &nbsp;     --data_dir test_images/ \
&nbsp; &nbsp;&nbsp; &nbsp;     --output_dir results/ \
&nbsp; &nbsp;&nbsp; &nbsp;     --batch_size 32

# 📁 Project Structure
```bash
DermaMamba/ 
├── configs/                 # Configuration files 
│   ├── dermamamba.yaml     # Main model config 
│   └── ablation/           # Ablation study configs 
├── data/                   # Dataset directory 
├── models/                 # Model implementations 
│   ├── dermamamba.py      # Main DermaMamba model 
│   ├── vmamba.py          # VMamba implementation 
│   ├── fusion.py          # State space fusion module 
│   └── attention.py       # Attention mechanisms 
├── datasets/              # Dataset classes 
├── utils/                 # Utility functions 
├── scripts/               # Data processing scripts 
├── experiments/           # Training outputs 
├── assets/               # Documentation assets 
├── train.py              # Training script 
├── inference.py          # Inference script 
├── evaluate.py           # Evaluation script 
└── requirements.txt      # Dependencies 
```
# 🔬 Reproducing Results <br>
## Ablation  <br>
### Run complete ablation study <br>
bash scripts/run_ablation.sh

# Individual ablation experiments<br>
python train.py --config configs/ablation/cnn_only.yaml <br>
python train.py --config configs/ablation/spatial_attention.yaml <br>
python train.py --config configs/ablation/vmamba_added.yaml <br>

# Hyperparameter Analysis <br>
## Learning rate sweep <br>
python scripts/hyperparameter_sweep.py <br>
&nbsp; &nbsp;&nbsp; &nbsp; --param learning_rate <br>
&nbsp; &nbsp;&nbsp; &nbsp; --values 1e-5 5e-5 1e-4 5e-4 1e-3 <br>

## Batch size analysis <br>
python scripts/hyperparameter_sweep.py <br>
&nbsp; &nbsp;&nbsp; &nbsp;    --param batch_size <br>
&nbsp; &nbsp;&nbsp; &nbsp;    --values 16 32 64 128 256 <br>

## Attention Visualization <br>
### Generate attention maps <br>
python visualize_attention.py <br>
&nbsp; &nbsp;&nbsp; &nbsp;    --model_path experiments/dermamamba/checkpoints/best.pth <br>
 &nbsp; &nbsp;&nbsp; &nbsp;   --image_path test_images/melanoma.jpg <br>
  &nbsp; &nbsp;&nbsp; &nbsp;  --output_dir visualizations/ <br>





















