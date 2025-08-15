class AnatomicalPositionEncoding(nn.Module):
    def __init__(self, embed_dim=768):
        super().__init__()
        # 定义常见的皮肤病变解剖部位
        self.body_parts = {
            'head_neck': 0, 'trunk': 1, 'upper_extremity': 2,
            'lower_extremity': 3, 'palms_soles': 4, 'unknown': 5
        }
        self.position_embedding = nn.Embedding(len(self.body_parts), embed_dim)

    def forward(self, body_part_ids):
        return self.position_embedding(body_part_ids)


# 在主模型中集成
class DermaMamba(nn.Module):
    def __init__(self, ...):
        # ... 其他初始化
        self.anatomical_encoder = AnatomicalPositionEncoding()

    def forward(self, x, body_part_id=None):
        # 核心特征提取
        cnn_features = self.cnn_branch(x)
        vmamba_features = self.vmamba_branch(x)

        # 添加解剖位置编码（如果提供）
        if body_part_id is not None:
            pos_encoding = self.anatomical_encoder(body_part_id)
            # 将位置编码添加到特征中
            cnn_features += pos_encoding.unsqueeze(-1).unsqueeze(-1)

        return self.fusion_module(cnn_features, vmamba_features)
