# PSTNet_CS231A

This repo is based on the official release of [PSTNet](https://github.com/hehefan/Point-Spatio-Temporal-Convolution).
In order to complete a course project for CS 231a, a series of adaptations needed to be made to the existing PSTNet repository so that it could support few-shot training and contrastive learning pretraining. They are summarized below:

- Adjusted data preprocessing.
- Add dataset file for contrastive learning setting.
- Add few-shot finetuning option.
- Add support for contrastive learning, borrowing code from [Supervised Contrastive Learning](https://github.com/HobbitLong/SupContrast).
