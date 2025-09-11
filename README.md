DermaMamba: A Dual-Branch Vision Mamba Architecture with Linear Complexity for Efficient Skin Lesion Classification<br>
<img width="65" height="15" alt="image" src="https://github.com/user-attachments/assets/544033e7-5869-4c8b-8728-aee683c8b475" />
<img width="75" height="15" alt="image" src="https://github.com/user-attachments/assets/4c2a6d4e-036b-4925-82fb-a617b67fe6f9" />
<img width="62" height="15" alt="image" src="https://github.com/user-attachments/assets/21aceae9-7a63-4253-82c3-99035691e76b" />

🔬 Abstract <br>
DermaMamba introduces a novel dual-branch fusion architecture that synergistically combines CNN-based local feature extraction with Vision Mamba (VMamba) for efficient skin lesion classification. Our approach achieves 92.1% accuracy on the ISIC dataset with linear complexity O(n), representing a 2.0% improvement over state-of-the-art methods while delivering 2.3× inference speedup and 40% memory reduction. <br>
✨ Key Features <br>
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
📊 Performance Results
Main Results on ISIC Dataset <br>
| Method  |  Accuracy (%) | Precision (%)   |Recall (%)|Macro-F1 (%)|Speedup|Memory|
|   :----:  |  :----:   |    :----:   |    :----:   |    :----:   | :----:   | :----:   |
|ResNet50|	86.7|	86.2	|86.1|	86.1|	1.0×	|100%|
|EfficientNet-B0	|88.1	|87.8	|87.5	|87.6	|0.8×	|120%|
|ViT-Base	|87.4	|87.1	|86.9	|87.0	|0.3×	|180%|
|Med-ViT	|90.1	|89.7	|90.5	|90.1|	0.4×	|165%|
|DermaMamba	|92.1	|91.7	|91.3	|91.5	|2.3×	|60%|




